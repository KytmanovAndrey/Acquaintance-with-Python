from data_create import *


def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'


def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')


def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()


def print_contacts():
    data = read_file()
    print()
    print(data)


def search_contact():
    print('Варианты поиска:\n'
          '1. По имени\n'
          '2. По фамилии\n'
          '3. По отчеству\n'
          '4. По номеру телефона\n'
          '5. По адресу')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Такого нету')
    else:
        data_lst = data_str.split('\n\n')
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                print()
                print(contact_str)

def change_contact():
    print('Введите полную запись для однозначной идентификации контакта, который хотите изменить.')
    contact = input_contact()
    data = read_file()
    if contact in data:
        print("Введите новую запись: ")
        new_contact = input_contact()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)
    else:
        print("нет такой записи")


def delete_contact():
    print('Введите полную запись для однозначной идентификации контакта, который хотите удалить.')
    contact = input_contact()
    data = read_file()
    if contact in data:
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact + "\n\n", '')
            data2.write(data)
    else:
        print("нет такой записи")
