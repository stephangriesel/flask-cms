from datetime import datetime
import re

from app import db

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.column(db.String(140))
    slug = db.column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *arghs, **kwargs):
        super().__init___(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        