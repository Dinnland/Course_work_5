# import json
# # from src.vacancy import Vacancy
#
#
# class Connector:
#     def __init__(self, user_keyword, vacancies_json):
#         self.connect_file = f'{str(user_keyword).title()}.json'
#
#         self.insert(vacancies_json)
#
#     def insert(self, vacancies_json):
#         with open(self.connect_file, 'w', encoding='utf-8') as f:
#             json.dump(vacancies_json, f, indent=4, ensure_ascii=False) # ,  ensure_ascii=False
