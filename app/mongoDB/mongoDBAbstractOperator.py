from abc import ABC, abstractmethod

class mongoDBAbstractOperator(ABC):

    @classmethod
    @abstractmethod
    def document_count(cls, *args):
        pass
    
    @classmethod
    @abstractmethod
    def search_document(cls, *args):
        pass

    @classmethod
    @abstractmethod
    def create_document(cls, *args):
        pass
    
    @classmethod
    @abstractmethod
    def update_document(cls, *args):
        pass
    
    @classmethod
    @abstractmethod
    def delete_document(cls, *args):
        pass

    