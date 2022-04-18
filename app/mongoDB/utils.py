import sys
import bson
from gridfs import GridFS
from io import BytesIO

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
        return True, BSON_file
    return False, None
    
    # @classmethod
    # def store_large_file(cls, BSON_file, filename='None'):
    #     if not isinstance(BSON_file, bson.BSON):
    #         BSON_file = cls.encode_file_to_BSON_file(BSON_file)

    #     print('hhhh', type(BSON_file))
    #     fileobj = BytesIO(BSON_file)
    #     file_id = pyMongo.save_file(filename=filename, fileobj=fileobj, base='fs')
    #     return file_id

    # @classmethod
    # def retrieve_large_file(cls, base='fs', file_id=None, filename=None):
    #     gridfs = GridFS(pyMongo.db, base)
    #     if filename:
    #         gridfile = gridfs.find_one({"filename": filename})
    #     elif file_id:
    #         gridfile = gridfs.find_one({"_id": file_id})
    #     else:
    #         return False
        
    #     return bson.BSON(gridfile.read()).decode()['file']

    # @classmethod
    # def delete_large_file(cls, file_id, base='fs'):
    #     gridfs = GridFS(pyMongo.db, base)
    #     gridfile = gridfs.delete({"_id": file_id})
    #     return gridfile