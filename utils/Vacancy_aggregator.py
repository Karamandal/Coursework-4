from abc import ABC, abstractmethod
import json


class AbstractJobStorage(ABC):
    """
    Абстрактный класс для работы с данными
    """
    @abstractmethod
    def add_vacancy(self, vacancy_info):
        pass

    @abstractmethod
    def get_vacancies(self, criteria):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy):
        pass


class JSONJobStorage(AbstractJobStorage):
    """
    Класс для работы с данными
    """
    def __init__(self, file_path="=../data/vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy_info):
        with open(self.file_path, 'w', encoding="utf8") as file:
            json.dump(vacancy_info, file)
            file.write('\n')

    def get_vacancies(self, criteria):
        result = []
        with open(self.file_path, 'r') as file:
            for line in file:
                vacancy = json.loads(line)
                # Проверка критериев (заглушка)
                if criteria in vacancy.values():
                    result.append(vacancy)
        return result

    def delete_vacancies(self, vacancy):
        open(self.file_path, 'w').close()