# """Forms for our demo Flask app."""

from flask_wtf import FlaskForm
from wtforms.widgets.html5 import URLInput, Input
# from wtforms.widgets.html5 import URLInput, Input

from wtforms import StringField, FloatField, TextAreaField, Field,  BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, Regexp, NumberRange, AnyOf, URL


class AddPetForm(FlaskForm):
    """Form for adding a new Pet."""

    name = StringField("Name:", 
              validators=[
                  InputRequired("Pet name can't be blank")],
              render_kw={"placeholder": "Enter your pet's name"}    
                  )


    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("snake", "Snake"), ("guinea pig", "Guinea Pig"), ("pig", "Pig"), ("mouse", "Mouse")],
        render_kw={"placeholder": "test"}
    )

    photo_url = StringField('Photo_URL:', 
        validators = [
          Optional(),
          URL('URL must be a valid link')],
          render_kw={"placeholder": "Enter URL for pet's picture (e.g., https://..)"}  
          )  
#        Regexp('^(http|https):\/\/[\w.\-]+(\.[\w.\-]+)+.*$', 0,
              #  'URL must be a valid link')])

    age = FloatField("Age:", 
          validators = [NumberRange(min=0, max=30, message="Pet's age can only be between 0 and 30")],
          render_kw={"placeholder": "Enter your pets age in years (e.g., 1 or 1.5 etc)"}
          )

    notes = TextAreaField("Notes:",
            render_kw={"placeholder": "Enter any notes you thing are pertinent"}
          )

    

class EditPetForm(FlaskForm):
  """ Form for editing subset of fields for a pet """

  photo_url = StringField('Photo_URL:', 
    validators = [
      Optional(),
      URL('URL must be a valid link')]) 

  notes = TextAreaField("Notes:")

  available = BooleanField("Available?")

