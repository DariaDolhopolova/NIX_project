"""DB core module"""


from film_proj import db
from film_proj.models_file import Films
from film_proj.models_file import Directors
from film_proj.models_file import Genres
from film_proj.models_file import Users
from film_proj.models_file import UserGroups
from film_proj.models_file import films_directors
from film_proj.models_file import films_genres


def get_user_id(username: str):
    """Gives user id from users.id by username from users.username"""
    if not isinstance(username, str):
        raise TypeError('Username type should be str.')

    user_id = Users.query.filter_by(username=username).first()

    if user_id is None:
        return user_id
    return user_id.id


def get_user_username(user_id: int):
    """Gives username from users.username by user id from users.id"""
    if not isinstance(user_id, int):
        raise TypeError('User id type should be int.')

    user_name = Users.query.get(user_id)
    return user_name.username


def get_user_full_name(user_id: int):
    """Gives user full name from users.first_name and user.last_name
     by user id from users.id"""
    if not isinstance(user_id, int):
        raise TypeError('User id type should be int.')

    user_name = Users.query.get(user_id)
    return f'{user_name.first_name} {user_name.last_name}'


def get_user_auth(user_id: int):
    """Returns authorization parameters for flask-login"""
    if not isinstance(user_id, int):
        raise TypeError('User id type should be int.')

    user = Users.query.get(user_id)

    return user.username, user.password


def get_user_password(user_id:int):
    """Returns user password by user id"""
    if not isinstance(user_id, int):
        raise TypeError('User id type should be int.')
    user_pw = Users.get(user_id)

    return user_pw.password


def add_new_user(username: str, first_name: str, last_name: str,
                 password: str, user_group_id: int = 1):
    """Add new user:
    username: str - min len=3, max=20
    first_name: str - min len=3, max=20
    last_name: str - min len=3, max=20
    password: str - min len=8, max=30
    user_group_id - 1-user, 2-admin

    output: user id of new user"""

    if not isinstance(username, str):
        raise TypeError('Username type should be str.')
    if not isinstance(first_name, str):
        raise TypeError('First name type should be str.')
    if not isinstance(last_name, str):
        raise TypeError('Last name type should be str.')
    if not isinstance(password, str):
        raise TypeError('Password should contain letters and numbers.')
    if not isinstance(user_group_id, int):
        raise TypeError('User group id should be int')
    if not 1 <= user_group_id <= 2:
        raise ValueError('User group id should be 1 for user or 2 for admin.')
    if not 3 <= len(username) <= 20:
        raise ValueError('Username length must be between 3 and 20')
    if not 3 <= len(first_name) <= 20:
        raise ValueError('First name length must be between 3 and 20')
    if not 3 <= len(last_name) <= 20:
        raise ValueError('Last name length must be between 3 and 20')
    if not 8 <= len(password) <= 30:
        raise ValueError('Password length must be between 8 and 30')

    try:
        if get_user_id(username=username) is not None:
            return f'Username {username} is already taken.'
        new_user = Users(username=username, first_name=first_name,
                         last_name=last_name, password=password, user_group_id=user_group_id)
        db.session.add(new_user)
        db.session.commit()
        user_id = get_user_id(username=username)
        return user_id
    except Exception as error:
        print(error)
        return 'Something went wrong'


def get_user_group_name(user_group_id: int):
    """get user group name by user group id"""
    if not isinstance(user_group_id, int):
        raise TypeError('User group id type should be int')
    user_group = UserGroups.query.get(user_group_id)
    if user_group is None:
        return user_group
    return user_group.user_group_name


def get_user_group_id(user_group_name: str):
    """get user group id by user group name"""
    if not isinstance(user_group_name, str):
        raise TypeError('User group name type should be str')
    user_group = UserGroups.query.get(user_group_name)
    if user_group is None:
        return user_group
    return user_group.user_group_id


def add_new_user_group(user_group_name: str):
    """Add new user group
    input: user_group_name - str
    output: user_group_id"""

    if not isinstance(user_group_name, str):
        raise TypeError('User group name should be str')

    try:
        if get_user_group_id(user_group_name=user_group_name) is not None:
            return 'This user group is already added'
        new_user_group = UserGroups(user_group_name=user_group_name)
        db.session.add(new_user_group)
        db.session.commit()
        user_group_id = get_user_group_id(user_group_name=user_group_name)
        return user_group_id
    except Exception as error:
        print(error)
    finally:
        return 'Something went wrong'


def get_genre(genre_name: str = None, genre_id: int = None):
    """input:
    genre_name or genre_id
    output:
    genre_id or genre_name"""

    if genre_name is not None:
        if not isinstance(genre_name, str):
            raise TypeError('Genre name type should be str')

        genre_id = Genres.query.filter_by(genre_name=str(genre_name)).first()

        if genre_id is None:
            return genre_id

        return genre_id

    if genre_id is not None:
        if not isinstance(genre_id, int):
            raise TypeError("Genre id should be int.")

        genre = Genres.get(genre_id)

        return str(genre.genre_name)


def add_new_genre(genre_name: str):
    """Add new genre
    input: genre_name - str
    output: genre_id"""

    if not isinstance(genre_name, str):
        raise TypeError('Genre name should be str')

    try:
        if get_genre(genre_name=genre_name) is not None:
            return 'This genre is already added'
        new_genre = Genres(genre_name=genre_name)
        db.session.add(new_genre)
        db.session.commit()
        genre_id = get_genre(genre_name=genre_name)
        return genre_id
    except Exception as error:
        print(error)
    finally:
        return 'Something went wrong'


def get_director(director_full_name: str = None,
                 director_id: int = None):
    """input: director_full_name  or director_id
    output: any combination of these parameters which is missing """

    if director_full_name is not None:
        if not isinstance(director_full_name, str):
            raise TypeError('Name type should be str')
        dir_id = Directors.query.filter_by(director_full_name=director_full_name).first()

        return dir_id.director_id

    if director_id is not None:
        if not isinstance(director_id, int):
            raise TypeError(f'director_id type must be int ')
        dir_id = Directors.get(director_id)
        return str(dir_id.director_full_name)


def add_new_director(director_full_name: str):
    """Add new director
    input: director full name - str
    output: director id - int"""
    if not isinstance(director_full_name, str):
        return 'Director name should be type str>'

    try:
        if get_director(director_full_name) is not None:
            return 'This director already exists'

        new_dir = Directors(director_full_name=director_full_name)
        db.session.add(new_dir)
        db.session.commit()

        dir_id = get_director(director_full_name=director_full_name)
        return str(dir_id)

    except Exception as error:
        print(error)


def get_film_id(film_name: str):
    """Get film name by film id"""
    if not isinstance(film_name, str):
        return 'Film name should be type str'

    film = Films.query.filter_by(film_name=film_name).first()

    if film is None:
        return film
    return film.film_id


def get_film_name(film_id: int = None):
    """input: film id
    output: film name"""
    if not isinstance(film_id, int):
        return 'Film id should be type int'

    film = Films.get(film_id)
    return film.film_name


def get_full_film_info(film_name: str = '', page: int = 1, genre_list: list = None,
                       dir_list: list = None, rel_start: int = 1900, rel_fin: int = 2100,
                       order: str = None):
    """Get full info about the film"""
    orderby = None
    if order is not None:
        if order.lower() == 'rating':
            orderby = Films.rating
        elif order.lower() == 'release_date':
            orderby = Films.release_date
    else:
        orderby = None

    names = ['film', 'film_id', 'film_name', 'poster', 'release_date',
             'rating', 'username', 'description', 'genres', 'directors']

    if genre_list[0] is None:
        genre_list = []
        gen = Genres.query.add_columns(Genres.genre_name).all()
        for element in gen:
            genre_list.append(element[1])

    if dir_list[0] is None:
        dir_list = []
        direc = Directors.query.add_columns(Directors.director_full_name).all()
        for elem in direc:
            dir_list.append(elem[1])

    all_films = Films.query.select_from(Films)\
        .join(films_genres)\
        .join(films_directors)\
        .join(Genres)\
        .join(Directors)\
        .join(Users, Films.added_user_id == Users.id) \
        .filter(
            (Films.film_name.ilike(f'%{film_name}%')) &
            (Films.film_id == films_genres.c.film_id) &
            (films_genres.c.genre_id == Genres.genre_id) &
            (Genres.genre_name.in_(genre_list)) &
            (films_directors.c.director_id == Directors.director_id) &
            (Directors.name.in_(dir_list)) &
            (Films.release_date.between(rel_start, rel_fin))) \
        .add_columns(
            Films.film_id,
            Films.film_name,
            Films.poster,
            Films.release_date,
            Films.rating,
            Users.username,
            Films.description,
        ).order_by(orderby).paginate(page=page)

    all_genres = Films.query.select_from(Films).join(films_genres).join(Genres).filter(
      (Films.film_id == films_genres.c.film_id) &
      (films_genres.c.genre_id == Genres.genre_id)
      ).add_columns(Films.film_id, Genres.genre_name).all()

    all_directors = Films.query.select_from(Films).join(films_directors).join(Directors).filter(
        (Films.film_id == films_directors.c.film_id) &
        (films_directors.c.director_id == Directors.director_id)
        ).add_columns(Films.film_id, Directors.director_full_name).all()

    gendict = dict()
    dirdict = dict()

    for i in all_genres:
        if i[0] not in gendict:
            gendict[i[0]] = []
            gendict[i[0]].append(i[2])

    for i in all_directors:
        if i[0] not in dirdict:
            dirdict[i[0]] = []
        if i[2] is not None:
            dirdict[i[0]].append(i[2])
        else:
            dirdict[i[0]].append('unknown')

    all_films = all_films.items

    for i, x in enumerate(all_films):
        x = list(x)
        all_films[i] = x
        all_films[i].append(','.join(gendict[x[0]]))
        all_films[i].append(','.join(dirdict[x[0]]))
        a = all_films[i]
        all_films[i] = a

    new_list = []
    for element in all_films:
        new_list.append(dict(zip(names, element)))

    return new_list


def add_new_film(film_name: str, poster: str, release_date: int, rating: float,
                 added_user_id: int, genre: list[str], director: list[str], description: str = None):
    """input all of the parameters (description - optional) for the film, but film id
    output: film id"""
    if not isinstance(film_name, str):
        return 'TypeError: film_name type must be str'
    if not isinstance(poster, str):
        return 'TypeError: poster type must be str'
    if not isinstance(release_date, int):
        return 'TypeError: release_date type must be int'
    if not isinstance(rating, float):
        return 'TypeError: rating type must be float'
    if not isinstance(added_user_id, int):
        return 'TypeError: added_user_id type must be int'
    if not isinstance(genre, list):
        return 'TypeError: genre type must be list[str]'
    if not isinstance(director, list):
        return 'TypeError: director type must be list[str]'
    if not isinstance(description, str):
        return 'TypeError: description type must be str'

    try:
        new_film = Films(film_name=film_name,
                         poster=poster,
                         release_date=release_date,
                         rating=rating, added_user_id=added_user_id,
                         description=description.lstrip().rstrip())
        db.session.add(new_film)
        db.session.commit()

        for dir_full_name in director:
            if get_director(director_full_name=dir_full_name.lstrip().rstrip()) is None:
                add_new_director(director_full_name=dir_full_name.lstrip().rstrip())
            add_dir = Directors.query.filter_by(director_full_name=dir_full_name.lstrip().rstrip())
            new_film.film_director.append(add_dir)
        db.session.commit()

        for gen_name in genre:
            if get_genre(genre_name=gen_name.lstrip().rstrip()) is None:
                add_new_genre(genre_name=gen_name.lstrip().rstrip())
            add_gen = Genres.query.filter_by(genre_name=gen_name.lstrip().rstrip())
            new_film.film_genre.append(add_gen)
        db.session.commit()

        result = get_film_id(film_name=film_name)
        return result
    except Exception as error:
        print(error)


def update_film(film_id: int = None, film_name: str = None,
                poster: str = None, release_date: str = None,
                rating: float = None, added_user_id: str = None,
                genre: list[str] = None, director: list[str] = None,
                description: str = 'None'):
    """Update film info"""
    status = False

    film = Films.query.get(film_id)

    if film.added_user_id in (1, added_user_id):
        if film_name:
            film.film_name = film_name
        if poster:
            film.poster = poster
        if release_date:
            film.release_date = release_date
        if rating:
            film.rating = rating
        if genre:
            for el in genre:
                new_gen = int(get_genre(genre_name=el))
                gen_class = films_genres.query.filter_by(film_id=film_id)
                gen_class.genre_id = new_gen
        if director:
            for d in director:
                new_dir = int(get_director(director_full_name=d))
                dir_class = films_directors.query.filter_by(film_id=film_id)
                dir_class.director_id = new_dir
        if description:
            film.description = description
        db.session.add(film)
        db.session.commit()
        status = True
    return status


def delete_film(film_id: int, user_id: int):
    """Delete film"""
    status = False
    films = db.session.query(Films).filter(Films.film_id == film_id).first()
    if films.added_user_id in (1, user_id):
        db.session.delete(films)
        db.session.commit()
        status = True
    return {'status': status}


def delete_directors(director_full_name: str, user_id: int):
    """
    Delete director
    """
    status = False
    if user_id == 1:
        direct = Directors.query.filter_by(director_full_name=director_full_name).first()
        db.session.delete(direct)
        db.session.commit()
        status = True

    return {'status': status}
