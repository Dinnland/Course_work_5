from src.api import Engine
from src.exceptions import ParsingError
import requests


class HeadHunterAPI(Engine):
    """
    Класс для работы с API HeadHunter
    """

    # адрес API
    url = "https://api.hh.ru/vacancies/"

    def __init__(self, key):
        self.params = {
            "per_page": 100,
            "page": None,
            # "text": key,
            "archived": False,
            "employer_id": key
        }
        # Тут наша прога
        self.headers = {
            "User-Agent": "HeadHunterAPI_cw4"
            }
        # СПИСОК ВАКАНСИЙ
        self.vacancies = []

    def get_request(self):
        """
        Метод создает запрос к api сайта
        :return: response.json()["Items"] список из item
        """
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка при получении вакансий! статус: {response.status_code}')
        return response.json()["items"]

    def get_vacancies(self, page_count=2):
        """
        получение вакансий
        :param page_count:
        :return:
        """
        self.vacancies = []  # очищение списка вакансий
        # постраничный перебор
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page
            print(f"({self.__class__.__name__}) Парсинг страницы {page} -", end=" ")
            try:
                page_vacancies = self.get_request()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий: {len(page_vacancies)}')
            if len(page_vacancies) == 0:
                break


    def get_form_vac(self):
        """
        метод, добавляющий вакансии в отдельный список formatted_vacancies
        """
        data = []

        formatted_vacancies = []

        for vacancy in self.vacancies:

            if vacancy['salary'] is not None:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
                salary_currency = vacancy['salary']['currency']
            else:
                salary_from = None
                salary_to = None
                salary_currency = None

            if vacancy['address'] is not None:  # or vacancy['address'] != 'null':
                address_raw = vacancy['address']['raw']
            else:
                address_raw = None

            if vacancy['department'] is not None:
                department_name = vacancy['department']['name']
            else:
                department_name = None

            formatted_vacancy = {
                'id': vacancy['id'],
                'premium': vacancy['premium'],
                'name': vacancy['name'],
                'department_name': department_name,
                'has_test': vacancy['has_test'],
                'area_id': vacancy['area']['id'],
                'area_name': vacancy['area']['name'],
                'salary_from': salary_from,
                'salary_to': salary_to,
                'salary_currency': salary_currency,
                'type_name': vacancy['type']['name'],
                'address_raw': address_raw,
                'response_url': vacancy['response_url'],
                'published_at': vacancy['published_at'],
                'created_at': vacancy['created_at'],
                'archived': vacancy['archived'],
                'apply_alternate_url': vacancy['apply_alternate_url'],
                'insider_interview': vacancy['insider_interview'],
                'url': vacancy['url'],
                'alternate_url': vacancy['alternate_url'],
                'employer_id': vacancy['employer']['id'],
                'employer_name': vacancy['employer']['name'],
                'snippet_requirement': vacancy['snippet']['requirement'],
                'snippet_responsibility': vacancy['snippet']['responsibility'],
                'contacts': vacancy['contacts'],
                'employer_url': vacancy['employer']['url'],
                'employer_alternate_url': vacancy['employer']['alternate_url'],
                'schedule_name': vacancy['working_days'],
                'working_time_intervals': vacancy['working_time_intervals'],
                'working_time_modes': vacancy['working_time_modes'],
                'accept_temporary': vacancy['accept_temporary'],
                'experience': vacancy['experience']
            }
            formatted_vacancies.append(formatted_vacancy)
            formatted_vacancy = {}
            data.append(formatted_vacancies)

        return formatted_vacancies
