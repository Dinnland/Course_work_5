import psycopg2
from sql_code import *


class DBManager:
    """
    класс DBManager, который подключается к БД Postgres и работает с бд, таблицами SQL
    """

    def __init__(self, database_name: str, host, user, port, password):
        self.database_name = database_name
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def connect(self, query):
        """Выводит данные по запросу ниженаписанных  функций"""
        conn = psycopg2.connect(database=self.database_name, user=self.user, password=self.password)
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        for i in results:
            print(i)

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        query = sql_companies_and_vacancies_count
        self.connect(query)

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        query = sql_all_vacancies
        self.connect(query)

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        query = sql_avg_salary
        self.connect(query)

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        query = sql_vacancies_with_higher_salary
        self.connect(query)

    def get_vacancies_with_keyword(self, word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        query = sql_vacancies_with_keyword
        keyword = '%' + word + '%'

        conn = psycopg2.connect(database=self.database_name, user=self.user, password=self.password)
        cur = conn.cursor()
        cur.execute(query, (keyword,))
        results = cur.fetchall()
        if len(results) == 0:
            print(f"В названиях вакансий слова '{word}' не найдено\n")
        else:
            for i in results:
                print(i)
