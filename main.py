open_file = open('C:/Users/Domantas/Desktop/quizzr/sample_quiz.txt', 'r') # change to your directory
read_file = open_file.read()
quiz_file = read_file.splitlines()

numbers = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. ", "11. ", "12. ", "13. ", "14. ", "15. "]
right_answers = 0

class Question:
    def __init__(self, qumber, asnum):
        self.qumber = qumber
        self.asnum = asnum
    def quiz(self, qumber, asnum):
        global right_answers
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
            right_answers += 1
        else:
            print("Your answer is incorrect.")


questions = 5 # set to your question number

for i in range(0, questions):
    ob = Question(qumber = f"{i+1}.", asnum = i) # asnum starts from 0
    ob.qumber = f"{i+1}."  # question number i
    ob.asnum = i
    ob.quiz(ob.qumber, ob.asnum)

print(f"You correctly answered {right_answers} questions!")
'''
add more questions if you need to.
to add more questions simply copy the last line and change
qumber to your question number, and asnum to an integer 
which is qumber's number -1 (assuming all questions are in order by number)
and if you have more than 15 questions add their numbers as in the example to
the numbers list
'''

