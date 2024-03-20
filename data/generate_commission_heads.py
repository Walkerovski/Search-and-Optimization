from random import randint
number_of_people = 6
number_of_days = 5
number_of_hours = 6

whole_week = []
for i in range(number_of_people):
    head_week = []
    selected_day = randint(0, number_of_days-1)
    print(selected_day)
    for x in range(number_of_hours):
        for j in range(number_of_days):
            head_day = []
            if (j == selected_day):
                for _ in range(number_of_hours):
                    if (_ == x):
                        head_day.append(1)
                        # head_week.append(1)
                    else:
                        # head_week.append(0)
                        head_day.append(0)
            else:
                for _ in range(number_of_hours):
                    # head_week.append(0)
                    head_day.append(0)
            head_week.append(head_day)
        whole_week.append(head_week)

for person_data in whole_week:
    for hour in person_data:
        print(hour,  ",", end='', sep='')
    print()
