from entities.event import Target
from systems.helpers import get_staff

def incident_penalty(festival) -> float:
    total = 0
    for event in festival.events:
        if event.penalty_target == Target.PERFORMANCE:
            mitigator = get_staff(festival, event.mitigated)
            mitigation = mitigator.mitigation_value if mitigator else 0
            damage = max(event.penalty_value - mitigation, 0)
            total += damage
    return total

