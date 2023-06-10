import random
from faker import Faker
from data.data import Person

faker_en = Faker('En')


def generate_fake_password(length):
    password = faker_en.password(length)
    return password


def generated_person():
    return Person(
        name=faker_en.first_name(),
        email=faker_en.email(),
        password=faker_en.password(),
        incorrect_password=generate_fake_password(5)

    )


def generate_file():
    path = rf'/Users/verakhatskevich/Desktop/autotests/project/Sprint3/{random.randint(10, 100)}.txt'
    file = open(path, 'w')
    file.write(f'GenetatedFile{random.randint(23, 100)}')
    file.close()
    return path
