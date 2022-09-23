from typing import TypedDict


class BaseType(TypedDict):
    pass


class Assets(BaseType):
    cover: str
    featured_img_l: str
    featured_img_m: str
    featured_img_s: str
    flag_img_icon: str
    flag_img_l: str
    flag_img_m: str
    flag_img_s: str
    landing_page: str


class GameDetail(BaseType):
    assets: Assets
    game_id: str
    long_label: str
    order: str
    parent_game_id: str
    platforms: list[str]
    regions: list[str]
    short_label: str


class GamesList(BaseType):
    end: int
    items: list[GameDetail]
    start: int