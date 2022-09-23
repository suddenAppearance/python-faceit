import json
from typing import Callable, Any, TypeVar

import urllib3

from types_ import GamesList

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
    message = "Hello"

    def games(self, offset: int | None, limit: int | None) -> GamesList:
        r = self.http.request("GET", f"https://open.faceit.com/data/v4/games?offset={offset}&limit={limit}")
        return json.loads(r.data)