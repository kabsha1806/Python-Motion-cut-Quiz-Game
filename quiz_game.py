class Quiz:
    def _init_(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        while True:
            user_input = input("Enter the number of your answer: ")
            if user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(self.questions[0]['options']):
                    return user_choice
            print("Invalid input. Please enter a valid option number.")

    def check_answer(self, question, user_answer):
        correct_answer_index = question['options'].index(question['answer']) + 1
        if user_answer == correct_answer_index:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect! The correct answer is:", question['answer'])
        print()

    def run_quiz(self):
        print("Welcome to the Quiz Game!\n")
        for idx, question in enumerate(self.questions, start=1):
            print(f"Question {idx}:")
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)

        print("Quiz completed!")
        print(f"Your final score is: {self.score}/{len(self.questions)}")


questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Mercury'],
        'answer': 'Mars'
    },
    {
        'question': 'Who wrote "Romeo and Juliet"?',
        'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'Mark Twain'],
        'answer': 'William Shakespeare'
    }
]


quiz = Quiz(questions)
quiz.run_quiz()
