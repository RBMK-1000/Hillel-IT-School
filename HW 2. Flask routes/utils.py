def open_requirements():
    f = open('requirements.txt')
    return f.read()

def generate_names():
    from faker import Faker

    qty = int(input())
    names = []
    emails = []

    fake = Faker('uk_UA')
    for _ in range(qty):
        names.append(fake.name())
        emails.append(fake.ascii_email())

    result = dict(zip(names, emails))
    return result

def people_in_space():
    import requests

    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()

    quantity = f'Quantity of people in Space: {data['number']}'

    cosmonauts = []

    for person in data['people']:
        cosmonauts.append(person['name'])

    return quantity
    print(*cosmonauts, sep='\n')