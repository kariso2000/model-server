import dash
import dash_bootstrap_components as dbc
from flask import Flask
from dask.distributed import Client
from ai4good.runner.facade import Facade
from ai4good.webapp.model_runner import ModelRunner

flask_app = Flask(__name__)

dash_app = dash.Dash(
    __name__,
    server=flask_app,
    routes_pathname_prefix='/sim/',
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)


_client = None  #Needs lazy init


def dask_client() -> Client:
    global _client
    if _client is None:
        _client = Client(processes=False)
    return _client


facade = Facade.simple()
model_runner = ModelRunner(facade, dask_client)