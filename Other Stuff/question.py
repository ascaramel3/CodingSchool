questions=[]
answers=[]
 
print("-Create Your Own Quiz v.1.0-\nBy Aidan Singer\n")
 
question_number=input("How many questions do you want in the quiz? (At least 1.)")
 
#Easter egg/message
while question_number=="pneumonoultramicroscopicsilicovolcanoconiosis":
    print("QwQ")
if question_number=="m3ssag3":
    print("hi so i like dis program but idk its not that good if im being honest it could prob be opt but im lazy :P (btw this causes 3RR0R)")
 
def question_and_answers():
    for i in range(int(question_number)):
        question_query=input("Input a question:")
        answers_query=input("Now input an answer to this question:")
        questions.append(question_query)
        answers.append(answers_query)
question_and_answers()
 
print("Now have another person answer these questions!\n\n\n\n\n")
 
def ask_questions(index):
    global score
    score=0
    for i in range(0,len(questions)):
        ask=input(questions[index])
        if ask==answers[index]:
            print("Correct! ^^\n")
            score+=1
        else:
            print("Incorrect! >:P\n")
        index+=1
 
ask_questions(0)
 
print(f"You have completed the quiz! Your score is {score} out of {len(questions)}.")
# Finished 8-2-2025.