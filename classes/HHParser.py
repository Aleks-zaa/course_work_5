import requests


class HHParser:

    @staticmethod
    def get_request():
        params = {
            "per_page": 10,
            "sort_by": "by_vacancies_open"
        }
        response = requests.get("http://api.hh.ru/employers/", params)
        if response.status_code == 200:
            return response.json()["items"]

    def get_employers(self):
        data = self.get_request()
        employers = []
        for employer in data:
            employers.append({"id": employer["id"], "name": employer["name"]})
        return employers

    @staticmethod
    def get_vacancies_from_company(employer_id):
        params = {
            "per_page": 20,
            "employer_id": employer_id
        }
        response = requests.get("http://api.hh.ru/vacancies/", params)
        if response.status_code == 200:
            return response.json()["items"]

    def get_all_vacancies(self):
        employers = self.get_employers()
        vacancies = []
        for employer in employers:
            vacancies.extend(self.get_vacancies_from_company(employer["id"]))
        return vacancies

    def filter_vacancies(self):
        vacancies = self.get_all_vacancies()
        filter_data = []
        for vacancy in vacancies:
            if not vacancy["salary"]:
                salary_from = 0
                salary_to = 0
            else:
                salary_from = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_to = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            filter_data.append({
                "id": vacancy["id"],
                "name": vacancy["name"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "url": vacancy["alternate_url"],
                "employer": vacancy["employer"]["id"],
            })
        return filter_data

