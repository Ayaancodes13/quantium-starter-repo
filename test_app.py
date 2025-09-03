import pytest
from dash.testing.application_runners import import_app

def dash_app():
   app = import_app("process_sales_chart.py") 
   return app

def test_header(dash_duo):
   dash_duo.start_server(dash_app)
   header = dash_duo.find_element("H1")
   assert "Soul Foods sales visualizer" in header.text

def test_graph(dash_duo):
   dash_duo.start_server(dash_app)
   graph = dash_duo.find_element("#sales-line-chart")
   assert graph is not None

def test_region(dash_duo):
   dash_duo.start_server(dash_app)
   region_picker = dash_duo.find_element("#region-filter")
   assert region_picker is not None