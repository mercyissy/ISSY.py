num_users = int(input('How many users are taking the Test: '))
allstudents = []
studentscores = []
for user in range(num_users):
    # Collecting student name
    students = input(f'Name of Student {user + 1}: ') 
    allstudents.append(students)

# def welcome_message():
#     print("Instruction: Choose the correct answer for the following question.")

def get_questions():
    Question =[
    '1. What is the capital of Nigeria  a). Lagos b). Abuja',
    '2. What is the name of Osun State Governor? a.) Governor Adeleke b). Governor Bello',
    '3. What is the capital of Osogbo  a). Lagos b). Osun',
    '4. Who is the founder of SQI  a). Adeyemi Aderinto b). Abiodun Gbenga',
    '5. What year was SQI founded  a). 2002 b). 2008'
    ]
    Answer = [
    'b',
    'a',
    'b',
    'a',
    'b'
    ]

    for student in allstudents:
        score = 0
        print(f'{student}, Answer the following questions')
        for question, ans in zip(Question, Answer):
            print(question)
            Answer = input('Answer: ')

            if Answer.lower() == ans:
                print('correct')
            else:
                print('wrong')

    
get_questions()


