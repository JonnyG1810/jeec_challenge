from jeec_app.models.characters import Characters

class CharactersFinder:
    @classmethod
    def get_from_id(cls, id):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(id=id).first()
            return result
        finally:
            session.close()

    @classmethod
    def get_by_name(cls, name):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(Characters.name.ilike(f"%{name}%")).all()
            return result
        finally:
            session.close()
        
    @classmethod
    def get_by_age(cls, age):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(Characters.age == age).all()
            return result
        finally:
            session.close()


    @classmethod
    def get_alive(cls):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(Characters.is_alive == True).all()
            return result
        finally:
            session.close()

    @classmethod
    def get_by_species(cls, species):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(Characters.species == species).all()
            return result
        finally:
            session.close()
    
    @classmethod
    def get_by_series(cls, series):
        query, session = Characters.get_query()
        try:
            result = query.filter_by(Characters.series == series).all()
            return result
        finally:
            session.close()
            
    @classmethod
    def get_all(cls):
        query, session = Characters.get_query()
        try:
            return query.order_by(Characters.id).all()
        finally:
            session.close()



