from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractDatabaseStrategy(ABC):
    '''
    Abstract class for database strategy class.
    This is where our DatabaseOperator can override
    '''
    @abstractmethod
    def set_database(self, **kwargs) -> None:
        pass
    
    @abstractmethod
    def get_all_documents(self, **kwargs):
        pass
    
    @abstractmethod
    def search_document(self, **kwargs):
        pass
    
    @abstractmethod
    def create_document(self, **kwargs):
        pass

    @abstractmethod
    def update_document(self, **kwargs):
        pass
    
    @abstractmethod
    def delete_document(self, **kwargs):
        pass