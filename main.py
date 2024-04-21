from classes.db_manager import DBManager
from utils.utils import create_database, create_tables, insert_data_into_tables


def user_interaction():
    list_employers = [2180, 2180, 2748, 3127, 3388, 3529, 3529, 3776, 4181, 4934, 49357, 54979, 64174, 78638, 78638,
                      1648566, 1942330, 1942336, 9498112, 93787326]
    dbm = DBManager('')
    # print(dbm)
    create_database('HH_BASE')
    create_tables('HH_BASE')
    insert_data_into_tables(list_employers)
    name_vac = str(input('Какую профессию  необходимо? '))
    count_vac = int(input('Сколько вакансий? '))
    print(dbm.get_vacancies_with_keyword(name_vac))


if __name__ == "__main__":
    user_interaction()
