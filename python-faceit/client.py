import json
from typing import TypeVar, Literal
from urllib.parse import urlencode

import urllib3
from urllib3.util import Url

from types_ import GamesList, GameDetail, ChampionshipsList

T = TypeVar('T')


class SyncClient:
    def __init__(self, api_key: str, **config):
        headers = config.get('headers') or {}
        headers.update({"Authorization": "Bearer " + api_key})

        self.http = urllib3.PoolManager(
            headers=headers,
            **config
        )

    def __aenter__(self):
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.http.clear()


class DataWrapper(SyncClient):
    def get_championships(self, game: int, type: Literal['all', 'upcoming', 'ongoing', 'past']) -> ChampionshipsList:
        pass

    def get_games(self, offset: int | None = None, limit: int | None = None) -> GamesList:
        params = {k: v for k, v in (("offset", offset), ("limit", limit)) if v is not None}
        r = self.http.request("GET", f"https://open.faceit.com/data/v4/games?{urlencode(params)}")
        return json.loads(r.data)

    def get_game_by_id(self, game_id: int) -> GameDetail:
        r = self.http.request("GET", f"https://open.faceit.com/data/v4/games/{game_id}")
        return json.loads(r.data)

    def get_game_parent_by_game_id(self, game_id: int) -> GameDetail:
        r = self.http.request("GET", f"https://open.faceit.com/data/v4/games/{game_id}/parent")
        return json.loads(r.data)


print(Url(scheme='https',
          host='open.faceit.com',
          path='Generate+value'))
