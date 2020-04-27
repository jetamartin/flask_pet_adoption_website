from app import db
from models import Pet

db.drop_all()
db.create_all()

Pet.query.delete()

pet1 = Pet(name="Bacon", species = "pig", age=3, available = True,
          photo_url = "https://images.unsplash.com/photo-1516467508483-a7212febe31a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1952&q=80", 
          notes = "Bacon is a sweet adorable pig. He loves to eat")

pet2 = Pet(name="Monty", species = "snake", age=4, available = True,
          photo_url = "https://images.unsplash.com/photo-1585095595274-aeffce35511a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80", 
          notes = "Monty  is a Ball pythons. He eats two mice per week")

pet3 = Pet(name="Templeton", species = "rat", age=1, available = True,
          photo_url = "https://images.unsplash.com/photo-1550697851-920b181d8ca8?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80", 
          notes = "Templeton loves his cheese and lots of attention")

pet4 = Pet(name="Blanca", species = "cat", age=4, available = True,
          photo_url = "https://images.unsplash.com/photo-1573148164257-8a2b173be464?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80", 
          notes = "Blanca is a sweet kitty who loves chest and chin rubs")

pet5 = Pet(name="Ruffy", species = "dog", age=1.5, available = True,
          photo_url = "https://images.unsplash.com/photo-1502673530728-f79b4cab31b1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80", 
          notes = "Ruffy is well trained. He's a snuggler")

pet6 = Pet(name="Garth", species = "Guinea Pig", age=1, available = True,
          photo_url = "https://animals.sandiegozoo.org/sites/default/files/2019-04/animals_guineapig-domestic.jpg", 
          notes = "Garth is chubby little Guinea Pig who loves his kibbles ")


db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6])
db.session.commit()
