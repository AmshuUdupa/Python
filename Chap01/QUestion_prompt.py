from Questions import Question

Question_prompt =[
    "What color are Oranges\na)Red\nb)Orange\nc)Black\n\n",
    "What color are Apples\na)Red\nb)Orange\nc)Green\n\n",
    "What color are Bananas\na)Red\nb)Orange\nc)Yellow\n\n"
]


Questions = [
    Question(Question_prompt[0],"b"),
    Question(Question_prompt[1],"a"),
    Question(Question_prompt[2],"c")
]

def run_test(Questions):
    score  = 0
    for question in Questions:
        answer =  input(print(question.prompt))

        if answer == question.answer:
            score = score +1

    print("You have got "+str(score)+" out of "+str(len(Questions)))

run_test(Questions)