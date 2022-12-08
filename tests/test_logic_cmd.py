import ast
import json
from json import JSONDecodeError
from variables import HOST, PORT
import pytest

from flashlight_control import make_command
from main import create_connection
from my_exceptions import ValidationError
from validators import is_valid


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.mark.parametrize("expected, command", [
    (True, {"command": "ON", "metadata": "green"}),
    (None, {"command": "ONN", "metadata": "green"}),
    (True, {"command": "off", "metadata": "green"}),
    (None, {"command": "offf", "metadata": "green"}),
    (True, {"command": "coLor", "metadata": "green"}),
    (None, {"command": "new_cmd", "metadata": "green"})
])
def test_make_command(expected, command):
    """
    тестируем выполнение комманд
    """
    result = make_command(command)
    assert expected == result


@pytest.mark.anyio
async def test_connection(mock_connection, mock_reader):
    reader, writer = await create_connection(HOST, PORT)
    data = await reader.read(100)
    try:
        data = json.loads(data)
    except JSONDecodeError:
        data = ast.literal_eval(data.decode("UTF-8"))
    with pytest.raises(ValidationError):
        is_valid(data)
