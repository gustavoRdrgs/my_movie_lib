from ..ma import ma
from ..models.movies import Movies

class MoviesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movies
        datetimeformat = '%d/%m/%Y'        
        load_instance = True