# Подтверждение множества сообщений за один раз
import rabbitpy

for msg in rabbitpy.consume('amqp://guest:guest@localhost:5672/%2F','test-msg'):
    msg.pprint()
    print('Redelivered msg: %s' % msg.redelivered)
    msg.reject(True)