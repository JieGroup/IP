from app._typing import Database_Type

from typing import Union

from typeguard import typechecked

from pymongo.results import (
    InsertOneResult,
    UpdateResult,
    DeleteResult
)

from pymongo.cursor import Cursor

from app.database.strategy.api import DatabaseOperator


@typechecked
def set_database_type(
    database_type: Database_Type
) -> DatabaseOperator:
    '''
    Set database strategy
    '''
    db_operator = DatabaseOperator()
    db_operator.set_database(database_type=database_type)
    return db_operator

@typechecked
def get_all_documents_count(
    database_type: Database_Type,
    **kwargs
) -> int:  
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.get_all_documents_count(**kwargs)

@typechecked
def get_all_documents(
    database_type: Database_Type,
    **kwargs
) -> Cursor:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.get_all_documents(**kwargs)
    
@typechecked
def search_document(
    database_type: Database_Type,
    **kwargs
) -> Union[None, dict]:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.search_document(**kwargs)

@typechecked
def search_multiple_documents(
    database_type: Database_Type,
    **kwargs
) -> Cursor:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.search_multiple_documents(**kwargs)

@typechecked
def create_document(
    database_type: Database_Type,
    **kwargs
) -> InsertOneResult:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.create_document(**kwargs)

@typechecked
def update_document(
    database_type: Database_Type,
    **kwargs
) -> UpdateResult:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.update_document(**kwargs)

@typechecked
def delete_document(
    database_type: Database_Type,
    **kwargs
) -> DeleteResult:
    '''
    Wrapper of database strategy and call corresponding funcion
    '''
    db_operator = set_database_type(database_type=database_type)
    return db_operator.delete_document(**kwargs)
