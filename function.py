import operations
import notepad
import ui

number = 6


def add():
    note = ui.create_note(number)
    array = operations.read_file()
    for notes in array:
        if notepad.Note.get_id(note) == notepad.Note.get_id(notes):
            notepad.Note.set_id(note)
    array.append(note)
    operations.write_file(array, 'a')
    print('Заметка добавлена')


def show(text):
    logic = True
    array = operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(notepad.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + notepad.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in notepad.Note.get_date(notes):
                print(notepad.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = operations.read_file()
    logic = True
    for notes in array:
        if id == notepad.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                notepad.Note.set_title(notes, note.get_title())
                notepad.Note.set_body(notes, note.get_body())
                notepad.Note.set_date(notes)
                print('Заметка изменена')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена')
            if text == 'show':
                print(notepad.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет')
    operations.write_file(array, 'a')