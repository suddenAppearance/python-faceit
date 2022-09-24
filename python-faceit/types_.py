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


class OrganizerDetail(BaseType):
    pass


class JoinChecks(BaseType):
    allowed_team_types: list[str]
    blacklist_geo_countries: list[str]
    join_policy: str
    max_skill_level: int
    membership_type: str
    min_skill_level: int
    whitelist_geo_countries: list[str]
    whitelist_geo_countries_min_players: int


class Prize(BaseType):
    faceit_points: int
    rank: int


class Schedule(BaseType):
    date: int
    status: str


class Stream(BaseType):
    active: str
    platform: str
    source: str
    title: str


class SubstitutionConfiguration(BaseType):
    max_substitutes: int
    max_substitutions: int


class ChampionshipDetail(BaseType):
    anticheat_required: bool
    avatar: str
    background_image: str
    championship_id: str
    championship_start: int
    checkin_clear: int
    checkin_enabled: bool
    checkin_start: int
    cover_image: str
    current_subscriptions: int
    description: str
    faceit_url: str
    featured: bool
    full: bool
    game_data: GameDetail
    game_id: str
    id: str
    join_checks: JoinChecks
    name: str
    organizer_data: OrganizerDetail
    organizer_id: str
    prizes: list[Prize]
    region: str
    rules_id: str
    schedule: dict[str, Schedule]
    seeding_strategy: str
    slots: int
    status: str
    stream: Stream
    subscription_end: int
    subscription_start: int
    subscription_locked: bool
    substitution_configuration: SubstitutionConfiguration
    total_groups: int
    total_prizes: int
    total_rounds: int
    type: str


class ChampionshipsList(BaseType):
    end: int
    items: list[ChampionshipDetail]
    start: int


class Results(BaseType):
    score: dict[str, int]
    winner: str


class Team(BaseType):
    pass


class MatchDetail(BaseType):
    best_of: int
    broadcast_start_time: int
    broadcast_start_time_label: str
    calculate_elo: bool
    chat_room_id: str
    competition_id: str
    competition_name: str
    competition_type: str
    configured_at: int
    demo_url: list[str]
    faceit_url: str
    finished_at: str
    game: str
    group: int
    match_id: str
    organizer_id: str
    region: str
    results: Results
    round: int
    scheduled_at: int
    started_at: int
    status: str
    teams: dict[str, Team]


class MatchesList(BaseType):
    end: int
    items: list[MatchDetail]
    start: int
