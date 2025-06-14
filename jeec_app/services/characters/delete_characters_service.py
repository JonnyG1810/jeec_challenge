from jeec_app.models.characters import Characters

class DeleteCharacterService:
    def __init__(self, character: Characters):
        self.character = character

    def call(self) -> bool:
        try:
            db_session.delete(self.character)
            db_session.commit()
            return True
        except Exception as e:
            db_session.rollback()
            return False