from typing import Any
import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """
    Создание базы данных и таблиц для сохранения данных
    :param database_name:
    :param params:
    :return: None
    """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    # Проверка наличия базы данных
    cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname='{database_name}'")
    result = cur.fetchone()

    # Если база данных существует, выполняем операцию DROP DATABASE
    if result:
        cur.execute(f"DROP DATABASE {database_name}")

    # Создание базы данных
    cur.execute(f"CREATE DATABASE {database_name}")
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    # CREATE TABLE EMPLOYERS
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers  (
                employer_id INTEGER UNIQUE,
                employer_name VARCHAR NOT NULl,
                hh_url VARCHAR ,
                company_url VARCHAR,
                address_raw TEXT
                 )
        """)

    # CREATE TABLE vacancies
    with conn.cursor() as cur:
        cur.execute("""            
             CREATE TABLE vacancies(
                vacancy_id INT UNIQUE,
                employer_id INT references employers(employer_id) NOT NULL,
                employer_name VARCHAR NOT NULl,
                vacancy_name VARCHAR,
                requirement VARCHAR,
                responsibility VARCHAR,
                salary_from REAL,
                salary_to REAL,
                salary_currency VARCHAR,
                url VARCHAR,
                area_id INT,
                area_name VARCHAR,
                experience VARCHAR,
                department_name VARCHAR
                 )
        """)
    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """
    Сохранение данных в базу данных
    :param data:
    :param database_name:
    :param params:
    :return: None
    """
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for employer in data:
            if 'vacancies' in employer:
                vacancy = employer['vacancies']
                emp_id = employer['ID']
                emp_check = 0
                for vacancy_info in vacancy:

                    # Данная проверка используется, чтобы таблица employers не заполнялась одинаковыми данными
                    if emp_id != emp_check:
                        # Внесение данных в таблицу employers(РАБОТАДАТЕЛЬ) из загруженных вакансий по работадателю
                        cur.execute(
                            """
                            INSERT INTO employers (employer_id, employer_name, hh_url, company_url, address_raw)
                            VALUES (%s, %s, %s, %s, %s)
                            --RETURNING employer_id
                            """,
                            (vacancy_info['employer_id'], vacancy_info['employer_name'], vacancy_info['employer_url'],
                             vacancy_info['employer_alternate_url'], vacancy_info['address_raw'])
                        )
                        emp_check = emp_id
                    else:
                        pass

                        # Внесение данных в таблицу vacancies(ВАКАНСИИ) из ранее загруженных вакансий по работадателю
                    cur.execute(
                        """
                        INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, employer_name, requirement, responsibility,
                        salary_from, salary_to, salary_currency, url, area_id, area_name, experience, department_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (vacancy_info['id'], vacancy_info['employer_id'], vacancy_info['name'], vacancy_info['employer_name'],
                         vacancy_info['snippet_requirement'], vacancy_info['snippet_responsibility'],
                         vacancy_info['salary_from'], vacancy_info['salary_to'], vacancy_info['salary_currency'],
                         vacancy_info['alternate_url'], vacancy_info['area_id'], vacancy_info['area_name'],
                         vacancy_info['experience']['name'], vacancy_info['department_name'])
                    )
    conn.commit()
    conn.close()
