from flask import Flask
from flask_restful import Api
from data import db_session, users_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/mars_explorer2.db")
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:users_id>')
    app.run()


if __name__ == '__main__':
    main()