from src.headhunter_api import HeadHunterAPI
from config import config
from src.utils import create_database, save_data_to_database
from config import config


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


if __name__ == "__main__":
    main()
