class Contact:

    def __init__(self, name, surname, phone_number,
                 chosen_contact = False, *args, **kwargs):

        self.name = name,
        self.surname = surname,
        self.phone_number = phone_number,
        self.chosen_contact = chosen_contact
        self.other = dict(**kwargs)
        if not self.chosen_contact:
            self.chosen_contact = 'нет'

    def __str__(self):

        return ('Имя: %s\nФамилия: %s \nТелефон: %s \nВ избранных: %s \nДополнительная информация: \n%s' \
                % (self.name[0], self.surname[0], self.phone_number[0], self.chosen_contact, '\n'.join(self.get_other_info())))

    def get_other_info(self):

        items_list = []

        for key, value in self.other.items():
            items_list.append(f'{key}: {value}')

        return items_list   

class Phonebook:

    def __init__(self, name):

        self.name = name
        self.contacts_list = []

    def __str__(self):

        some_list = []

        for item in self.contacts_list:
            some_list.append(str(item))

        return ('\nКонтакты:\n \n%s') % ('\n\n'.join(some_list))    

    def add_contact(self, contact):

        self.contacts_list.append(contact)
        
    def del_contact(self, info):

        for item in self.contacts_list:
            if info in item.phone_number:
                self.contacts_list.remove(item)

    def find_chosen_contacts(self):

        chosen_contacts_list = []

        for item in self.contacts_list:
            if item.chosen_contact == 'нет':
                pass
            else:
                chosen_contacts_list.append(item)
                
        print('Избранные контакты:\n')
        
        start = 0
        end = len(chosen_contacts_list)
        
        while start < end:
            yield print(chosen_contacts_list[start], end='\n\n')
            start += 1

    def search_contact(self, name, surname):

        for item in self.contacts_list:
            if name == item.name[0] and surname == item.surname[0]:
                print(f'Найден контакт:\n\n{item}')


if __name__ == '__main__':
   
    user_1 = Contact('Ruslan', 'Sibgatullin', '+7982111111', 'кот', email = 'rus21@yandex.ru', vk = 'id123321123321123', telegram = '@Rus')
    user_2 = Contact('Иван', 'Иванов', '+7982222222', email = 'ivanivanov22@mail.ru', telegram = '@Ivanivanov22')
    user_3 = Contact('Сергей', 'Степанов', '+7983333333', 'есть', email = 'stepanov33@mail.ru', telegram = '@Stepanov33')
    user_4 = Contact('Андрей', 'Иванов', '+7984444444', 'есть', email = 'ivanov44@mail.ru', telegram = '@Ivanov44')
    phone_book = Phonebook('PHB')
    phone_book.add_contact(user_1)
    phone_book.add_contact(user_2)
    phone_book.add_contact(user_3)
    phone_book.add_contact(user_4)
    print(phone_book)
    phone_book.contacts_list
    phone_book.del_contact('+7982111111')
    print(phone_book, end='\n\n')
    [item for item in phone_book.find_chosen_contacts()]
    phone_book.search_contact('Сергей', 'Степанов')