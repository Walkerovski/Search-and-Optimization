from random import randint
number_of_people = 31
number_of_days = 5
number_of_hours = 6

whole_week = []
for _ in range(number_of_people):
    days = []
    hours = []
    for j in range(number_of_days):
        free_hours = []
        while (len(free_hours) < 2):
            random_number = randint(0, 5)
            if (not random_number in free_hours):
                free_hours.append(random_number)
        for _ in range(number_of_hours):
            hours.append(0)
        for i in range(len(hours), ):
            if (i in free_hours):
                hours[i] = 1
        days.append(hours)
        hours = []
    whole_week.append(days)

for person_data in whole_week:
    for day in person_data:
        for hour in day:
            print(hour,  ",", end='', sep='')
    print()
