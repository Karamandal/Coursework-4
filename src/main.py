from utils.API import API_HH
from utils.Class_Vacancy import Vacancies
from utils.Vacancy_aggregator import JSONJobStorage


def get_value(dictionary, *keys):
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary


def user_interaction():
    name_vacancy = input('Введите название вакансии: ')
    keyword_vacancy = input('Введите ключевые слова для фильтрации вакансий: ').split()
    top_n = int(input('Введите количество вакансий для отображения по убыванию зарплаты: '))

    vacancy_hh = API_HH()
    all_vacancy = vacancy_hh.getting_vacancies(name_vacancy)
    all_vacancy = [vacancy for vacancy in all_vacancy.get('items')]
    if len(all_vacancy) == 0:
        print("По вашему запросу вакансий не найдено")
    else:
        print(f"Всего найдено вакансий по запросу {name_vacancy}: {len(all_vacancy)}")
        print(f"Топ {top_n or len(all_vacancy)} вакансий по зарплате:")

        vacancies = []

        for vacancy in all_vacancy:
            name = get_value(vacancy, 'name')
            min_salary = get_value(vacancy, 'salary', 'from')
            max_salary = get_value(vacancy, 'salary', 'to')
            salary_currency = get_value(vacancy, 'salary', 'currency')
            requirement = get_value(vacancy, 'snippet', 'requirement')
            link = get_value(vacancy, 'alternate_url')

            if any(keyword.lower() in str(vacancy).lower() for keyword in keyword_vacancy):
                vacancies.append(Vacancies(name, min_salary, max_salary, salary_currency, requirement, link))

        vacancies.sort(key=lambda x: x.max_salary or 0, reverse=True)
        top_vacancies = vacancies[:top_n]
        for v in top_vacancies:
            result = Vacancies.__repr__(v)
            print(result)

            # Создаем экземпляр класса JSONFileWriter
            file_writer = JSONJobStorage('../data/vacancies.json')

            # Подготавливаем данные для записи в файл
            data_to_write = [vars(vacancy) for vacancy in top_vacancies]

            # Записываем данные в файл
            file_writer.add_vacancy(data_to_write)


user_interaction()
