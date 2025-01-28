import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as plotly
import dash.testing.wait as wait
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from dataVisual import app


def test_header(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=60)


def test_graph(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=60)


def test_filter(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=60)
