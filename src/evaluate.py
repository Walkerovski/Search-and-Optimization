def evaluate(exam):
    correct = 0
    incorrect = []
    i = 0
    # check all exams that should've taken place
    for single_exam in exam:
        i += 1
        for hour_of_person in range(1, len(single_exam[0])):
            # check next time intervals for all participants
            if single_exam[0][hour_of_person] == single_exam[1][hour_of_person] == \
                single_exam[2][hour_of_person] == single_exam[3][hour_of_person] == \
                    single_exam[4][hour_of_person] == "1":
                correct += 1
                break
            # we checked all possibilities - there's no suitable case
            if hour_of_person == len(single_exam[0]) - 1:
                incorrect.append(i-1)
    return correct, incorrect
