import json
from pathlib import Path
from entities.artist import Artist, MusicGenre
from entities.event import Target, Mitigated, Type, Event
from entities.objective import Objective, Types
from entities.venue import Venue, Locations
from entities.staff import Staff, Services

DATA_DIR = Path("data")

def load_artists() -> list[Artist]:
    path = DATA_DIR / "artists.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    artists_list: list[Artist] = []
    for item in raw_list:
        name = item["name"]
        genre_str = item["genre"]
        genre = MusicGenre[genre_str]
        reputation = item["reputation"]
        fee = item["fee"]
        level = item["level"]
        is_retired = item["is_retired"]

        artist = Artist(
            name=name,
            genre=genre,
            reputation=reputation,
            fee=fee,
            level=level,
            is_retired=is_retired
        )
        artists_list.append(artist)
    return artists_list


def load_venues() -> list[Venue]:
    path = DATA_DIR / "venues.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    venues_list: list[Venue] = []
    for item in raw_list:
        name = item["name"]
        quality = item["quality"]
        capacity = item["capacity"]
        rent = item["rent"]
        reputation = item["reputation"]
        location_str = item["location"]
        location = Locations[location_str]
        level = item["level"]
        is_owned = item["is_owned"]

        venue = Venue(
            name=name,
            quality=quality,
            capacity=capacity,
            rent=rent,
            reputation=reputation,
            location=location,
            level=level,
            is_owned=is_owned
        )
        venues_list.append(venue)
    return venues_list


def load_staff() -> list[Staff]:
    path = DATA_DIR / "staff.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    staff_list: list[Staff] = []
    for item in raw_list:
        type_str = item["type"]
        service_type = Services[type_str]
        level = item["level"]
        cost = item["cost"]
        effect_value = item["effect_value"]
        min_reputation = item["min_reputation"]
        mitigation_value = item["mitigation_value"]

        staff_member = Staff(
            type=service_type,
            level=level,
            cost=cost,
            effect_value=effect_value,
            min_reputation=min_reputation,
            mitigation_value=mitigation_value
        )
        staff_list.append(staff_member)
    return staff_list


def load_objectives() -> list[Objective]:
    path = DATA_DIR / "objectives.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    objective_list: list[Objective] = []
    for item in raw_list:
        type_str = item["type"]
        obj_type = Types[type_str]
        target_value = item["target_value"]
        description = item["description"]
        fulfilled = item["fulfilled"]
        max_reputation = item["max_reputation"]

        obj = Objective(
            type = obj_type,
            target_value = target_value,
            description = description,
            fulfilled = fulfilled,
            max_reputation=max_reputation
        )
        objective_list.append(obj)
    return objective_list


def load_events() -> list[Event]:
    path = DATA_DIR / "events.json"
    with path.open("r", encoding="utf-8") as f:
        raw_list = json.load(f)

    event_list: list[Event] = []
    for item in raw_list:
        event_id = item["id"]
        name = item["name"]
        description = item["description"]
        resolve_cost = item["resolve_cost"]
        penalty_value = item["penalty_value"]
        type_str = item["type"]
        event_type = Type[type_str]
        mitigated_str = item["mitigated"]
        mitigated_by = Mitigated[mitigated_str] if mitigated_str else None
        target_str = item["target"]
        target = Target[target_str]
        resolved = item["resolved"]
        is_positive = item["is_positive"]

        event = Event(
            id = event_id,
            name = name,
            description = description,
            resolve_cost = resolve_cost,
            penalty_value = penalty_value,
            penalty_from = event_type,
            penalty_target = target,
            mitigated = mitigated_by,
            resolved = resolved,
            is_positive = is_positive
        )
        event_list.append(event)
    return event_list


