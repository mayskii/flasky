from flask import abort, make_response, Blueprint, request
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


# @cats_bp.get("")
# def get_all_cats():
#     result_list = []

#     # for cat in cats:
#     #     result_list.append(dict(
#     #         id=cat.id,
#     #         name=cat.name,
#     #         color=cat.color,
#     #         personality=cat.personality
#     #     ))

#     # return result_list

#     for cat in cats:
#         result_list.append({
#             "id": cat.id,
#             "name": cat.name,
#             "color": cat.color,
#             "personality": cat.personality
#         })

#     return result_list

# @cats_bp.get("/<id>")
# def get_some_cats(id):
    
#     cat = validate_cat(id)

#     cat_dict =  dict(
#         id=cat.id,
#         name=cat.name,
#         color=cat.color,
#         personality=cat.personality
#         )
        
#     return cat_dict
    
        
# def validate_cat(id):
#     try:
#         id = int(id)
#     except ValueError:
#         invalid = {"message": f"cat id ({id}) is invalid."}
#         abort(make_response(invalid, 400))

#     for cat in cats:
#             if cat.id == id:
#                 return cat
            
#     not_found = {"message": f"Cat with id ({id}) not found"}
#     abort(make_response(not_found, 404))