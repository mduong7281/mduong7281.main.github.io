import random

#avoid crash when user enter strage input
def valid_input(prompt):
    got_valid_input = False
    while got_valid_input == False:
        try:
            answer = int(input(prompt))
            got_valid_input = True
        except ValueError:
            print("Invalid input, try again!")
    return answer


# def attempt():
#     attempts = 0
#     question: int
#     while attempts < 3:
#         answer = valid_input("Enter your answer")
#         if answer == question:
#             print("good!")
#         else:
#             print('try again.')
#             attempts += 1
#     return answer

number_students_test = valid_input("Enter number student taking test: ")
for test in range(number_students_test):


    # Main program run
    def main():
        score = 0
        time_program_start = 0
        start = True
        while start:
            num1 = random.randint(10, 20)
            num2 = random.randint(1, 9)
            print("what do you to practice? ")
            print("1. Summation")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. I don't want to do any math now!")
            user_input = valid_input("Enter your choice: ")
            if user_input == 1:
                # 1 Plus question
                print("what is: ", num1, "+", num2)
                question = num1 + num2
                answer = valid_input("Enter your answer: ")
                while answer != question:
                    print("Try again!")
                    score -= 1
                    time_program_start += 1
                    answer = valid_input("Enter your answer: ")
                else:
                    score += 1
                    time_program_start += 1
                    print("Good!")
            elif user_input == 2:
                # 2 subtraction question
                print("what is: ", num1, "-", num2)
                question = num1 - num2
                answer = valid_input("Enter your answer: ")
                while answer != question:
                    print("Try again!")
                    score -= 1
                    time_program_start += 1
                    answer = valid_input("Enter your answer: ")
                else:
                    score += 1
                    time_program_start += 1
                    print("Good!")
            elif user_input == 3:
                # 3 multiplication question
                print("what is: ", num1, "*", num2)
                question = num1 * num2
                answer = valid_input("Enter your answer: ")
                while answer != question:
                    print("Try again!")
                    score -= 1
                    time_program_start += 1
                    answer = valid_input("Enter your answer: ")
                else:
                    score += 1
                    time_program_start += 1
                    print("Good!")
            elif user_input == 4:
                # 4 divide question
                print("what is: ", num1, "/", num2)
                question = round(num1 / num2)
                answer = valid_input("Enter your answer: ")
                while answer != question:
                    print("Try again!")
                    score -= 1
                    time_program_start += 1
                    answer = valid_input("Enter your answer: ")
                else:
                    score += 1
                    time_program_start += 1
                    print("Good!")
            elif user_input == 5:
                start = False
        return [score, time_program_start]


    a, b = main()

#find the average score
    def average(a, b):
        score = a
        loops = b
        avg = (score / loops) * 10
        return avg

#find the scale
    def scale():
        if average(a, b) > 9:
            status = str("Excellent")
        elif (average(a, b) <= 9) and (average(a, b) >= 8):
            status = str("Good")
        elif (average(a, b) < 8) and (average(a, b) >= 7):
            status = str("Accepted")
        else:
            status = str("Fail")
        return status

#tell user what are they get.
    def plan():
        if (average(a, b) > 9) or (average(a, b) >= 7):
            print("Congratulation!")
        elif not (average(a, b) > 9) or (average(a, b) >= 7):
            print("Hope you doing better next time!")

#sotre user's information and score
    def info():
        last_name = input("Enter your last name: ")
        first_name = input("Enter your first name: ")
        student_score = a

        in_file = open("studentInfo.txt", 'a')
        in_file.write("Name: " + first_name + " " + last_name)
        in_file.write("\nYour score:" + str(student_score) + "/ " + str(b))
        in_file.write("\n")
        in_file.write(scale())
        in_file.write("\n")
        in_file.close()
        print("Data is saved in file: studentInfo.txt")
        print("Open file to see score!")


    plan()
    info()
# https://note.nkmk.me/en/python-function-return-multiple-values/
