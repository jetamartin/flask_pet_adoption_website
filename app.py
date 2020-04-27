from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm
from forms import EditPetForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "my-secret-word"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///pet_adoption'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def homepage():
    """Show listing of all pets"""
    pets = Pet.query.all()
    return render_template("index.html", pets = pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Display Form to add a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data.strip().capitalize()
        species = form.species.data.strip().capitalize()
  
        photo_url = form.photo_url.data if form.photo_url.data else None
        age = form.age.data
        notes = form.notes.data.strip()
        flash(f"Added {name} the {species} as a new pet", "success-msg")
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")

    else:
        return render_template("add_pet.html", form=form)

@app.route("/<int:pet_id>/edit", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Display Pet detail page with form to edit some info on Pets."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj = pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data.strip()
        pet.available = form.available.data
        flash(f"Updated '{pet.name}' the {pet.species}'s profile", 'success-msg')
        db.session.add(pet)
        db.session.commit()
        # import pdb; pdb.set_trace()
        return redirect("/")

    else:
        return render_template("edit_pet.html", form=form, pet=pet)
