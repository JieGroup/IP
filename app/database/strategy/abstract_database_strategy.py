from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractDatabaseStrategy(ABC):

    @classmethod
    @abstractmethod
    def get_instance(cls):
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