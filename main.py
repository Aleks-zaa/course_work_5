from classes.db_manager import DBManager
from utils.utils import create_database, create_tables, insert_data_into_tables, print_vacancy


def user_interaction():
    """Основная функция"""

    list_employers = [2180, 2180, 2748, 3127, 3388, 3529, 3529, 3776, 4181, 4934, 49357, 54979, 64174, 78638, 78638,
                      1648566, 1942330, 1942336, 9498112, 93787326]
    dbm = DBManager('')
    create_database('db_hh')
    create_tables('db_hh')
    insert_data_into_tables(list_employers)
    name_vac = str(input('Какую профессию необходимо?\n '))
    data = dbm.get_all_with_keyword(name_vac)
    # print(data)
    print_vacancy(data)


if __name__ == "__main__":
    user_interaction()
