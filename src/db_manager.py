import psycopg2
from config import config

class DBManager:

    def __init__(self, database_name: str, params: dict):
        conn = psycopg2.connect(database_name='postgres', **params)
        self._db_name = conn['host']
        self._user = conn[1]
        self._password = conn[2]
        # cur = conn.cursor()
        # conn.cursor.execute(query)

    def connect(self, query):
        conn = psycopg2.connect(database_name='postgres', **params)
        cur = conn.cursor()
        results = conn.cursor.fetchall()
        for i in results:
            print(i)

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании."""
        query = """SELECT e.company_name,
                                  count(v.vacancy_id) as num_vacancies
                           FROM employers e 
                           FULL JOIN vacancies v on v.employer_id = e.employer_id
                           GROUP BY e.company_name"""
        self.connect(query)


    def get_all_vacancies(self):
        """
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        pass


    def get_avg_salary():
        """получает среднюю зарплату по вакансиям"""
        pass


    def get_vacancies_with_higher_salary():
        """
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        pass


    def get_vacancies_with_keyword():
        """
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        """
        pass

