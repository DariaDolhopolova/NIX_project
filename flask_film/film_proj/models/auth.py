"""File for authentification"""

from film_proj import login_manager
from film_proj.db_core import get_user_username


@login_manager.user_loader
def load_user(id):
    return get_user_username(int(id))
