from __future__ import annotations

import sys
import bson

from typing import Any

from app._typing import Serializable_Datatype


# def encode_file_to_BSON_file(
#     file: dict[str, Any]
# ) -> type[bson]:

#     '''
#         Encode Dict to bson file, which is the mongoDB 
#         storage type
#     '''

#     if isinstance(file, bson.BSON):
#         return file
#     return bson.BSON.encode({'file': file})

# def decode_BSON_file_to_file(
#     BSON_file: type[bson]
# ) -> dict[str, Any]:

#     '''
#         Decode bson to dict type and return
#     '''
    
#     if not isinstance(BSON_file, bson.BSON):
#         return BSON_file
#     return bson.BSON(BSON_file).decode()

# def is_file_size_exceed_limit(
#     file: dict[str, Any]
# ) -> bool:

#     '''
#         Check size of file.
#         If size surpasses the limit, return False. Otherwise, True
#     '''

#     BSON_file = encode_file_to_BSON_file(file)
#     if sys.getsizeof(BSON_file) > 16000000:
#         return False
#     return True