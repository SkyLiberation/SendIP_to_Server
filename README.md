# SendIP_to_Server

Use socket to build a connection, and send the ever-changing IP of intranet computer.

## Demands

An intranet computer use pppoeconf to connect internet, but the intranet IP of the computer changes when the computer reconnect to internet(maybe reboot or instable network). Another machine in the same intranet needs the new intranet IP to build a ssh connection.

## Solution

Build a socket connection between a server in the public network and the intranet computer. When the server receives the intranet IP from the intranet computer, the server will update its static html.

## Code Constitution

> **Server End**: Server.py
> **Client End**: Client.py

## Make Timed Tasks

> crontab -e
>
> '''run the server.py in 59 every hour'''
>
> 59 */1 * * * /usr/bin/python /home/ubuntu/LJT/server.py
>
> '''run the server.py in 0 every hour'''
>
> 0 */1 * * * /usr/bin/python /home/ubuntu/LJT/client.py
>
> '''the socket will wait the connection for 2 minutes and stop waiting after 2 minutes.'''
