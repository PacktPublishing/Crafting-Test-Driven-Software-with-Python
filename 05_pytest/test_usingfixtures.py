import pytest

@pytest.mark.usefixtures("provide_current_time")
class TestMultiple:
    def test_first(self):
        print("RUNNING AT", self.now)
        assert 5 == 5

    @pytest.mark.usefixtures("greetings")
    def test_second(self):
        assert 10 == 10


@pytest.fixture
def greetings():
    print("HELLO!")
    yield
    print("GOODBYE")


@pytest.fixture(scope="class")
def provide_current_time(request):
    import datetime
    request.cls.now = datetime.datetime.utcnow()
    print("ENTER CLS")
    yield
    print("EXIT CLS")

