from ..ma import ma
from ..models.comentarios import Comentarios

class ComentariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comentarios
        datetimeformat = '%d/%m/%Y'        
        load_instance = True