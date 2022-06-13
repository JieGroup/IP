from __future__ import annotations

import json
import copy
import numpy as np

from app._typing import Serializable_Datatype

from typing import (
    Any
)

from app.utils.dtypes.api import (
    is_numpy,
    is_dict_like,
    is_list,
    is_set
)


class Serialization:

    '''
    Serialize data, mainly deal with the object that cant be serialized.
    Ex. set

    Attributes
    ----------
    None

    Methods
    -------
    make_data_serializable
    '''
    
    @classmethod
    def __is_serializable(
        cls,
        data: Any
    ) -> bool:

        '''
        Check if data is serializable

        Parameters
        ----------
        data : Any
            Can be any form

        Returns
        -------
        bool
        '''

        try:
            json.dumps(data)
        except:
            return False
        else:
            return True

    @classmethod
    def __change_datatype_to_serializable(
        cls,
        data: Any
    ) -> Serializable_Datatype:

        '''
        Turn the unserializable data to serializable data

        Parameters
        ----------
        data : Any
            Can be any form

        Returns
        -------
        Serializable_Datatype
        '''

        if is_numpy(data):
            return copy.deepcopy(data.tolist())
        elif is_set(data):
            return copy.deepcopy(list(data))
        
        return data

    @classmethod
    def make_data_serializable(
        cls,
        data: Any
    ) -> Serializable_Datatype:

        '''
        Use recursion to make_data_serializable 

        Parameters
        ----------
        data : Any
            Can be any form

        Returns
        -------
        Serializable_Datatype
        '''

        if data is None:
            return None

        if cls.__is_serializable(data) and not is_dict_like(data):
            return copy.deepcopy(data)
        
        if is_dict_like(data):
            processed_data = {}
            for key, value in data.items():
                processed_data[key] = cls.make_data_serializable(value)   
            return processed_data 
        else:
            return cls.__change_datatype_to_serializable(data)
