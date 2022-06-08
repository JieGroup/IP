from __future__ import annotations

from abc import ABC, abstractmethod

class AbstractDatabase(ABC):

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

    