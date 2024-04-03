class Vacancies:

    def __init__(self, name, min_salary, max_salary, currency, requirements, link):
        self.name = name
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.currency = currency
        self.requirements = requirements
        self.link = link

    def __lt__(self, other):
        """
        Сравнивает зарплаты вакансий
        """
        return self.min_salary < other.max_salary

    def __repr__(self):
        return (f"""Название вакансии: {self.name}\n
        Заработная плата: {self.max_salary} - {self.min_salary} {self.currency}\nТребования: {self.requirements}
        Ссылка на вакансию: {self.link}""")


