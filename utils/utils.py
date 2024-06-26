import psycopg2
from utils.config import config
from classes.HHParser import HHParser


def create_database(db_name):
    """Функция создания базы данных"""

    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    cur.execute(f'CREATE DATABASE {db_name}')

    cur.close()
    conn.close()


def create_tables(db_name):
    """Функция создания таблиц"""

    conn = psycopg2.connect(dbname="db_hh", **config())
    with conn:
        with conn.cursor() as cur:
            cur.execute('''CREATE TABLE employers 
                           (employer_id int PRIMARY KEY,
                           name VARCHAR(255) UNIQUE NOT NULL,
                           open_vacancies int
                           );
                           ''')
            cur.execute('''CREATE TABLE vacancies
                        (vacancy_id int,
                        name VARCHAR(255) NOT NULL,
                        salary_from int,
                        salary_to int,
                        url VARCHAR(255),
                        employer_id int REFERENCES employers(employer_id) NOT NULL
                        );
                        ''')
    conn.close()


def insert_data_into_tables(db_name):
    """Функция заполнения таблиц"""

    hh = HHParser()
    employers = hh.get_employers()
    vacancies = hh.filter_vacancies()
    conn = psycopg2.connect(dbname='db_hh', **config())
    with conn:
        with conn.cursor() as cur:
            for employer in employers:
                cur.execute("""
                                INSERT INTO employers VALUES (%s, %s)
                            """, (employer["id"], employer["name"]))
            for vacancy in vacancies:
                cur.execute("""INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)
                                    """, (vacancy["id"], vacancy["name"],
                                          vacancy["salary_from"], vacancy["salary_to"],
                                          vacancy["url"], vacancy["employer"]))
    conn.close()


def print_vacancy(data):
    """Функция вывода вакансий"""

    for vacancy in data:
        print("================================================================")
        print(f"Работодатель - {vacancy[0]}")
        print(f"Должность - {vacancy[1]}")
        if vacancy[2] == 0 and vacancy[3] == 0:
            print(f"Оклад - по договоренности ")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == 0 or vacancy[3] == 0:
            if vacancy[2] == 0:
                print(f"Оклад до {vacancy[3]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
            else:
                print(f"Оклад от {vacancy[2]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == vacancy[3]:
            print(f"Оклад - {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        else:
            print(f"Оклад от {vacancy[2]} до {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")


def print_vacancy1(data):
    """Функция вывода  всех компаний и вакансий у каждой компании"""

    for vacancy in data:
        print("================================================================")
        print(f"Работодатель - {vacancy[0]}")
        print(f"Колличество вакансий - {vacancy[1]}")


def print_vacancy2(data):
    """Функция вывода всех вакансий"""

    for vacancy in data:
        print("================================================================")
        print(f"Работодатель - {vacancy[0]}")
        print(f"Должность - {vacancy[1]}")
        if vacancy[2] == 0 and vacancy[3] == 0:
            print(f"Оклад - по договоренности ")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == 0 or vacancy[3] == 0:
            if vacancy[2] == 0:
                print(f"Оклад до {vacancy[3]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
            else:
                print(f"Оклад от {vacancy[2]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == vacancy[3]:
            print(f"Оклад - {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        else:
            print(f"Оклад от {vacancy[2]} до {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")


def print_vacancy3(data):
    """Функция вывода средней з.п"""

    print(f"Средняя з.п. - {data[0]}")


def print_vacancy4(data):
    """Функция вывода всех вакансий, у которых зарплата выше средней по всем вакансия"""

    for vacancy in data:
        print("================================================================")
        print(f"Работодатель - {vacancy[0]}")
        print(f"Должность - {vacancy[1]}")
        if vacancy[2] == 0 and vacancy[3] == 0:
            print(f"Оклад - по договоренности ")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == 0 or vacancy[3] == 0:
            if vacancy[2] == 0:
                print(f"Оклад до {vacancy[3]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
            else:
                print(f"Оклад от {vacancy[2]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == vacancy[3]:
            print(f"Оклад - {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        else:
            print(f"Оклад от {vacancy[2]} до {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")


def print_vacancy5(data):
    """Функция вывода всех вакансий по ключевому слову."""

    for vacancy in data:
        print("================================================================")
        print(f"Вакансия - {vacancy[1]}")
        if vacancy[2] == 0 and vacancy[3] == 0:
            print(f"Оклад - по договоренности ")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == 0 or vacancy[3] == 0:
            if vacancy[2] == 0:
                print(f"Оклад до {vacancy[3]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
            else:
                print(f"Оклад от {vacancy[2]}")
                print(f"Ссылка на вакансию - {vacancy[4]}")
        elif vacancy[2] == vacancy[3]:
            print(f"Оклад - {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")
        else:
            print(f"Оклад от {vacancy[2]} до {vacancy[3]}")
            print(f"Ссылка на вакансию - {vacancy[4]}")
