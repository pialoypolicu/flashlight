import asyncio
import random


async def handle_echo(reader, writer):
    cnt = 0
    while True:
        commands = ['ON', 'OFF', "COLOR"]
        command = random.choice(commands)
        metadata = ["white", "green", "red", None]
        metadata = random.choice(metadata)
        data = str({"command": command, "metadata": metadata}).encode()
        writer.write(data)
        try:
            await writer.drain()
            print(cnt)
        except ConnectionResetError as error:
            writer.close()
            print(error)
            break
        await asyncio.sleep(2)
        cnt += 1



async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 9999)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())