# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer): # Verilen cevabın doğruluğunu test etme.
        return self.answer == answer

# print(q1.checkAnswer('Python'))
# print(q2.checkAnswer('C#'))
# print(q3.checkAnswer('Python'))

# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self): # Gelecek olan soru
        return self.questions[self.questionIndex]

    def displayQuestion(self): # O anki aktif soru hangisiyse liste içerisinden ilgili soruyu alıp gösteriyor.
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices: # Cevapları gösterme
            print('-'+ q)

        answer = input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer): # Cevabı tahmin etme
        question = self.getQuestion()

        if question.checkAnswer(answer): # Eğer question.checkAnswer(answer) ' dan gelen değer doğruysa
            self.score += 1 # Her bildiğin soru'da 1 ekle
        self.questionIndex += 1 # Her bildiğin soru'dan sonra bir sonraki soruyu göstermek için index numarasını 1 arttır.


    def loadQuestion(self):
        if len(self.questions) == self.questionIndex: # Eğer indexi aşmışsak bize score bilgisini göndericek.
            self.showScore()
        else: # Eğer aşmamışsak bize diğer soruyu göstericek.
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f' Question {questionNumber} of {totalQuestion} '.center(100,'*'))

q1 = Question('En iyi programlama dili hangisidir ?', ['C#', 'Python', 'Javascript', 'Java'], 'Python')
q2 = Question('En popüler dili hangisidir ?', ['C#', 'Javascript', 'Python', 'Java'], 'Python')
q3 = Question('En çok kazandıran dili hangisidir ?', ['Javascript', 'C#', 'Python', 'Java'], 'Python')
q4 = Question('En çok sevilen dili hangisidir ?', ['Javascript', 'C#', 'Python', 'Java'], 'Python')
q5 = Question('En kolay dili hangisidir ?', ['Javascript', 'C#', 'Python', 'Java'], 'Python')
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)

quiz.loadQuestion()