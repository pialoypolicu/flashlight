import ast
import asyncio
import json
from asyncio import StreamReader, StreamWriter
from json.decoder import JSONDecodeError

from loguru import logger

from flashlight_control import make_command
from validators import is_valid


async def create_connection(host: str, port: int) -> tuple[StreamReader, StreamWriter]:
    while True:
        try:
            reader, writer = await asyncio.open_connection(host, port)
            return reader, writer
        except ConnectionRefusedError as error:
            logger.error(error)
            await asyncio.sleep(1)


async def main_client(message: str) -> None:
    logger.info(message)
    reader, writer = await create_connection("127.0.0.1", 9999)
    data = await reader.read(100)
    try:
        data = json.loads(data)
    except JSONDecodeError:
        data = ast.literal_eval(data.decode("UTF-8"))
    writer.close()
    await is_valid(data)
    await make_command(data)


if __name__ == '__main__':
    asyncio.run(main_client('run client!'))
