# В задачке указаны варианты:
# 3. Реализация сетевого протокола может быть на aiohttp, tornado или fastAPI.
import asyncio
# Переделайте, пожалуйста, используя fastAPI
import json
from asyncio import StreamReader, StreamWriter
from json.decoder import JSONDecodeError

from loguru import logger

from flashlight_control import make_command
from validators import is_valid
from variables import HOST, PORT


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
    reader, writer = await create_connection(HOST, PORT)
    data = await reader.read(100)
    writer.close()
    try:
        data = json.loads(data)
    except JSONDecodeError as error:
        logger.error(f"json parse error {error}")
    is_valid(data)
    make_command(data)


if __name__ == '__main__':
    asyncio.run(main_client('run client!'))
