def start():
    """Program entry point."""
    fileName = 'task_38_Phonebook.txt'
    menuItem = ShowMenu()
    phoneBook = GetPhonebook(fileName)

    while(True):
        if menuItem == 1:
            # 1. Вывод всех абонентов
            PrintAll(phoneBook)
        elif menuItem == 2:
            #2. Поиск абонента по имени
            name = GetName()
            PrintRecord(GetByName(phoneBook, name))
        elif menuItem == 3:
            # 3. Поиск абонента по номеру телефона
            phone = GetPhone()
            PrintRecord(GetByPhone(phoneBook, phone))
        elif menuItem == 4:
            # 4. Добавление нового абонента
            record = GetNewRecord()
            AddRecord(phoneBook, record)
            SavePhonebook(fileName, phoneBook)
        elif menuItem == 5:
            # 5. Удалить абонента
            phone = GetPhone()
            DeletRecord(phoneBook, phone)
            SavePhonebook(fileName, phoneBook)
        elif menuItem == 6:
            # 6. Изменить имя абонента
            phone = GetPhone()
            ChangeName(phoneBook, phone)
            SavePhonebook(fileName, phoneBook)
        menuItem = ShowMenu()

def GetPhonebook(filename: str) -> list:
    """Get Phonebook data from a file."""
    db = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Примечание']
    with open(filename, mode = 'r', encoding = 'utf-8') as fileToRead:
        for line in fileToRead:
            record = dict(zip(fields, line.split(',')))
            db.append(record)
    return db

def SavePhonebook(filename: str, data: list):
    """Save Phonebook data to a file."""
    with open(filename, mode = 'w', encoding = 'utf-8') as fileToWrite:
        for recordIndex in range(len(data)):
            record = ''
            for item in data[recordIndex].values():
                record += item + ','
            fileToWrite.write(f'{record[:-1]}')

def PrintAll(phoneBook):
    """Print all recorords from Phonebook."""
    for record in phoneBook:
        for key in record:
            print(f'{key}: {record[key]}', end=" ")

def GetName():
    """Get name to search."""
    return(input('Введите имя: '))

def GetByName(phoneBook, name):
    """Get record in Phonebook by Name."""
    for record in phoneBook:
        if record['Имя'] == name:
            return record

def PrintRecord(record):
    """Print one record from Phonebook."""
    for key in record:
        print(f'{key}: {record[key]}', end=" ")

def GetPhone():
    """Get phone to search."""
    return(input('Введите номер телефона: '))

def GetByPhone(phonebook, phone):
    """Get record in Phonebook by phone."""
    for record in phonebook:
        if record['Телефон'] == phone:
            return record

def GetNewRecord():
    """Make record from user input."""
    userInput = input('Введите через запятую Фамилию, Имя, Телефон, Примечание: ')
    fields = ['Фамилия', 'Имя', 'Телефон', 'Примечание']
    return dict(zip(fields, userInput.split(',')))

def AddRecord(phoneBook, record):
    phoneBook.append(record)

def DeletRecord(phonebook, phone):
    """Delete record by phone"""
    for record in phonebook:
        if record['Телефон'] == phone:
            phonebook.pop(phonebook.index(record))

def ChangeName(phoneBook, phone):
    """Change name in f record."""
    newName = input('Введите новое имя абонента: ')
    for record in phoneBook:
        if record['Телефон'] == phone:
            record['Имя'] = newName

def ShowMenu() -> int:
    """Get user choice from menu."""
    print('\nМЕНЮ:')
    print('1. Вывод всех абонентов')
    print('2. Поиск абонента по имени')
    print('3. Поиск абонента по номеру телефона')
    print('4. Добавление нового абонента')
    print('5. Удалить абонента')
    print('6. Изменить имя абонента')
    return int(input('Введите пункт меню: '))

start()