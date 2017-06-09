from src import db

class Tasks(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, title, description, done):
        self.title = title
        self.description = description
        self.done = done

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            # This is an example how to deal with Many2Many relations
            'done': self.done
        }