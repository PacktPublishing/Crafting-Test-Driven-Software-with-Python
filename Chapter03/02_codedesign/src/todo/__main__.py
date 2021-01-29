from .app import TODOApp
from .db import BasicDB

TODOApp(dbmanager=BasicDB("todo.data")).run()