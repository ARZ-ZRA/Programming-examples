import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        exchange = rabbitpy.Exchange(channel,
                                     'topic_rpc_request',
                                     exchange_type='topic')
        exchange.declare()