from src.headhunter_api import HeadHunterAPI
from src.utils import create_database, save_data_to_database
from config import config
import psycopg2
from src.db_manager import DBManager


def main():
    vacancies_json = []
    data = []
    user_employee = [
        ['80', 'Альфа-Банк'],
        ['370', 'АльфаСтрахование'],
        ['402', 'Компания ТрансТелеКом'],
        ['733', 'ЛАНИТ'],
        ['882', '1С'],
        ['2523', 'М.Видео-Эльдорадо'],
        ['407', 'Гарант'],
        ['490', 'Ренессанс cтрахование, Группа'],
        ['2748', 'Ростелеком'],
        ['2808', 'Открытые Технологии']
    ]

    start_question_database_ini = input(
        f'\n!!! Убедитесь в наличии файла "database.ini" в проекте, и корректного абсолютного пути в файле "config.py"\n\n'
        f'Нажмите "w", если файл и путь присутствуют\n'
        f'Для выход выхода из программы нажмите любую клавишу\n')

    if start_question_database_ini != 'w':
        exit()

    start_question_hh = int(input('Загрузить данные с HH?\n'
                           '1 - Да\n'
                           '2 - Нет, продолжить работу с готовой бд\n'))

    if start_question_hh == 1:

        pages = int(input('Введите количество страниц для загрузки по каждому работадателю\n'
                          '0-20\n'))
        for employee in user_employee:

            print(f'\nid Работадателя - {employee[0]}, Название Работадателя - {employee[1]}\n')
            for element in employee:

                # Создание экземпляра класса для работы с API сайтов с вакансиями
                hh_api = HeadHunterAPI(element)

                while True:
                    hh_api.get_vacancies(pages)
                    vacancies_json.extend(hh_api.get_form_vac())
                    break
                break

            data.append({
                'ID': employee[0],
                'vacancies': vacancies_json
            })
            vacancies_json = []

        params = config()

        print('Создание бд...')
        database_name = str.lower(input((f'Введите название бд\n')))
        create_database(database_name, params)

        print('Заполнение бд данными...')
        save_data_to_database(data, database_name, params)

    # Работа с заполненной SQL базой данных
    database_name = str.lower(input((f'Введите название бд с которой надо работать далее\n')))

    params = config()
    conn = psycopg2.connect(database=database_name, user=params['user'], password=params['password'])
    conn.autocommit = True
    cur = conn.cursor()

    while True:
        db_manager_quest = \
            int(input('\nЧто хотите получить?\n'
                      '1 - получить список всех компаний и количество вакансий у каждой компании\n'
                      '2 - получить список всех вакансий с указанием названия компании,'
                      'названия вакансии и зарплаты и ссылки на вакансию.\n'
                      '3 - получить среднюю зарплату по вакансиям.\n'
                      '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям. \n'
                      '5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова,'
                      ' например “python”. \n'
                      '0. выход\n'
                      )
                )
        db_manager = DBManager(database_name, **params)
        if db_manager_quest == 1:
            db_manager.get_companies_and_vacancies_count()

        elif db_manager_quest == 2:
            db_manager.get_all_vacancies()

        elif db_manager_quest == 3:
            db_manager.get_avg_salary()

        elif db_manager_quest == 4:
            db_manager.get_vacancies_with_higher_salary()

        elif db_manager_quest == 5:
            word = input("Какое слово ищем? ")
            db_manager.get_vacancies_with_keyword(word)
        elif db_manager_quest == 0:
            quit()
        else:
            print('Укажите число из списка выше')


if __name__ == "__main__":
    main()
