from app import create_app, db
from app.models.cat import Cat

my_app = create_app()

with my_app.app_context():
    cats = [
        Cat(name="Shadow", color="Black", personality="Mysterious night hunter"),
        Cat(name="Mila", color="Gray", personality="Playful and curious"),
        Cat(name="Cleo", color="Calico", personality="Elegant and dramatic"),
        Cat(name="Oreo", color="Black and White", personality="Always hungry"),
        Cat(name="Toby", color="Orange", personality="Chaotic good")
    ]

    db.session.add_all(cats)
    db.session.commit()