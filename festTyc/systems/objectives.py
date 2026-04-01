# GERENCIA OBJETIVOS DO JOGO
from entities.event import Type


# gerar objetivos (player)
    # 1-n objetivos baseado na reputacao do player

# validar (festival)
def objective_check(festival):
    for objective in festival:
        if objective.type == Type.PROFIT:
            if objective.target_value <= festival.profit:
                objective.fulfilled = True
            else: objective.fulfilled = False

        if objective.type == Type.LINEUPSIZE:
            if objective.target_value <= len(festival.lineup):
                objective.fulfilled = True
            else: objective.fulfilled = False

        if objective.type == Type.LINEUPLEVEL:
            if objective.target_value <= festival.lineup:
                objective.fulfilled = True
            else: objective.fulfilled = False

        if objective.type == Type.LOCATION:
            if objective.target_value == festival.venue.location:
                objective.fulfilled = True
            else: objective.fulfilled = False



    # verificar objetivos depois da simulacao, seta fulfilled

# check minimum met (festival)
    # verifica se ao menos metade dos obj. foram concluidos

# track consecutive failures (player, objectives)
    # incrementa ou resta contador

# check dismissal (player)
    # verifica se o player vai ser demitido por falhas