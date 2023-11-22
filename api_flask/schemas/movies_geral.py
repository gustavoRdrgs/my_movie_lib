from ..ma import ma
from ..models.movies_geral import MoviesGeral

class MoviesGeralSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MoviesGeral
        datetimeformat = '%d/%m/%Y'        
        load_instance = True