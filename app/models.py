from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    completada = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "completada": self.completada
        }