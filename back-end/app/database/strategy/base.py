from __future__ import annotations

from typing import (
    final,
    Any
)


class BaseDatabaseStrategy:
    '''
    Base class for database strategy

    Attributes
    ----------
    None

    Methods
    -------
    None
    '''
    @final
    def placeholder(self, **kwargs):
        pass

    @final
    @classmethod
    def check_search_document_response(
        cls,
        res: Any
    ) -> None:
        '''
        Check if searched document is None

        Parameters
        ----------
        res : Any

        Returns
        -------
        None
        '''
        if not res:
            raise ValueError('Cannot find the document')
        return
    
    @final
    @classmethod
    def check_create_document_response(
        cls,
        res: Any
    ) -> None:
        '''
        Check if create document has been 
        sucessfully done

        Parameters
        ----------
        res : Any

        Returns
        -------
        None
        '''
        if not res:
            raise ValueError('Cannot create the document')
        elif not res.inserted_id:
            raise ValueError('Cannot create the document')
        return
    
    @final
    @classmethod
    def check_update_document_response(
        cls,
        res: Any
    ) -> None:
        '''
        If we update a specific record in the DB and
        the modified_count or matched_count is 0.
        We shall raise an error.

        Parameters
        ----------
        res : Any

        Return
        -------
        None
        '''
        if not res:
            raise ValueError('Cannot update the document')
        elif res.modified_count == 0:
            raise ValueError('Cannot update the document')
        elif res.matched_count == 0:
            raise ValueError('Cannot find the document')
        return

    @final
    @classmethod
    def check_delete_document_response(
        cls,
        res: Any
    ) -> None:
        '''
        If we delete a specific record in the DB and
        the deleted_count is 0.
        We shall raise an error.

        Parameters
        ----------
        res : Any

        Return
        -------
        None
        '''
        if not res:
            raise ValueError('Cannot delete the document')
        elif res.deleted_count == 0:
            raise ValueError('Cannot delete the document')
        return