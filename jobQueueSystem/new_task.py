#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

amtWI = input('How many items do you want to queue: ')
lenamtWI = int(amtWI)
workItems = []
messages = []

for k in range(lenamtWI):

	workItemToSend = input('Enter work item to send to queue: ')
	workItems.append(workItemToSend)
	message = workItemToSend#' '.join(sys.argv[1:]) or "Hello World!"
	messages.append(message)

for v in range(lenamtWI):
	channel.basic_publish(exchange='',
	                      routing_key='task_queue',
	                      body=messages[v],
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2, # make message persistent
	                      ))
	print(" [x] Sent %r" % messages[v])

connection.close()