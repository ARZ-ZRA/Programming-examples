# Пакетная обработка с транзакциями
import rabbitpy

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        tx = rabbitpy.Tx(channel)
        tx.select()
        message = rabbitpy.Message(channel,
                                   '   |;-)',
                                   {'content_type': 'text/plain',
                                    'delivery_mode': 2})
        message.publish('exhg', 'important_msg')
        try:
            if tx.commit():
                print('Transaction committed')
        except rabbitpy.exceptions.NoActiveTransactionError:
            print('Tried to commit without active transaction')