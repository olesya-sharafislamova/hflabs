# -*- coding: utf-8 -*-

import string
import random



def test_create_appeal(app):
    app.open_appeal_page()
    app.appeal.fill_username(fullname=random_string("firstname", 5), name=random_string("firstname", 5),
                             secondname=random_string("firstname", 5))
    app.appeal.fill_phone(phone=random_string_for_phone("+495", 7))
    app.appeal.fill_email(email=random_string_for_email("mail", 7))
    app.appeal.fill_message(random_string_message("message", 100))
    app.appeal.fill_address()
    app.appeal.send_message()


# генерация случайного номера телефона
def random_string_for_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# генерация случайных данных
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# генерация случайного email
def random_string_for_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])+ "@ya.ru"

# генерация случайного сообщения
def random_string_message(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

