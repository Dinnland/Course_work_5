CREATE DATABASE {database_name};

CREATE TABLE employers  (
                employer_id INTEGER UNIQUE,
                employer_name VARCHAR NOT NULl,
                hh_url VARCHAR ,
                company_url VARCHAR,
                address_raw TEXT
                 );

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
                 );


"""
INSERT INTO employers (employer_id, employer_name, hh_url, company_url, address_raw)
VALUES (%s, %s, %s, %s, %s);
--RETURNING employer_id
""",
(vacancy_info['employer_id'], vacancy_info['employer_name'], vacancy_info['employer_url'],
 vacancy_info['employer_alternate_url'], vacancy_info['address_raw'])


"""
INSERT INTO vacancies (vacancy_id, employer_id, vacancy_name, employer_name, requirement, responsibility,
salary_from, salary_to, salary_currency, url, area_id, area_name, experience, department_name)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""",
(vacancy_info['id'], vacancy_info['employer_id'], vacancy_info['name'], vacancy_info['employer_name'],
 vacancy_info['snippet_requirement'], vacancy_info['snippet_responsibility'],
 vacancy_info['salary_from'], vacancy_info['salary_to'], vacancy_info['salary_currency'],
 vacancy_info['alternate_url'], vacancy_info['area_id'], vacancy_info['area_name'],
 vacancy_info['experience']['name'], vacancy_info['department_name']


SELECT e.employer_name,
                             count(v.vacancy_id) as num_vacancies
                      FROM employers e
                      FULL JOIN vacancies v on v.employer_id = e.employer_id
                      GROUP BY e.employer_name;


SELECT e.employer_name,
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                       FROM vacancies v
                       LEFT JOIN employers e on v.employer_id = e.employer_id;


SELECT avg(case when v.salary_to = 0 then v.salary_from else v.salary_to end)
                      FROM vacancies v
                      WHERE v.salary_to > 0 or v.salary_from > 0;


SELECT e.employer_name,
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                      FROM vacancies v
                      LEFT JOIN employers e on v.employer_id = e.employer_id
                      WHERE CASE WHEN v.salary_to = 0 THEN v.salary_from ELSE v.salary_to END >
                      (SELECT avg(case when v.salary_to = 0 then v.salary_from else v.salary_to end)
                      FROM vacancies v
                      WHERE v.salary_to > 0 or v.salary_from > 0);


SELECT e.employer_name,
                             v.vacancy_name,
                             case when v.salary_to = 0 then v.salary_from else v.salary_to end as salary,
                             v.url
                      FROM vacancies v
                      LEFT JOIN employers e on v.employer_id = e.employer_id
                      WHERE v.vacancy_name LIKE %s