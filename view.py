
COMMANDS_LIST = {
    '1': 'Создать новую заметку',
    '2': 'Посмотреть все заметки',
    '3': 'Посмотреть все заметки за выбранную дату',
    '4': 'Найти конкретную заметку',
    '5': 'Редактировать заметку',
    '6': 'Удалить заметку',
    '0': 'Выход',
}

def greeting():
    print('Добро пожаловать в записную книжку!\n')

def goodbye():
    print('Будем рады увидеть вас снова!')

def menu():
    print('Выберите команду и нажмите соответствующую цифру:')
    for key, value in COMMANDS_LIST.items():
        print(f'{key} - {value}')
    while True:
        choice = input('Введите номер команды: ')
        if choice in COMMANDS_LIST:
            print(f'Вы выбрали команду "{COMMANDS_LIST[choice]}"')
            return choice
        else:
            print('Команда не распознана. Попробуйте еще раз')

def get_note_id():
    while True:
        id = input('Введите id-номер заметки: ')
        try:
            return int(id)
        except:
            print(f'Введенное значение {id} не является числом. Попробуйте еще раз')

def get_note_id():
    while True:
        id = input('Введите id-номер заметки: ')
        try:
            return int(id)
        except:
            print(f'Введенное значение {id} не является числом. Попробуйте еще раз')

