from flask import request
from flask_restx import Resource, Namespace
from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if request.args.get('director_id'):
            did = request.args.get('director_id')
            movies = movie_service.get_by_director_id(did)
        elif request.args.get('genre_id'):
            gid = request.args.get('genre_id')
            movies = movie_service.get_by_genre_id(gid)
        elif request.args.get('year'):
            y = request.args.get('year')
            movies = movie_service.get_by_year(y)
        else:
            movies = movie_service.get_all()
        return movies_schema.dump(movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        if not movie_service.get_one(mid):
            return "", 404
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        if not movie_service.get_one(mid):
            return "", 404
        req_json = request.json
        req_json['id'] = mid
        movie_service.update(req_json)
        return "", 204

    def patch(self, mid):
        if not movie_service.get_one(mid):
            return "", 404
        req_json = request.json
        req_json['id'] = mid
        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, mid):
        if not movie_service.get_one(mid):
            return "", 404
        movie_service.delete(mid)
        return "", 204
