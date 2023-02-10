import json
from model import Note

DATABASE_NAME = 'my_notes.json'


def write_to_database(data):
    with open(DATABASE_NAME, 'w', encoding='UTF-8') as base:
        json.dump(data, base)


def get_notes_list():
    with open(DATABASE_NAME, 'r', encoding='UTF-8') as base:
        data = json.load(base)
        return data


def create_id_number(all_notes):
    id = 0
    for note in all_notes:
        if note['id'] >= id:
            id = note['id'] + 1
    return id


def create_new_note(title, text):
    all_notes = get_notes_list()
    id = create_id_number(all_notes)
    new_note = Note(id, title, text)
    all_notes.append(new_note.__dict__)
    write_to_database(all_notes)


def update_note(id, **kwargs):
    data = get_notes_list()
    is_updated, i = False, 0
    while not is_updated and i < len(data):
        if data[i]['id'] == id:
            for key, value in kwargs.items():
                data[i][key] = value
            is_updated = True
        i += 1
    if is_updated:
        write_to_database(data)
    else:
        print(f'Запись с id = {id} не найдена')


def delete_note(id):
    data = get_notes_list()
    is_deleted, i = False, 0
    while not is_deleted and i < len(data):
        if data[i]['id'] == id:
            data.pop(i)
            is_deleted = True
        i += 1
    if is_deleted:
        write_to_database(data)
    else:
        print(f'Запись с id = {id} не найдена')



# create_new_note('test', 'Hello')
# create_new_note('Вторая заметка', 'Всем привет')
# print(get_notes_list())
# # delete_note(3)
# # print(get_notes_list())