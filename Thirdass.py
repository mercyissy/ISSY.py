all_todo = []

def dashboard():
    print(
        '''
        Welcome to myTODO App

        1. Add a todo
        2. Edit a todo
        3. Delete a todo
        4. View todo
        5. Exit

        '''
    )

    option = input('Option: ')
    if option == '1':
        createTodo()
    elif option == '4':
        viewTodo()
    elif option == '2':
        editTodo()
    elif option == '3':
        deleteTodo()
    elif option == '5':
        print("Exiting the To-Do App.")
        exit()
    else:
        print('Error')
        dashboard()

    
def createTodo():
    while True:
        todo = input('Todo: ')
        all_todo.append(todo)
        option = input('Press 1 to stop or enter to continue adding todo: ')
        if option == '1':
            viewTodo()
        else:
            continue


def viewTodo():
    print(f'\nMy TODO List: {all_todo}\n')
    if len(all_todo) > 0:
        x = 1
        for todo in all_todo:
            print(f'{x}.{todo}')
            x += 1
    else:
        print('No_Todo')
    dashboard()

def deleteTodo():
    print(all_todo)
    delete = int(input('Enter a number of Todo to delete: '))
    if delete < 1  and delete > len(all_todo):
        print('Invalid number, Try Again')
        viewTodo()

    else:
        all_todo.pop(delete-1)
        viewTodo()
        

def editTodo():
    print(all_todo)
    rem = int(input('Enter a number of Todo to edit: '))
    if rem < 1  and rem > len(all_todo):
        print('invlaid task number')
    else:
        new_todo = input(f'Enter new Todo: {all_todo[rem-1]}: ')
        all_todo[rem-1] = new_todo
        print(f'{rem} Updated Successfully!')
        viewTodo()
    

      

dashboard()

# To display my todo with numbers 
all_todo = []
x = 1

for todo in all_todo:
    print(f'{x}.{todo}')
    x += 1