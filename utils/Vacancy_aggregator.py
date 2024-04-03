from abc import ABC, abstractmethod
import json


class AbstractJobStorage(ABC):

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

    def __init__(self, file_path="vacancies.json"):
        self.file_path = file_path

    def add_vacancy(self, vacancy_info):
        with open(self.file_path, 'a') as file:
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