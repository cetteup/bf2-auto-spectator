class GameInstanceState:
    # Global details
    __spectator_on_server: bool = False
    __hud_hidden: str = ''

    # Server details
    __server_ip: str = ''
    __server_port: str = ''
    __server_password: str = ''
    __server_player_count: int = -1

    # Map details (map is as in one entry in the map rotation)
    __rotation_map_name: str = ''
    __rotation_spawned: bool = False

    # Round details
    __round_team: int = -1
    __round_started_spectation: bool = False

    # Error details
    __error_restart_required: bool = False

    # Global getter/setter functions
    def set_spectator_on_server(self, spectator_on_server: bool):
        self.__spectator_on_server = spectator_on_server

    def spectator_on_server(self) -> bool:
        return self.__spectator_on_server

    def set_hud_hidden(self, hud_hidden: bool):
        self.__hud_hidden = hud_hidden

    def hud_hidden(self) -> bool:
        return self.__hud_hidden

    # Server getter/setter functions
    def set_server_ip(self, server_ip: str):
        self.__server_ip = server_ip

    def get_server_ip(self) -> str:
        return self.__server_ip

    def set_server_port(self, server_port: str):
        self.__server_port = server_port

    def get_server_port(self) -> str:
        return self.__server_port

    def set_server_password(self, server_password: str):
        self.__server_password = server_password

    def get_server_password(self) -> str:
        return self.__server_password

    def set_server_player_count(self, player_count: int):
        self.__server_player_count = player_count

    def get_server_player_count(self) -> int:
        return self.__server_player_count

    def set_rotation_map_name(self, map_name: str):
        self.__rotation_map_name = map_name

    def get_rotation_map_name(self) -> str:
        return self.__rotation_map_name

    def set_rotation_spawned(self, spawned: bool):
        self.__rotation_spawned = spawned

    def rotation_spawned(self) -> bool:
        return self.__rotation_spawned

    def set_round_team(self, team: int):
        self.__round_team = team

    def get_round_team(self) -> int:
        return self.__round_team

    def set_round_started_spectation(self, startet_spectation: bool):
        self.__round_started_spectation = startet_spectation

    def round_started_spectation(self) -> bool:
        return self.__round_started_spectation

    def set_error_restart_required(self, restart_required: bool):
        self.__error_restart_required = restart_required

    def error_restart_required(self) -> bool:
        return self.__error_restart_required

    # Reset relevant fields after map rotation
    def map_rotation_reset(self):
        self.__rotation_map_name = ''
        self.__rotation_spawned = False
        self.__round_team = -1
        self.__round_started_spectation = False

    # Reset relevant fields when round ended
    def round_end_reset(self):
        self.__round_team = -1
        self.__round_started_spectation = False

    # Reset relevant fields after/on game restart
    def restart_reset(self):
        self.__spectator_on_server = False
        self.__hud_hidden = False
        self.__rotation_map_name = ''
        self.__rotation_spawned = False
        self.__round_team = -1
        self.__round_started_spectation = False
        self.__error_restart_required = False
