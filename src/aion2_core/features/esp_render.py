"""Player / mob ESP rendering hooked into the overlay pass."""
from __future__ import annotations

from aion2_core.features.base_feature import BaseFeature


class EspRender(BaseFeature):
    slug = "esp"
    display_name = "ESP"
    default_bind = "F2"

    def __init__(self) -> None:
        super().__init__()
        self.show_players = True
        self.show_mobs = True
        self.show_distance = True
        self.box_color = (0, 255, 120, 200)

    def tick(self) -> None:
        if not self.enabled or self.process is None:
            return
        entities = self.process.read_entity_list(self.offsets.resolve("entity_list"))
        for ent in entities:
            if ent.is_player and not self.show_players:
                continue
            if not ent.is_player and not self.show_mobs:
                continue
            screen = self.process.world_to_screen(ent.pos, self.offsets.resolve("view_matrix"))
            self._draw_box(screen, ent.name)

    def _draw_box(self, screen, label: str) -> None:
        # Overlay backend exposes draw_rect / draw_text through the context.
        overlay = self._ctx.get("overlay")
        if overlay is None:
            return
        x, y = screen.x - 30, screen.y - 60
        overlay.draw_rect(x, y, 60, 120, self.box_color)
        if self.show_distance or label:
            overlay.draw_text(x, y - 14, label)