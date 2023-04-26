from flask import Flask
from config import Config
from content.blueprint import content

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(content, url_prefix='/content')
# localhost:5050/content
