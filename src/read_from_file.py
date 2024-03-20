import csv


def read_from_file():
    file = open("./mockdata/students.csv", "r")
    students = list(csv.reader(file, delimiter=","))
    file.close()

    file = open("./mockdata/reviewers.csv", "r")
    reviewers = list(csv.reader(file, delimiter=","))
    file.close()

    file = open("./mockdata/patrons.csv", "r")
    patrons = list(csv.reader(file, delimiter=","))
    file.close()

    file = open("./mockdata/commission_heads.csv", "r")
    commission_heads = list(csv.reader(file, delimiter=","))
    file.close()

    file = open("./mockdata/commission_participants.csv", "r")
    commission_participants = list(csv.reader(file, delimiter=","))
    file.close()

    return (students, reviewers, patrons, commission_heads, commission_participants)
