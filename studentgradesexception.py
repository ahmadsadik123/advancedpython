import csv


class StudentFailException(ValueError):
    pass


def grader(a):
    if a < 70:
        raise StudentFailException


with open("student_grades.csv") as csv_file:
    csv_reader = csv.reader(csv_file)

    while True:
        for row in csv_reader:
            try:
                average = (int(row[1]) + int(row[2]) + int(row[3]) + int(row[4])) / 4
                print(f"{row[0]}'s average grade is {average}")

                if average < 70:
                    print("Student has failed")
                    raise StudentFailException
                else:
                    print("Student has passed")

            except:
                pass
        else:
            break
