# This file will initialize our Flask app and all fixtures that we need.

""" 
There are 3 pytest fixtures: explicit, modular, scalable. Fixtures initialize test functions.

They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results. 
Initialization may setup services, state, or other operating environments. These are accessed by test functions 
through arguments; for each fixture used by a test function there is typically a parameter (named after the fixture)
in the test function’s definition.
"""

import pytest
from main import app as flask_app


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()

# Now, pytest will discover all our test files, We can create some test files with test_ prefix in the same directory.
