from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


from . import views  # noqa
from . import models  # noqa
