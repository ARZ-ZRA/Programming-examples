import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        exchange = rabbitpy.Exchange(channel,
                                     'headers_rpc_request',
                                     exchange_type='headers')
        exchange.declare()