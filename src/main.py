from read_from_file import read_from_file
from next_generation import generate_next_population
from evaluate import evaluate
from tournament import duel
from hours import hours


def print_result(exam):
    id = 0
    for single_exam in exam:
        id += 1
        for hour_of_person in range(1, len(single_exam[0])):
            if single_exam[0][hour_of_person] == single_exam[1][hour_of_person] == \
                single_exam[2][hour_of_person] == single_exam[3][hour_of_person] == \
                    single_exam[4][hour_of_person] == "1":
                print(f'\nEGZAMIN NR {id}, godz {hours[hour_of_person-1]}')
                print("Uczestnicy:")
                print(f'Student: {single_exam[0][0]}')
                print(f'Recenzent: {single_exam[1][0]}')
                print(f'Opiekun: {single_exam[2][0]}')
                print(f'Przewodniczący: {single_exam[3][0]}')
                print(f'Członek komisji: {single_exam[4][0]}')


def genetic_algorithm(probability_tournament, probability_hybrid, max_iter_to_shuffle, iter_of_shuffle):
    students, reviewers, patrons, commission_heads, commission_participants = read_from_file()

    exam = []
    for student_index in range(0, len(students)):
        exam.append([students[student_index], reviewers[student_index], patrons[student_index],
                    commission_heads[student_index], commission_participants[student_index]])

    timer = 0
    while (True):
        exam = generate_next_population(exam, probability_hybrid)
        correct, incorrect = evaluate(exam)
        # Schedule was found, we can exit program
        if correct == len(exam):
            break
        # Make tournament selection between incorrect cases
        exam = duel(exam, incorrect, probability_tournament)
        # If algorithm (exploitation) is working too long, it means exploration needs to be prioritised
        timer += 1
        if timer == max_iter_to_shuffle:
            timer = 0
            shuffle = iter_of_shuffle
            while (shuffle > 0):
                exam = generate_next_population(exam, 0.5)
                shuffle -= 1

    print_result(exam)


def main():
    print("Układanie planu egzeminów...")
    probability_tournament = 0.9
    probability_hybrid = 0.0005
    max_iter_to_shuffle = 80000
    iter_of_shuffle = 5000
    genetic_algorithm(probability_tournament=probability_tournament, probability_hybrid=probability_hybrid,
                      max_iter_to_shuffle=max_iter_to_shuffle, iter_of_shuffle=iter_of_shuffle)


if (__name__ == "__main__"):
    main()
