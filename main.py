open_file = open('C:/sample_quiz.txt', 'r') # change to your directory
read_file = open_file.read()
quiz_file = read_file.splitlines()

numbers = []
for i in range(1, 100):
    num = f"{i}. "
    numbers.append(num)
    
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


