import asyncio
import json
import random

from variables import HOST, PORT

"""Серверная часть использовалась исключительно для тестов"""

async def handle_echo(reader, writer):
    # по аналогии и здесь, и в питесте - все команды, параметры и пр. берется из одной
    # и той же разделяемой сущности - общего словаря
    commands = ['ON', 'OFF', "COLOR"]
    command = random.choice(commands)
    metadata = ["white", "green", "red", None]
    metadata = random.choice(metadata)
    data = json.dumps({"command": command, "metadata": metadata}).encode()
    writer.write(data)
    try:
        await writer.drain()
        writer.close()
    except ConnectionResetError as error:
        print(error)



async def main():
    server = await asyncio.start_server(
        handle_echo, HOST, PORT)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
