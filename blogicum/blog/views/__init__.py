from .posts import (
    index,
    post_detail,
    create_post,
    edit_post,
    delete_post,
    add_comment,
    edit_comment,
    delete_comment,
) # noqa 401
from .categories import category_posts # noqa 401
from .users import profile, edit_profile, RegistrationView, my_profile # noqa 401