from multiprocessing.managers import SyncManager, ListProxy


def new_chat_server():
    messages = []

    class _ChatServerManager(SyncManager):
        pass
    _ChatServerManager.register("get_messages", callable=lambda: messages, 
                                proxytype=ListProxy)    
    return _ChatServerManager(("", 9090), authkey=b'mychatsecret')
