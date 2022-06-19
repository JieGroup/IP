from __future__ import annotations

from app import pyMongo

from app.database.database.base import BaseDatabase

from app.database.database.abstract_database import AbstractDatabase

from typeguard import typechecked

from typing import Any

@typechecked
class SurveySummary(AbstractDatabase, BaseDatabase):
    '''
    SurveySummary is not needed for now

    Attributes
    ----------
    None

    Methods
    -------
    get_all_documents_count
    get_all_documents
    search_document
    create_document
    update_document
    delete_document
    '''

    @classmethod
    def get_all_documents_count(cls) -> int:

        pass

    @classmethod
    def get_all_documents(cls) -> list[dict[str, Any]]:

        pass

    @classmethod
    def search_document(
        cls
    ) -> None:

        pass

    @classmethod
    def create_document(
        cls
    ) -> None:

        pass
    
    @classmethod
    def update_document(
        cls
    ) -> None:

        pass
    
    @classmethod
    def delete_document(
        cls
    ) -> None:

        pass