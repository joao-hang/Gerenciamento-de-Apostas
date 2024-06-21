from flask import Flask
from flask_restful import Api
from config import Base, engine
from controllers import UsuarioResource, UsuarioListResource

app = Flask(__name__)
api = Api(app)

Base.metadata.create_all(engine)

api.add_resource(UsuarioListResource, '/usuarios')
api.add_resource(UsuarioResource, '/usuarios/<int:usuario_id>')

if __name__ == '__main__':
    app.run(debug=True)
