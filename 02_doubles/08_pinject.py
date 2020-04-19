class ChatClient:
    def __init__(self, connection):
        print(self, "GOT", connection)

class Connection:
    pass

import pinject
injector = pinject.new_object_graph()
cli = injector.provide(ChatClient)


class FakeConnection:
    pass


class FakedBindingSpec(pinject.BindingSpec):
    def provide_connection(self):
        return FakeConnection()

faked_injector = pinject.new_object_graph(binding_specs=[FakedBindingSpec()])
cli = faked_injector.provide(ChatClient)
cli2 = faked_injector.provide(ChatClient)


class PrototypeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_connection(self):
        return Connection()

proto_injector = pinject.new_object_graph(binding_specs=[PrototypeBindingSpec()])
cli = proto_injector.provide(ChatClient)
cli2 = proto_injector.provide(ChatClient)
