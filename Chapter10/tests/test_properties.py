from hypothesis import given
import hypothesis.strategies as st

from contacts import Application


@given(st.text())
def test_adding_contacts(name):
    app = Application()

    app.run(f"contacts add {name} 3456789")

    name = name.strip()
    if name:
        assert app._contacts == [(name, "3456789")] 
    else:
        assert app._contacts == []

