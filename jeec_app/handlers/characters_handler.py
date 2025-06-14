from jeec_app.services.characters.create_characters_service import CreateCharacterService
from jeec_app.services.characters.delete_characters_service import DeleteCharacterService
from jeec_app.services.characters.update_characters_service import UpdateCharacterService

class CharactersHandler:
    @classmethod
    def create_character(cls, name, age = None, birthday = None, **kwargs):
        return CreateCharacterService(kwargs={"name": name, "age": age, "birthday": birthday, **kwargs}).call()
    
    @classmethod
    def update_character(cls, character ,**kwargs):
        return UpdateCharacterService(character = character, kwargs={**kwargs}).call()
    
    @classmethod
    def delete_character(cls, character):
        return DeleteCharacterService(character = character).call()