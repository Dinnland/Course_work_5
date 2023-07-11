import requests      # Для запросов по API
import json          # Для обработки полученных результатов
import time          # Для задержки между запросами
import os            # Для работы с файлами
# import pandas as pd  # Для формирования датафрейма с результатами


# def getEmployers():
#     req = requests.get('https://api.hh.ru/employers')
#     data = req.content.decode()
#     req.close()
#     count_of_employers = json.loads(data)['found']
#     employers = []
#     i = 2000
#     j = count_of_employers
#     while i < j:
#         req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
#         data = req.content.decode()
#         req.close()
#         jsObj = json.loads(data)
#         try:
#             employers.append([jsObj['id'], jsObj['name']])
#             i += 1
#             print([jsObj['id'], jsObj['name']])
#         except:
#             i += 1
#             j += 1
#         if i % 200 == 0:
#             time.sleep(0.1)
#     return employers
#
#
# employers = getEmployers()

user_employee = [
         ['80', 'Альфа-Банк'],
         ['370', 'АльфаСтрахование'],
         ['402', 'Компания ТрансТелеКом'],
         ['548', 'АстроСофт'],
         ['882', '1С'],
         ['2523', 'М.Видео-Эльдорадо'],
         ['2589', 'D-Link'],
         ['2683', 'Форпост, АКБ'],
         ['2748', 'Ростелеком'],
         ['2808', 'Открытые Технологии']
    ]

for employee in user_employee:
     print(f'id Работадателя - {employee[0]}, Название Работадателя - {employee[1]}\n')
     for element in employee:
          print(f'{element}\n')
          break

{
    'id': '81236105',
    'premium': False,
    'name': 'Back-end developer Python Junior / Бекенд-разработчик Python',
    'department': None,
    'has_test': False,
    'response_letter_required': False,
    'area': {
      'id': '1550',
      'name': 'Таганрог',
      'url': 'https://api.hh.ru/areas/1550'
    },
    'salary': {
      'from': 50000,
      'to': None,
      'currency': 'RUR',
      'gross': False
    },
    'type': {
      'id': 'open',
      'name': 'Открытая'
    },
    'address': {
      'city': 'Таганрог',
      'street': 'Котлостроительная улица',
      'building': '37-19',
      'lat': 47.250008,
      'lng': 38.891204,
      'description': None,
      'raw': 'Таганрог, Котлостроительная улица, 37-19',
      'metro': None,
      'metro_stations': [],
      'id': '5658825'
    },
    'response_url': None,
    'sort_point_distance': None,
    'published_at': '2023-05-29T13:24:47+0300',
    'created_at': '2023-05-29T13:24:47+0300',
    'archived': False,
    'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=81236105',
    'insider_interview': None,
    'url': 'https://api.hh.ru/vacancies/81236105?host=hh.ru',
    'adv_response_url': None,
    'alternate_url': 'https://hh.ru/vacancy/81236105',
    'relations': [],
    'employer': {
      'id': '5375272',
      'name': 'APPTRIX',
      'url': 'https://api.hh.ru/employers/5375272',
      'alternate_url': 'https://hh.ru/employer/5375272',
      'logo_urls': {
        '240': 'https://hhcdn.ru/employer-logo/3809784.jpeg',
        '90': 'https://hhcdn.ru/employer-logo/3809783.jpeg',
        'original': 'https://hhcdn.ru/employer-logo-original/842227.jpg'
      },
      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5375272',
      'accredited_it_employer': False,
      'trusted': True
    },
    'snippet': {
      'requirement': 'С уверенными знаниями <highlighttext>Python</highlighttext> 3. С уверенными знаниями фреймворков: Django, Django REST Framework. Опыт работы с Selenium. Умением работать с...',
      'responsibility': 'Участвовать в разработке новых проектов. Поддерживать и модернизировать существующие. Разрабатывать внутренние проекты компании.'
    },
    'contacts': None,
    'schedule': None,
    'working_days': [],
    'working_time_intervals': [],
    'working_time_modes': [],
    'accept_temporary': False,
    'professional_roles': [
      {
        'id': '96',
        'name': 'Программист, разработчик'
      }
    ],
    'accept_incomplete_resumes': False,
    'experience': {
      'id': 'between1And3',
      'name': 'От 1 года до 3 лет'
    },
    'employment': {
      'id': 'full',
      'name': 'Полная занятость'
    }
  },