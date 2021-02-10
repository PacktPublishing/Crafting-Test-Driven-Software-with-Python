from multiprocessing.managers import SyncManager, ListProxy


_messages = []
def _srv_get_messages():
    return _messages
class _ChatServerManager(SyncManager):
    pass
_ChatServerManager.register("get_messages",
                            callable=_srv_get_messages,
                            proxytype=ListProxy)    

def new_chat_server():
    return _ChatServerManager(("", 9090), authkey=b'mychatsecret')