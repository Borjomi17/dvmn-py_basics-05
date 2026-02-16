from os import remove
import file_operations
from faker import Faker
import random


def main():
    for i in range(10):
        fake = Faker('ru_RU')
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        strength = random.randint(3,18)
        agility = random.randint(3,18)
        endurance = random.randint(3,18)
        intelligence = random.randint(3,18)
        luck = random.randint(3,18)
        skills = ["Стремительный прыжок","Электрический выстрел", "Ледяной удар", "Стремительный удар",
        "Кислотный взгляд","Тайный побег", "Ледяной выстрел", "Огненный заряд"]
        rename_skills = []
        letters_mapping = {
            'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
            'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
            'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
            'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
            'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
            'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
            'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
            'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
            'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
            'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
            'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
            'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
            'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
            'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
            'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
            'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
            'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
            'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
            'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
            'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
            'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
            'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
            ' ': ' '
        }
        for skill in skills:
            for letter, letter_1 in letters_mapping.items():
                skill = skill.replace(letter,letter_1)
            rename_skills.append(skill)
        new_skill = random.sample(rename_skills,3)
        skill_1 = new_skill[0]
        skill_2 = new_skill[1]
        skill_3 = new_skill[2]
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job,
            "town": town,
            "strength": strength,
            "agility": agility,
            "endurance": endurance,
            "intelligence": intelligence,
            "luck": luck,
            "skill_1": skill_1,
            "skill_2": skill_2,
            "skill_3": skill_3
        }
        file_operations.render_template('charsheet.svg','svg/result_{}.svg'.format(i),context)


if __name__ == '__main__':
    main()