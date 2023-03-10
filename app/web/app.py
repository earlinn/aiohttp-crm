from typing import Optional

from aiohttp.web import Application as AiohttpApplication
from aiohttp.web import Request as AiohttpRequest
from aiohttp.web import View as AoihttpView
from aiohttp.web import run_app as aiohttp_run_app
from aiohttp_apispec import setup_aiohttp_apispec

from app.store import setup_accessors
from app.store.crm.accessor import CrmAccessor
from app.web.config import Config, setup_config
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Optional[Config] = None
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(AoihttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_config(app)
    setup_routes(app)
    setup_aiohttp_apispec(
        app, title="CRM Application", url="/docs/json", swagger_path="/docs"
    )
    setup_middlewares(app)
    setup_accessors(app)
    aiohttp_run_app(app, host="127.0.0.1")
