import pytest
from channels.testing import WebsocketCommunicator
from myproject.asgi import application

@pytest.mark.asyncio
async def test_chat_consumer():
    communicator = WebsocketCommunicator(application, "/ws/chat/")
    connected, _ = await communicator.connect()
    assert connected

    await communicator.send_to(text_data="Hello")
    response = await communicator.receive_from(timeout=5)
    assert response == "Echo: Hello"

    await communicator.disconnect()
