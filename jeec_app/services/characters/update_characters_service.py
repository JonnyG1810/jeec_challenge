from typing import Dict, Optional
from jeec_app.models.characters import Characters

class UpdateCharacterService:
    def __init__(self, character: Characters, kwargs: Dict):
        self.character = character
        self.kwargs = kwargs

    def call(self) -> Optional[Characters]:
        try:
            for key, value in self.kwargs.items():
                setattr(self.character, key, value)  
            db_session.commit()
            return self.character
        except Exception as e:
            db_session.rollback()
            return None