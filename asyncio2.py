import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message,addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()
    print("close the client socket")
    writer.close()

#loop = asyncio.get_event_loop()

    server_coro = asyncio.start_server(handle_echo, '127.0.0.1', 2500, loop=loop)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        await server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
asyncio.run(main())