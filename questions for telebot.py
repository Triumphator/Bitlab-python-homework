import json


class QuizQuestion:
    def __init__(self, question="", answers=None, correct_answer=""):
        if answers is None:
            answers = []
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.correct_answer_position = self.__get_correct_answer_position__()

    def __get_correct_answer_position__(self):
        id = -1
        i = 0
        if self.correct_answer.lower() in self.answers:
            for answer in self.answers:
                if answer.lower() == self.correct_answer.lower():
                    id = i
                    break
                i = i + 1
            return id

    def __str__(self):
        return f"question:{self.question} answers:{self.answers} correct_answer:{self.correct_answer} correct_answer_position:{self.correct_answer_position} "


class Main:

    def getQuestionsList():
        file = open('user.json', 'r')
        text = json.load(file)
        file.close()
        for key, value in text.items():
            print(key, ':', value)

    def saveQuestion(quiz):
        file = open('user.json', 'r')
        dict = json.load(file)
        file.close()
        count = -1
        for row in dict:
            count += 1
        file2 = open('user.json', 'w')
        dictQuiz = {"question" : quiz.question, "answers" : quiz.answers, "correct answer" : quiz.correct_answer, "correct_answer_position" : ???}
        dict["q" + str(count+1)] = dictQuiz

        json.dump(dict, file2)
        file2.close()


    while True:


        choice = int(input(""" 
    PRESS [1] TO ADD QUESTION
    PRESS [2] TO LIST QUESTIONS
    PRESS [3] TO EXIT\n"""))

        if 0 <= choice <= 3:
            if choice == 1:
               #try:
                question = input("Enter new question: ")
                answers = input("Enter answers, separated by comma: ").split(",")
                answers_list = []
                correct_answer = input("Enter password: ")
                quiz = QuizQuestion(question, answers, correct_answer, correct_answer_position)
                saveQuestion(quiz)
                continue

            elif choice == 2:
                getQuestionsList()
                continue
            else:
                print("Exiting")
                break
