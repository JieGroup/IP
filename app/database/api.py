from app._typing import Database_Type

from app.database.strategy.api import DatabaseOperator

def set_database_type(
    database_type: str
) -> type[DatabaseOperator]:

    '''
        Set database strategy
    '''

    db_operator = DatabaseOperator()
    db_operator.set_database(database_type=database_type)
    return db_operator

def get_all_documents(
    database_type: Database_Type,
    **kwargs
) -> list:
    
    '''
        Wrapper of database strategy and call corresponding funcion
    '''

    db_operator = set_database_type(database_type=database_type)
    return db_operator.get_all_documents(**kwargs)
    
def search_document(
    database_type: Database_Type,
    **kwargs
) -> list:

    '''
        Wrapper of database strategy and call corresponding funcion
    '''

    db_operator = set_database_type(database_type=database_type)
    return db_operator.search_document(**kwargs)

def create_document(
    database_type: Database_Type,
    **kwargs
) -> list:

    '''
        Wrapper of database strategy and call corresponding funcion
    '''

    db_operator = set_database_type(database_type=database_type)
    return db_operator.create_document(**kwargs)

def update_document(
    database_type: Database_Type,
    **kwargs
) -> list:

    '''
        Wrapper of database strategy and call corresponding funcion
    '''

    db_operator = set_database_type(database_type=database_type)
    return db_operator.update_document(**kwargs)

def delete_document(
    database_type: Database_Type,
    **kwargs
) -> list:

    '''
        Wrapper of database strategy and call corresponding funcion
    '''

    db_operator = set_database_type(database_type=database_type)
    return db_operator.delete_document(**kwargs)
