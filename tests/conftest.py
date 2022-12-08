import asyncio
from asyncio import StreamReader, StreamWriter

import pytest


@pytest.fixture
async def mock_connection(monkeypatch):
    async def mock_get(host, port):
        return StreamReader, StreamWriter
    monkeypatch.setattr(asyncio, "open_connection", mock_get)


@pytest.fixture(params=[
    b'{"command": "color"}',
    b'{"new_cmd": "music"}',
    b'{"command": 1}',
    b'{"command": 1, "metadata": None}',
    b'{"command": "test", "metadata": 1}'
])
async def mock_reader(request, monkeypatch):
    async def mock_return(*args):
        return request.param
    monkeypatch.setattr(StreamReader, "read", mock_return)
