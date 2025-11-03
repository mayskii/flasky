from flask import Response, abort, make_response, Blueprint, request
from ..models.cat import Cat
from ..db import db
from .routes_utilities import validate_model

bp = Blueprint("cat_bp", __name__, url_prefix="/cats")

@bp.post("")
def create_cat():
    request_body = request.get_json()

    # name = request_body["name"]
    # color = request_body["color"]
    # personality = request_body["personality"]

    # new_cat = Cat(
    #     name=name,
    #     color=color,
    #     personality=personality
    # )

    try:
        new_cat = Cat.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_cat)
    db.session.commit()

    return new_cat.to_dict(), 201


@bp.get("")
def get_all_cats():

    query = db.select(Cat)

    name_param = request.args.get("name") # request.args.get("name") or request.args.get["name"]
    if name_param:
        query = query.where(Cat.name == name_param).order_by(Cat.id)

    color_param = request.args.get("color")
    if color_param:
        query = query.where(Cat.color.ilike(f"%{color_param}%")).order_by(Cat.id)

    cats = db.session.scalars(query)  # get back data from data
    result_list = []

    for cat in cats:
        result_list.append(cat.to_dict())

    return result_list


@bp.get("/<int:id>")
def get_some_cat(id):
    cat = validate_model(id)

    return cat.to_dict(), 200


@bp.put("/<id>")
def replace_cat(id):
    cat = validate_model(id)

    request_body = request.get_json()
    cat.name = request_body["name"]
    cat.color = request_body["color"]
    cat.personality = request_body["personality"]

    db.session.commit()

    # return "", 204
    return Response(status=204, mimetype="application/json")

@bp.delete("/<id>")
def delete_cat(id):
    cat = validate_model(id)
    db.session.delete(cat)
    db.session.commit()
    
    # return "", 204
    return Response(status=204, mimetype="application/json")