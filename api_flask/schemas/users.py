from ..ma import ma
from ..models.users import Users

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        datetimeformat = '%d/%m/%Y'        
        load_instance = True