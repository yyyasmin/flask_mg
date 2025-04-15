#!flask/bin/python

from app import create_app
from app.models import *
import os

app = create_app()
           
if __name__ == "__main__":
	app.run(debug=True, port=os.getenv("PORT", default=5000))
