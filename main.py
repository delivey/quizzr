open_file = open('D:/Quizzes/sample_quiz.txt', 'r') # change to your directory
read_file = open_file.read()
quiz_file = read_file.splitlines()

numbers = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. ", "11. ", "12. ", "13. ", "14. ", "15. "]

class Question:
    def __init__(self, qumber, asnum):
        self.qumber = qumber
        self.asnum = asnum
    def quiz(self, qumber, asnum):
        questions = []
        real_answers = []
        for line in quiz_file:
            for i in numbers:
                if line.startswith(i):
                    questions.append(line)
            if "R" in line:
                real_answers.append(line)
            if line.startswith(qumber):
                new_line = line.replace("R", "")
                print(new_line)
        answer = input("What's your answer: \n")

        one_answer = str(real_answers[asnum])
        fixed_answer = one_answer.replace("['", "")
        digit = 3
        if len(answer) >= 4:
            digit += 1
        right_answer = fixed_answer[:digit]
        if answer == right_answer:
            print("Your answer is correct!")
        else:
            print("Your answer is incorrect.")

ob = Question(qumber = "1.", asnum = 0) # asnum starts from 0
ob.qumber = "1."  # question number 1
ob.asnum = 0
ob.quiz(ob.qumber, ob.asnum)

ob = Question(qumber = "2.", asnum = 1) # asnum starts from 0
ob.qumber = "2."  # question number 2
ob.asnum = 1
ob.quiz(ob.qumber, ob.asnum)

ob = Question(qumber = "3.", asnum = 2) # asnum starts from 0
ob.qumber = "3."  # question number 3
ob.asnum = 2
ob.quiz(ob.qumber, ob.asnum)

ob = Question(qumber = "4.", asnum = 3) # asnum starts from 0
ob.qumber = "4."  # question number 4
ob.asnum = 3
ob.quiz(ob.qumber, ob.asnum)

ob = Question(qumber = "5.", asnum = 4) # asnum starts from 0
ob.qumber = "5."  # question number 5
ob.asnum = 4
ob.quiz(ob.qumber, ob.asnum)

'''
add more questions if you need to.
to add more questions simply copy the last line and change
qumber to your question number, and asnum to an integer 
which is qumber's number -1 (assuming all questions are in order by number)
and if you have more than 15 questions add their numbers as in the example to
the numbers list
'''

