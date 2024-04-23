from classes.db_manager import DBManager
from utils.utils import (create_database, create_tables, insert_data_into_tables, print_vacancy, print_vacancy1,
                         print_vacancy2, print_vacancy3, print_vacancy4, print_vacancy5)


def main() -> None:
    """Основная функция"""

    list_employers = [2180, 2180, 2748, 3127, 3388, 3529, 3529, 3776, 4181, 4934, 49357, 54979, 64174, 78638, 78638,
                      1648566, 1942330, 1942336, 9498112, 93787326]
    dbm = DBManager('')
    create_database('db_hh')
    create_tables('db_hh')
    insert_data_into_tables(list_employers)

    while True:

        new = input(
            '1 - список всех компаний и кол-во вакансий у каждой компании\n'
            '2 - список всех вакансий\n'
            '3 - средняя зарплата по вакансиям\n'
            '4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
            '5 - список вакансий по ключевому слову\n'
            '0 - завершить работу\n'
        )

        if new == '1':
            print_vacancy1(dbm.get_companies_and_vacancies_count())
        elif new == '2':
            print_vacancy2(dbm.get_all_vacancies())
        elif new == '3':
            print_vacancy3(dbm.get_avg_salary())
        elif new == '4':
            print_vacancy4(dbm.get_vacancies_with_higher_salary())
        elif new == '5':
            keyword = str(input('Найти: '))
            print_vacancy5(dbm.get_vacancies_with_keyword(keyword))
        elif new == 'Выход':
            break


if __name__ == "__main__":
    main()
