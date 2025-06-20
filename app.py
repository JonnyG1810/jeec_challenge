from flask import Flask, jsonify, request  # Adicionado request
from database import engine, Base, db_session
from jeec_app.handlers.characters_handler import CharactersHandler  # Corrigido nome
from jeec_app.finders.characters_finder import CharactersFinder
from jeec_app.models.characters import Characters  # Nome correto do modelo
import os
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Cria tabelas
    Base.metadata.create_all(bind=engine)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    # Rotas para Character (4.2)
    @app.route("/character/add", methods=["POST"])
    def add_character():
        data = request.get_json()
        character = CharactersHandler.create_character(
            name=data['name'],
            age=data.get('age'),
            is_alive=data.get('is_alive', True)
        )
        if character:
            return jsonify({"id": character.id, "name": character.name}), 201
        return jsonify({"error": "Failed to create character"}), 400

    @app.route("/characters", methods=["GET"])
    def get_characters():
        characters = CharactersFinder.get_all()
        return jsonify([{
            "id": c.id,
            "name": c.name,
            "age": c.age,
            "is_alive": c.is_alive
        } for c in characters])

    @app.route("/character/<int:id>", methods=["GET"])
    def get_character(id):
        character = CharactersFinder.get_from_id(id)
        if character:
            return jsonify({
                "id": character.id,
                "name": character.name,
                "age": character.age,
                "is_alive": character.is_alive
            })
        return jsonify({"error": "Character not found"}), 404
        
    @app.route("/character/remove/<int:id>", methods=["POST"])  # DELETE single id
    def remove_character(id):
        character = CharactersFinder.get_from_id(id)
        if character:
            success = CharactersHandler.delete_character(character)
            if success:
                return jsonify({"message": f"Character {id} removed successfully"}), 200
            return jsonify({"error": "Failed to delete character"}), 500
        return jsonify({"error": "Character not found"}), 404
    
    @app.route("/character/delete_all", methods=["POST"])  #DELETE all elements of the table
    def delete_all():
        try:
            db_session.query(Characters).delete()
            db_session.commit()
            return jsonify({"message": "All characters deleted"}), 200
        except Exception as e:
            db_session.rollback()
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
