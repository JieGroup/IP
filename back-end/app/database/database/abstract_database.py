from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractDatabase(ABC):
    '''
    Abstract class for database class.
    This is where our database class can override
    '''
    @classmethod
    @abstractmethod
    def get_all_documents_count(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def get_all_documents(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def search_document(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def create_document(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def update_document(cls, **kwargs):
        pass
    
    @classmethod
    @abstractmethod
    def delete_document(cls, **kwargs):
        pass

    