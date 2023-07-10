# import psycopg2
# import queries
from config import config
# #
# #
# #
#
# f = config()
# print(f)
db_manager_quest = input('Что хотите получит?\n'
                         '1 - получить список всех компаний и количество вакансий у каждой компании\n'
                         '2 - получить список всех вакансий с указанием названия компании,'
                         'названия вакансии и зарплаты и ссылки на вакансию.\n'
                         '3 - получить среднюю зарплату по вакансиям.\n'
                         '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям. \n'
                         '5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова,'
                         ' например “python”. \n'
                         )

# print(db_manager_quest)

params = config()
print(params)


#
# def create_database(database_name: str, params: dict) -> None:
#     """
#     Создание базы данных и таблиц для сохранения данных
#     :param database_name:
#     :param params:
#     :return: None
#     """
#     conn = psycopg2.connect(dbname='postgres', **params)
#     conn.autocommit = True #автокоммит sql запросов
#     cur = conn.cursor()
#
#     cur.execute(f"DROP DATABASE {database_name}")
#     cur.execute(f"CREATE DATABASE {database_name}")
#
#     conn.close()
#
#
# # def create_table(database_name: str, params: dict) -> None:
#
#     conn = psycopg2.connect(dbname=database_name, **params)
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE channels (
#                 channel_id SERIAL PRIMARY KEY,
#                 title VARCHAR(255) NOT NULL,
#                 views INTEGER,
#                 subscribers INTEGER,
#                 videos INTEGER,
#                 channel_url TEXT
#             )
#         """)
#
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE videos (
#                 video_id SERIAL PRIMARY KEY,
#                 channel_id INT REFERENCES channels(channel_id),
#                 title VARCHAR NOT NULL,
#                 publish_date DATE,
#                 video_url TEXT
#             )
#         """)
#
#     conn.commit()
#     conn.close()
#
# def save_data_to_database(data: list, database_name: str, params: list) -> None:
#     """
#     Сохранение данных в базу данных
#     :param data:
#     :param database_name:
#     :param params:
#     :return: None
#     """
# conf = config()
# # crdb = create_database('database_name', conf )
# print(conf)

#
# from typing import Any
# import psycopg2
#
#
# def create_database(database_name: str, params: dict) -> None:
#     """
#     Создание базы данных и таблиц для сохранения данных
#     :param database_name:
#     :param params:
#     :return: None
#     """
#     conn = psycopg2.connect(dbname='postgres', **params)
#     conn.autocommit = True
#     cur = conn.cursor()
#
#     # Проверка наличия базы данных
#     cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname='{database_name}'")
#     result = cur.fetchone()
#
#     # Если база данных существует, выполняем операцию DROP DATABASE
#     if result:
#         cur.execute(f"DROP DATABASE {database_name}")
#     # Создание базы данных
#     cur.execute(f"CREATE DATABASE {database_name}")
#     conn.close()
#
#     conn = psycopg2.connect(dbname=database_name, **params)
#
#     # CREATE TABLE EMPLOYERS
#     with conn.cursor() as cur:
#         cur.execute("""
#             CREATE TABLE employers  (
#                 employer_id INTEGER UNIQUE,
#                 employer_name VARCHAR NOT NULl,
#                 hh_url VARCHAR ,
#                 company_url VARCHAR,
#                 address_raw TEXT
#                  )
#         """)
#
#     # CREATE TABLE vacancies
#     with conn.cursor() as cur:
#         cur.execute("""
#              CREATE TABLE vacancies(
#                 vacancy_id INT UNIQUE,
#                 employer_id INT references employers(employer_id) NOT NULL,
#                 vacancy_name VARCHAR,
#                 requirement VARCHAR,
#                 responsibility VARCHAR,
#                 salary_from REAL,
#                 salary_to REAL,
#                 salary_currency VARCHAR,
#                 url VARCHAR,
#                 area_id INT,
#                 area_name VARCHAR,
#                 experience VARCHAR,
#                 department_name VARCHAR
#                  )
#         """)
#
#     conn.commit()
#     conn.close()
#
#
# def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
#     """
#     Сохранение данных в базу данных
#     :param data:
#     :param database_name:
#     :param params:
#     :return: None
#     """
#     conn = psycopg2.connect(dbname=database_name, **params)
#
#     with conn.cursor() as cur:
#         for employer in data:
#             if 'vacancies' in employer:
#                 vacancy = employer['vacancies']
#                 emp_id = employer['ID']
#                 emp_check = 0
#                 for vacancy_info in vacancy:
#
#                     # Данная проверка используется, чтобы таблица employers не заполнялась одинаковыми данными
#                     if emp_id != emp_check:
#                         # Внесение данных в таблицу employers(РАБОТАДАТЕЛЬ) из загруженных вакансий по работадателю
#                         cur.execute(
#                             """
#                             INSERT INTO employers (employer_id, employer_name, hh_url, company_url, address_raw)
#                             VALUES (%s, %s, %s, %s, %s)
#                             --RETURNING employer_id
#                             """,
#                             (vacancy_info['employer_id'], vacancy_info['employer_name'], vacancy_info['employer_url'],
#                              vacancy_info['employer_alternate_url'], vacancy_info['address_raw'])
#                         )
#                         emp_check = emp_id
#                     else:
#                         pass
#
#                         # Внесение данных в таблицу vacancies(ВАКАНСИИ) из ранее загруженных вакансий по работадателю
#                     cur.execute(
#                         """
#                         INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, requirement, responsibility,
#                         salary_from, salary_to, salary_currency, url, area_id, area_name, experience, department_name)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                         """,
#                         (vacancy_info['id'], vacancy_info['employer_id'], vacancy_info['name'],
#                          vacancy_info['snippet_requirement'], vacancy_info['snippet_responsibility'],
#                          vacancy_info['salary_from'], vacancy_info['salary_to'], vacancy_info['salary_currency'],
#                          vacancy_info['alternate_url'], vacancy_info['area_id'], vacancy_info['area_name'],
#                          vacancy_info['experience']['name'], vacancy_info['department_name'])
#                     )
#     conn.commit()
#     conn.close()


мэйн

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

    # Работа с заполненной SQL базой данных
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
