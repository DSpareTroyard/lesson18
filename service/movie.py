from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_by_director_id(self, did):
        return self.dao.get_by_director_id(did)

    def get_by_genre_id(self, gid):
        return self.dao.get_by_genre_id(gid)

    def get_by_year(self, y):
        return self.dao.get_by_year(y)

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        movie.genre = data.get("genre")
        movie.director = data.get("director")

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get("id")
        movie = self.get_one(mid)
        if "title" in data:
            movie.title = data.get("title")
        if "description" in data:
            movie.description = data.get("description")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "year" in data:
            movie.year = data.get("year")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "director_id" in data:
            movie.director_id = data.get("director_id")
        if "genre" in data:
            movie.genre = data.get("genre")
        if "director" in data:
            movie.director = data.get("director")

        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)
