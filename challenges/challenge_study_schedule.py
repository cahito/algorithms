def study_schedule(permanence_period, target_time):
    qtd_estudantes_online = 0

    try:
        if type(target_time) != int:
            raise TypeError
        for aluno in permanence_period:
            if target_time in range(aluno[0], aluno[1] + 1):
                qtd_estudantes_online += 1

        return qtd_estudantes_online
    except Exception:
        return None