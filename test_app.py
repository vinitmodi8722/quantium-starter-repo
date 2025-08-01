import pytest
from dash import Dash
from app import app  # 👈 make sure this points to your Dash app

# This is a fixture that sets up the Dash test app
@pytest.fixture
def dash_app():
    return app

def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"

def test_graph_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("div.js-plotly-plot")
    assert graph is not None

def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_items = dash_duo.find_element("#region-selector")
    assert radio_items is not None
