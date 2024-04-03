from utils.API import API_HH
from utils.Class_Vacancy import Vacancies
from utils.Vacancy_aggregator import JSONJobStorage


def user_interaction():
    name_vacancy = input('Введите название вакансии: ')
    keyword_vacancy = input('Введите ключевые слова для фильтрации вакансий: ').split()
    top_n = int(input('Введите количество вакансий для отображения по убыванию зарплаты: '))

    vacancy_hh = API_HH()
    all_vacancy = vacancy_hh.getting_vacancies(name_vacancy)


