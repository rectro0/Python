from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Message = db.Column(db.String(500), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "Email": self.Email,
            "Message": self.Message
        }
