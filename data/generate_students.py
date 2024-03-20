from random import random
student_time_list = []
probability = 0.86
number_of_people = 30
number_of_intervals = 30

for _ in range(number_of_people):
    student_time_list = []
    for _ in range(number_of_intervals):
        data_to_append = 0
        if(random() < probability):
            data_to_append = 1
        if(sum(student_time_list) > 26):
            data_to_append = 1
        student_time_list.append(data_to_append)
        
    for number in student_time_list:
        print(number,  ",", end='', sep='')
    print()