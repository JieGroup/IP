from __future__ import annotations

import sys
import bson

def encode_file_to_BSON_file(file):
    if isinstance(file, bson.BSON):
        return file
    return bson.BSON.encode({'file': file})

def decode_BSON_file_to_file(BSON_file):
    if not isinstance(BSON_file, bson.BSON):
        return BSON_file
    return bson.BSON(BSON_file).decode()

def if_file_size_exceed_limit(file):
    BSON_file = encode_file_to_BSON_file(file)
    # check size of file.
    # if size surpasses the limit, return False and BSON_file
    if sys.getsizeof(BSON_file) > 16000000:
        return BSON_file
    raise