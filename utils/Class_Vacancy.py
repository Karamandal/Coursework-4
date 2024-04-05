class Vacancies:
    """
    Класс для работы с вакансией
    """
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
        """
        Выводит данные
        """
        return (f"\nНазвание вакансии: {self.name}\n"
                f"Заработная плата: {self.max_salary} - {self.min_salary} {self.currency}\n"
                f"Требования: {self.requirements}\nСсылка на вакансию: {self.link}\n")

    def validate_data(self):
        """
        Валидация данный о вакансии
        """
        if not self.min_salary and not self.max_salary:
            self.min_salary = 0
