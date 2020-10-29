question_prompt = [
    "What color are apples?\n(a) Red/Green\t(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\t(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\t(b) Red\n(c) Blue\n\n"
]
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

ques = [
    Question(question_prompt[0],"a"),
    Question(question_prompt[1],"c"),
    Question(question_prompt[2],"b")
]

def run_test(questions):
    score =0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got"+str(score)+"/"+str(len(questions)))
run_test(ques)