from contacts import Application

def test_loading(benchmark):
    app = Application()
    app._contacts = [(f"Name {n}", "number") for n in range(1000)]
    app.save()

    benchmark(app.load)
