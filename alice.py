from syft.workers.websocket_server import WebsocketServerWorker
import syft as sy
import torch
hook = sy.TorchHook(torch)

kwargs = {
    "id": "alice",
    "host": "localhost",
    "port": 8779,
    "hook": hook,
    "verbose": True
}

server = WebsocketServerWorker(**kwargs)
server.start()