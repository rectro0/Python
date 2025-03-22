from flask import request, jsonify
from config import db, app
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        json_contacts = list(map(lambda x: x.to_json(), contacts))
        return jsonify({"contacts": json_contacts})
    except Exception as e:
        print(f"Error fetching contacts: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

@app.route("/create_contacts", methods=["POST"])
def create_contacts():
    try:
        Name = request.json.get("Name")
        Email = request.json.get("Email")
        Message = request.json.get("Message")

        if not Name or not Email or not Message:
            return jsonify({"message": "You must include a Name, Email, and Message"}), 400

        new_contact = Contact(Name=Name, Email=Email, Message=Message)
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "User Created!"}), 201
    except Exception as e:
        print(f"Error creating contact: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

@app.route("/update_contacts/<int:user_id>", methods=["PATCH"])
def update_contacts(user_id):
    try:
        contact = Contact.query.get(user_id)

        if not contact:
            return jsonify({"message": "User not found!"}), 404

        data = request.json
        contact.Name = data.get("Name", contact.Name)
        contact.Email = data.get("Email", contact.Email)
        contact.Message = data.get("Message", contact.Message)

        db.session.commit()
        return jsonify({"message": "User updated."}), 200
    except Exception as e:
        print(f"Error updating contact: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

@app.route("/delete_contacts/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    try:
        contact = Contact.query.get(user_id)

        if not contact:
            return jsonify({"message": "User not found!"}), 404

        db.session.delete(contact)
        db.session.commit()
        return jsonify({"message": "User deleted!"}), 200
    except Exception as e:
        print(f"Error deleting contact: {e}")
        return jsonify({"message": "Internal Server Error"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)