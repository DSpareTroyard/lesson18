from flask_restx import Resource, Namespace
from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        if not genre_service.get_one(gid):
            return "", 404
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre)
