#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

inboxAll = ['hello']

print ("current inbox options are: ",inboxAll)

inboxToSend = input("To which inbox do you want to send?")
messageToSend = input("What's is the message you want to send?")

channel.basic_publish(exchange='',
                      routing_key=inboxToSend,
                      body=messageToSend)
print(" [x] Sent: ",messageToSend,' to: ',inboxToSend)
connection.close()