from src.headhunter_api import HeadHunterAPI
from config import config
from src.utils import create_database, save_data_to_database
from config import config
import psycopg2


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
    start_question = input('Загрузить данные с HH?\n'
                           '1 - Да'
                           '2 - Нет, продолжить работу с готовой бд')
    if start_question == 1:
        for employee in user_employee:
            print(f'id Работадателя - {employee[0]}, Название Работадателя - {employee[1]}\n')
            for element in employee:

                # Создание экземпляра класса для работы с API сайтов с вакансиями
                hh_api = HeadHunterAPI(element)

                pages = int(input('Введите количество страниц для загрузки по каждому работадателю\n'
                                  '0-20\n'))

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
        create_database('youtube', params)

        print('Заполнение бд данными...')
        save_data_to_database(data, 'youtube', params)

    else:
        pass

    params = config()
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname='{database_name}'")
    result = cur.fetchone()

    # Если база данных существует, выполняем операцию DROP DATABASE
    if result:
        cur.execute(f"DROP DATABASE {database_name}")


    db_manager_quest = \
        int(input('Что хотите получит?\n'
                  '1 - получить список всех компаний и количество вакансий у каждой компании\n'
                  '2 - получить список всех вакансий с указанием названия компании,'
                  'названия вакансии и зарплаты и ссылки на вакансию.\n'
                  '3 - получить среднюю зарплату по вакансиям.\n'
                  '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям. \n'
                  '5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова,'
                  ' например “python”. \n'
                  )
            )


if __name__ == "__main__":
    main()
