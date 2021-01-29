from tg import expose, TGController

class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World'


def make_application():
    from tg import MinimalApplicationConfigurator

    config = MinimalApplicationConfigurator()
    config.update_blueprint({
        'root_controller': RootController()
    })

    return config.make_wsgi_app()