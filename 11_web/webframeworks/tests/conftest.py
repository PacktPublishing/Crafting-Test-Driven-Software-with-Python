import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--framework", action="store", 
        help="Choose which framework to use for "
             "the web application: [tg2, django, flask, pyramid]"
    )


@pytest.fixture
def wsgiapp(request):
    framework = request.config.getoption("--framework")

    if framework == "tg2":
        from wbtframeworks.tg2 import make_application
    elif framework == "flask":
        from wbtframeworks.flask import make_application
    elif framework == "pyramid":
        from wbtframeworks.pyramid import make_application
    elif framework == "django":
        from wbtframeworks.django import make_application
    else:
        make_application = None

    if make_application is not None:
        return make_application()

    if framework is None:
        raise ValueError("Please pick a framework with --framework option")
    else:
        raise ValueError(f"Invalid framework {framework}")