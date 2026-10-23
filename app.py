from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel 
from con_sql_alchemy import bd 
from resources.user import User, UserRegistar


app =Flask(__name__)



#configurações 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hoteis.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:hotel_id>")
api.add_resource(User,"/users/<string:username>")
api.add_resource(UserRegistar,"/registar")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all() #Cria todas as tabelas defininas no modelo do sqlalchemy
    app.run(debug=True)
