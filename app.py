from flask import Flask
from config import Config
from content.blueprint import content
from content.blueprint import static

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(content, url_prefix='/content')
# localhost:5050/content

app.register_blueprint(static, url_prefix='/static')
# localhost:5050/static
