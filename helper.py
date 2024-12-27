from faker import Faker
import random as r

faker = Faker("ru_RU")


def generate_registration():
    name = faker.first_name()
    last_name = faker.last_name()
    address = 'Химки, ул. Заречная, д.5'
    phone_number = generate_number()

    return name, last_name, address, phone_number


def generate_number():
    country_code = '+7'
    operator_code = r.randint(100, 999)
    last_digits = r.randint(100000, 999999)

    number = country_code + str(operator_code) + str(last_digits)
    return number
