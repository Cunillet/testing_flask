"""import sqlite3

conn = sqlite3.connect('people.db')
cur = conn.cursor()
cur.execute('SELECT * FROM person ORDER BY lname')
people = cur.fetchall()
for person in people:
    print(f'{person[2]} {person[1]}')


# version 2

from models import Person

people = Person.query.order_by(Person.lname).all()
for person in people:
    print(f'{person.fname} {person.lname}')
"""
from flask import render_template
import connexion
from config import connex_app

# Create the application instance
#app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yml', arguments={'api_local': 'local_value'}, options={"swagger_ui": True})

# Create a URL route in our application for "/"
@connex_app.route('/')
def home():
	"""
	This function just responds to the browser ULR
	localhost:5000/
	:return:        the rendered template 'home.html'
	"""
	return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
	connex_app.run(host='0.0.0.0', port=5000, debug=True)