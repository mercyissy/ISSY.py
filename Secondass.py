allstudents =[]

studentscores = []

questions = [
    ('1. What is the capital of Nigeria  a). Lagos b). Abuja'),
    ('2. What is the name of Osun State Governor? a.) Governor Adeleke b). Governor Bello'),
    ('3. What is the capital of Osogbo  a). Lagos b). Osun'),
    ('4. Who is the founder of SQI  a). Adeyemi Aderinto b). Abiodun Gbenga'),
    ('5. What year was SQI founded  a). 2002 b). 2008')
]
answers = [
    'b',
    'a',
    'b',
    'a',
    'b'
]

num_users = int(input('How many users are taking the Test: '))
# Loop through for each student
for user in range(num_users):
    
    # Collecting student name
    students = input(f'Name of Student {user + 1}: ') 
    allstudents.append(students)
   
for students in allstudents:
    print(f'{students}, Answer the following Questions Correctly:')
    scores = 0
    for question, answer in zip(questions, answers):
        print(question)
        user_answer = input('Answer: ')
        if user_answer.lower() == answer:
            print('correct')
            scores += 5
        else:
            print('wrong')   
    studentscores.append(scores)

 # Display the final score for the current student
for student, score in zip(allstudents, studentscores):
    print(f'{student} scored {score}')

    #  separation under each students 
    print('-' * 50)

# End of the test
print('Test complete for all students.')


# for i in range(num_users):
#     print(f'{allstudents[i]} => {studentscores[i]}')
    

sum_score = max(studentscores)
index_max = studentscores.index(max(studentscores))
print(allstudents[index_max])

sum_score = min(studentscores)
index_max = studentscores.index(min(studentscores))
print(allstudents[index_max])

length = len(studentscores)
mean_score = sum_score/length  
print('Average score is', mean_score)