def study_schedule(permanence_period, target_time):
    if type(target_time) != int:
        return None
    qtd_estudantes_online = 0

    for aluno in permanence_period:
        if (
            type(aluno[0]) != int
            or type(aluno[1]) != int
            or aluno[0] < 0
            or aluno[1] > 24
        ):
            return None

        if target_time in range(aluno[0], aluno[1] + 1):
            qtd_estudantes_online += 1

    return qtd_estudantes_online
