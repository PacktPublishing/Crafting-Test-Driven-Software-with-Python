import pytest 

pytest_plugins = ["fizzbuzz.testing.fixtures"]


def pytest_runtest_setup(item):
    print("Hook announce", item)


@pytest.fixture(scope="function", autouse=True)
def enterexit():
    print("ENTER")
    yield
    print("EXIT")


def pytest_addoption(parser):
    parser.addoption(
        "--upper", action="store_true", 
        help="test for uppercase behaviour"
    )

