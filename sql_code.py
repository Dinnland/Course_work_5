# sql код для класса DBManager

#Получает список всех компаний и количество вакансий у каждой компании.
sql_companies_and_vacancies_count = """SELECT e.employer_name,
                             count(v.vacancy_id) as num_vacancies
                      FROM employers e 
                      FULL JOIN vacancies v on v.employer_id = e.employer_id
                      GROUP BY e.employer_name"""

# Получает список всех вакансий с указанием названия компании,названия вакансии и зарплаты и ссылки на вакансию
sql_all_vacancies = """SELECT e.employer_name, 
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                       FROM vacancies v
                       LEFT JOIN employers e on v.employer_id = e.employer_id"""


# Получает среднюю зарплату по вакансиям
sql_avg_salary = """SELECT avg(case when v.salary_to = 0 then v.salary_from else v.salary_to end)
                      FROM vacancies v
                      WHERE v.salary_to > 0 or v.salary_from > 0 """

# Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
sql_vacancies_with_higher_salary = """SELECT e.employer_name, 
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                      FROM vacancies v
                      LEFT JOIN employers e on v.employer_id = e.employer_id
                      WHERE CASE WHEN v.salary_to = 0 THEN v.salary_from ELSE v.salary_to END > 
                      (SELECT avg(case when v.salary_to = 0 then v.salary_from else v.salary_to end)
                      FROM vacancies v
                      WHERE v.salary_to > 0 or v.salary_from > 0)"""

# Получает список всех вакансий, в названии которых содержатся переданные в метод слова
sql_vacancies_with_keyword = """SELECT e.employer_name, 
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                      FROM vacancies v
                      LEFT JOIN employers e on v.employer_id = e.employer_id
                      WHERE v.vacancy_name LIKE %s"""