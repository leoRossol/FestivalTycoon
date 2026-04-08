# GERENCIA OBJETIVOS DO JOGO
import math
import random
from core.reader import load_objectives
from entities.objective import Types

# defines how many objectives to draw based in player rep
def how_many_objs(reputation: int) -> int:
    if reputation < 25: return 2
    elif reputation < 50: return 3
    elif reputation < 75: return 4
    else: return 5

# called in core/game at the start of a festival
# returns ---
def generate_objectives(player):
    all_objectives = load_objectives()
    available = [
        obj for obj in all_objectives
        if obj.max_reputation >= player.reputation
    ]
    if len(available) < 2:
        available = all_objectives[:2]

    n = min(how_many_objs(player.reputation), len(available))
    chosen = random.sample(available, n)

    for obj in chosen:
        obj.fulfilled = False

    return chosen

# called in at the end of the simulation, after profit and lineup ready
def objective_check(festival):
    for objective in festival.objectives:
        if objective.type == Types.PROFIT:
            objective.fulfilled = festival.profit >= objective.target_value

        elif objective.type == Types.LINEUPSIZE:
                objective.fulfilled = len(festival.lineup) >= objective.target_value

        elif objective.type == Types.LINEUPLEVEL:
            if not festival.lineup:
                objective.fulfilled = False
            else:
                avg_level = sum(a.level for a in festival.lineup) / len(festival.lineup)
                objective.fulfilled = avg_level >= objective.target_value

        elif objective.type == Types.LOCATION:
            if festival.venue is None:
                objective.fulfilled = False
            else:
                objective.fulfilled = festival.venue.location.name == objective.target_value

        elif objective.type == Types.GENRE:
            if not festival.lineup:
                objective.fulfilled = False
            else:
                genre_count = {}
                for artist in festival.lineup:
                    genre_count[artist.genre] = genre_count.get(artist.genre, 0) +1
                dominant = max(genre_count, key=genre_count.get)
                majority = genre_count[dominant] > len(festival.lineup) / 2
                objective.fulfilled = dominant.name == objective.target_value and majority

# called in core/game to decide if the festival was successful
def minimum_obj_met(festival) -> bool:
    count = 0
    for objective in festival.objectives:
        if objective.fulfilled:
            count += 1
    if math.ceil(len(festival.objectives)/2) <= count:
        return True
    else: return False

# called in core/game to update failure counter
def consecutive_failure(player, festival):
    if minimum_obj_met(festival):
        player.consecutive_failures = 0
    else :
        player.consecutive_failures += 1

# called in core/game to check if player was fired
def check_dismissal(player) -> bool:
    return player.consecutive_failures > 5
