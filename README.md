# MQTT-Twistedws-GoogleCharts
A Twisted Websocket back-end for MQTT displayed in Google Charts.

MQTT + Twisted Websockets = A match made in heaven!

Twisted, an open source, event-driven networking engine written in Python, apparently is a match for MQTT, one of the emerging protocols for the future network architecture, IoT (Internet of Things). MQTT follows a publish-subscribe mechanism where the subscriber listens for events in the form of published messages from publishers in certain topics, a mechanism that aligns with the event driven nature of Twisted.

Here I present a simple implementation of utilizing an MQTT subscriber alongside Twisted WebSockets and displaying the data graphically using Google Charts library and jQuery for dynamic, real-time data loading. 

This started as the submission for my final project in Network Programming course and I realised there isn't much or even no one that have tried this (Twisted Websockets + MQTT) or atleast documented something like this in the internet, so here it is.

So this is how it works:

MQTT Publisher -> MQTT Subscriber + Twisted Websocker server -> Google charts

For the broker I used mosquitto.

I made a simulated MQTT publisher in "sensors_pub.py", you can start multiple publishers by entering a name as python argument.

