from flask import abort, make_response
from ..db import db

def validate_model(cls, id):

    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"{cls.__name__} id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    query = db.select(cls).where(cls.id == id)
    model = db.session.scalar(query)

    if not model:
        not_found = {"message": f"{cls.__name__} with id ({id}) not found"}
        abort(make_response(not_found, 404))
    
    return model