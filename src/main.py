from utils.API import API_HH
from utils.Class_Vacancy import Vacancies
from utils.Vacancy_aggregator import JSONJobStorage


def get_value(dictionary, *keys):
    """
    Возвращает значение словаря по ключу
    """
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary


def user_interaction():
    """
    Взаимодействует с пользователем
    """
    name_vacancy = input('Введите название вакансии: ')
    keyword_vacancy = input('Введите ключевые слова для фильтрации вакансий: ').split()
    top_n = int(input('Введите количество вакансий для отображения по убыванию зарплаты: '))

    vacancy_hh = API_HH()
    # Заходит на ресурс
    all_vacancy = vacancy_hh.getting_vacancies(name_vacancy)
    # Получает результат по запросу
    all_vacancy = [vacancy for vacancy in all_vacancy.get('items')]
    # Делает перебор по полученному результату
    if len(all_vacancy) == 0:
        print("По вашему запросу вакансий не найдено")
    else:
        print(f"Всего найдено вакансий по запросу {name_vacancy}: {len(all_vacancy)}")
        print(f"Топ {top_n or len(all_vacancy)} вакансий по зарплате:")

        vacancies = []

        for vacancy in all_vacancy:
            # Получает данные по ключу
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

            # Создает экземпляр класса JSONJobStorage
            file_writer = JSONJobStorage('../data/vacancies.json')

            # Подготавливает данные для записи в файл
            data_to_write = [vars(vacancy) for vacancy in top_vacancies]

            # Записывает данные в файл
            file_writer.add_vacancy(data_to_write)


user_interaction()
