import csv
import os
def valid_menu(to_do):
    if to_do.isdigit() and int(to_do) in (1,2,3,4,5):
        return True
    else: return False
def valid_digit(number):
    if number.isdigit():
        return True
    else:
        return False


def open_file():
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        lists_of_contacts = []
        for row in reader:
            contact = {}
            contact["name"] = row[0]
            contact["number"] = row[1]
            contact["email"] = row[2]
            lists_of_contacts.append(contact)
        return lists_of_contacts
def clear_console():
    os.system('cls||clear')

def show_contacts(lists_of_contacts):
    for item in lists_of_contacts:
        print(f'{item['name']:<30}{item['number']:<20}{item['email']:<20} ')
def string_to_continue ():
    print(input("Нажмите ENTER для продолжения..."))
def create_contact(lists_of_contacts):
    new_contact = {}
    name = input("Введите имя:")
    new_contact["name"] = name
    attempt = 1
    while attempt < 6:
        number = input("Введите телефон:")
        attempt = attempt + 1
        if number.isdigit():
            new_contact["number"] = number
            break
        else:
            continue
    if attempt == 5:
        print("Исчерпано кол-во попыток ввода.")
        string_to_continue()
        return
    email = input("Введите почту:")
    new_contact["email"] = email
    lists_of_contacts.append(new_contact)
    print("Контакт создан")

def find_contact(lists_of_contacts):
    contact_to_find  =  input("Введите имя или телефон для поиска контакта ")
    for item in lists_of_contacts:
        if item['name'] == contact_to_find or item['number'] == contact_to_find:
            print(f'{item['name']:<30}{item['number']:<20}{item['email']:<20} ')
            return
    print(f"Контакт {contact_to_find} не найден")
    return

def delete_contact(lists_of_contacts):
    contact_to_delete = input("Введите имя для удаления контакта ")
    for item in lists_of_contacts:
        if item['name'] == contact_to_delete:
            lists_of_contacts.remove(item)
            print(f"Контакт {contact_to_delete} удален.")
            return
    print(f"Контакт {contact_to_delete} не найден")
    return

def save_file(lists_of_contacts):
    with open('data.csv', 'w', encoding='utf-8', newline ='') as file:
        writer  = csv.writer(file)
        for item in lists_of_contacts:
            string_data = list(item.values())
            writer.writerow(string_data)

def main_func():
    lists_of_contacts = open_file()
    while 1 == 1:
        clear_console()
        print("МЕНЮ")
        print("1. Показать все контакты")
        print("2. Создать контакт")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Выход контакт")
        to_do = input("Введите пункт меню: ")
        if (valid_menu(to_do)):
            match int(to_do):
                case 1:
                    clear_console()
                    show_contacts(lists_of_contacts)
                    print('\n')
                    string_to_continue()
                case 2:
                    clear_console()
                    create_contact(lists_of_contacts)
                    save_file(lists_of_contacts)
                    print('\n')
                    string_to_continue()
                case 3:
                    clear_console()
                    find_contact(lists_of_contacts)
                    print('\n')
                    string_to_continue()
                case 4:
                    clear_console()
                    delete_contact(lists_of_contacts)
                    save_file(lists_of_contacts)
                    print('\n')
                    string_to_continue()
                case 5:
                    break
        else:
            print("\nВведен неверный пункт меню. ")
            string_to_continue()

main_func()