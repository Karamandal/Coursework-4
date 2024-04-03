import requests
from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    @abstractmethod
    def getting_vacancies(self, keyword):
        pass


class API_HH(AbstractAPI):
    def getting_vacancies(self, keyword):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data
