import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from app.crm.views import AddUserView, GetUserView, ListUserView
    app.router.add_view("/add_user", AddUserView)
    app.router.add_view("/list_users", ListUserView)
    app.router.add_view("/get_user", GetUserView)
