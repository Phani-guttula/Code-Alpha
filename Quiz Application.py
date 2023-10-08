questions = ("What does CPU stand for in the context of computer hardware?",
             " Which programming language is commonly used for developing mobile apps on the Android platform?",
             "What does HTML stand for in web development?",
             " Which of the following is a popular version control system used by developers to track changes in their code?",
             "What technology is used to connect devices to the internet and enable them to communicate with each other in the Internet of Things (IoT)?")

options = (("A. Computer Processing Unit", "B. Central Processing Unit", "C. Control Processing Unit", "D. Core Processing Unit"),
           ("A. Python", "B. Swift", "C. Java", "D. C#"),
           ("A. Hyperlink Text Markup Language", "B. Hyper Text Markup Language", "C. High-Level Text Markup Language", "D. Hypermedia Text Manipulation Language"),
           ("A. Git", "B. PHP", "C. SQL", "D. CSS"),
           ("A. Bluetooth", "B. NFC", "C. Wi-Fi", "D. MQTT"))

answers = ("B", "C", "B", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D ):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(answers[question_num], " is the correct answer")
    question_num += 1