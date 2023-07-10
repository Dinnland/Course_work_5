# import os
#
# from src.utils import create_database, save_data_to_database
# from config import config
#
#
# def main():
#     # api_key = os.getenv('YT_API_KEY')
#     # channel_ids = [
#     #     'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
#     #     'UCwHL6WHUarjGfUM_586me8w',  # highload
#     #
#     # ]
#     params = config()
#
#     # data = get_youtube_data(api_key, channel_ids)
#     data = [
#         {
#         "ID": "80",
#         "vacancies": [
#             {
#                 "id": "83062837",
#                 "premium": 'false',
#                 "name": "Специалист по документообороту",
#                 "department_name": " Альфа-Банк",
#                 "has_test": 'false',
#                 "area_id": "68",
#                 "area_name": "Омск",
#                 "salary_from": 29100,
#                 "salary_to": null,
#                 "salary_currency": "RUR",
#                 "type_name": "Открытая",
#                 "address_raw": 'null',
#                 "response_url": 'null',
#                 "published_at": "2023-07-06T07:30:51+0300",
#                 "created_at": "2023-07-06T07:30:51+0300",
#                 "archived": 'false',
#                 "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=83062837",
#                 "insider_interview":
#                     {
#                     "id": "30864",
#                     "url": "https://hh.ru/interview/30864?employerId=80"
#                     },
#                 "url": "https://api.hh.ru/vacancies/83062837?host=hh.ru",
#                 "alternate_url": "https://hh.ru/vacancy/83062837",
#                 "employer_id": "80",
#                 "employer_name": "Альфа-Банк",
#                 "snippet_requirement": "Образование не ниже среднего специального. Умение работать с большим объемом информации. Опыт работы в банке желателен.",
#                 "snippet_responsibility": "Подготовка клиентских досье для сдачи в архив. Подготовка карт на выдачу. Подготовка документов для выдачи для выездных специалистов и партнерским...",
#                 "contacts": 'null',
#                 "employer_url": "https://api.hh.ru/employers/80",
#                 "employer_alternate_url": "https://hh.ru/employer/80",
#                 "schedule_name": [],
#                 "working_time_intervals": [],
#                 "working_time_modes": [],
#                 "accept_temporary": 'false',
#                 "experience":
#                     {
#                     "id": "noExperience",
#                     "name": "Нет опыта"
#                     }
#             }
#         ]
#     }
#     ]
#     create_database('youtube', params)
#     save_data_to_database(data, 'youtube', params)
#
#
# if __name__ == '__main__':
#     main()
