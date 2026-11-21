; Inno Setup script for aion2-menu
#define MyAppName "Aion 2 Cheat Menu"
#define MyAppVersion "0.6.3"
#define MyAppPublisher "aion2-menu contributors"
#define MyAppExeName "aion2-menu.exe"

[Setup]
AppId={{7F1B2E4A-AION-CHEATMENU-2026}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\Aion2Menu
DefaultGroupName=Aion 2 Cheat Menu
DisableProgramGroupPage=yes
OutputBaseFilename=aion2-menu-{#MyAppVersion}-setup
Compression=lzma2
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "..\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\Aion 2 Cheat Menu"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\Offsets"; Filename: "{app}\global_offsets.json"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch Aion 2 Cheat Menu"; Flags: postinstall nowait skipifsilent