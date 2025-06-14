import logging
from    database import db_session
from jeec_app.models.characters import Characters
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class CreateCharacterService:
    def __init__(self, kwargs: Dict):
        self.kwargs = kwargs

    def call(self) -> Optional[Characters]:
        try:
            character = Characters(**self.kwargs)  
            db_session.add(character) 
            db_session.commit()  
            return character
        except Exception as e:
            db_session.rollback()                               # Em caso de erro, reverte
            logger.error(f"Error creating character: {e}")
            return None