import json
import os
import pytest
from api.client import Client


@pytest.fixture(scope="session")
def config():
    root_path = os.path.dirname(os.path.abspath("config.json"))
    config_file = os.path.join(root_path, "config.json")
    file = open(config_file)

    return json.load(file)


@pytest.fixture(scope="function")
def api_client(config):
    base_url = config.get("base_url")

    return Client(base_url)
