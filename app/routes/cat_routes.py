from flask import Response, abort, make_response, Blueprint, request
from ..models.cat import Cat
from ..db import db

cats_bp = Blueprint("cat_bp", __name__, url_prefix="/cats")

@cats_bp.post("")
def create_cat():
    request_body = request.get_json()
    name = request_body["name"]
    color = request_body["color"]
    personality = request_body["personality"]

    new_cat = Cat(
        name=name,
        color=color,
        personality=personality
    )

    db.session.add(new_cat)
    db.session.commit()

    cat_response = dict(
        id=new_cat.id,
        name=new_cat.name,
        color=new_cat.color,
        personality=new_cat.personality
    )

    return cat_response, 200


@cats_bp.get("")
def get_all_cats():
    query = db.select(Cat).order_by(Cat.id)
    cats = db.session.scalars(query)
    result_list = []

    for cat in cats:
        result_list.append({
            "id": cat.id,
            "name": cat.name,
            "color": cat.color,
            "personality": cat.personality
        })

    return result_list

@cats_bp.get("/<int:id>")
def get_some_cat(id):
    cat = validate_cat(id)

    result = {
        "id": cat.id,
        "name": cat.name,
        "color": cat.color,
        "personality": cat.personality
    }
    return result, 200

@cats_bp.put("/<id>")
def replace_cat(id):
    cat = validate_cat(id)

    request_body = request.get_json()
    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]

    db.session.commit()

    return "", 204

@cats_bp.delete("/<id>")
def delete_cat(id):
    cat = validate_cat(id)
    db.session.delete(cat)
    db.session.commit()
    
    return "", 204


        
def validate_cat(id):
    try:
        id = int(id)
    except ValueError:
        invalid = {"message": f"Cat id ({id}) is invalid."}
        abort(make_response(invalid, 400))

    query = db.select(Cat).where(Cat.id == id)
    cat = db.session.scalar(query)

    if not cat:
        not_found = {"message": f"Cat with id ({id}) not found"}
        abort(make_response(not_found, 404))
    
    return cat