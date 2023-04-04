# Programming Assignment 1 (PG1) - Simple Secure UDP Program

IS496: Computer Networks (Spring 2023) \
Name and Netid of each member: \
Member 1: Ken Wu (shwu2) \
Member 2: Thomas Huang (yenshuo2) \
Member 3: Jack Chuang (yzc2)

## Background

This is a simple and secure communication protocol using UDP client and server. The program will build a UDP connection between two hosts and exchange encryption keys. The client will then send an encrypted message to the server. The server will decrypt the message and reply with the timestamp when it receives the message.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some modules.

```shell
pip install cryptography
```

## Preparation

```shell
import socket
import sys
import struct
from pg1lib import *
```

## Execution

Please connect to your student machines first.

```shell
$ ssh YOUR_NET_ID@student00.ischool.illinois.edu

$ ssh YOUR_TEAM_MEMBER_NET_ID@student01.ischool.illinois.edu
```

The server is running on student00, the client should be tested on student student01/student02/student03.

### Part 1: UDP Practice

In this part of the assignment, we built a simple UDP server and client where the server can successfully establish the connection with the client and send a string (e.g., "Hello World") to the client.

Run the socket server program.

```shell
YOUR_NET_ID@is-student00:~$ /YOUR_PATH/python3 server.py
```

Then the server terminal will show the messages below:

```
********** PART 1 **********
Waiting ...

```

Run the socket client program.

```shell
YOUR_TEAM_MEMBER_NET_ID@is-student01:~$ /YOUR_PATH/python3 client.py
```

Then the server terminal will receive the messages from the client, and reply the message below:

```
Client message: Hello World

```

The client side will receive the confirmation.

```
Acknowledgement: 1
```

### Part 2: Simple Secure UDP Program

In this part of the assignment, we use the code from part1 as the framework and make the client program read the host name, port number, and the message to be sent from the user input.

UDP client that takes in:

- The hostname of the server (argument 1).
- The port number on the server (argument 2).
- The text to be sent (argument 3).

UDP server that takes in:

- The port number to listen on (argument 3).

Run the socket server program.

```shell
YOUR_NET_ID@is-student00:~$ /YOUR_PATH/python3 server.py [PORT_NUMBER]
```

Then the terminal will show the messages below:

```
********** PART 2 **********
Waiting ...

```

Run the socket client program.

```shell
YOUR_TEAM_MEMBER_NET_ID@is-student01:~$ /YOUR_PATH/python3 client.py [SERVER_HOST_NAME] [PORT_NUMBER] [THE_TEXT_YOU_WANT_TO_TEST]
```

Then the server terminal will show the messages below:

```
******** New Message ********

Received message: [THE_TEXT_YOU_WANT_TO_TEST]
```

The server program will receive the encrypted message and checksum from the client. The server will decrypt the message from the client and then compare the result to the received checksum.

```
Received Client Checksum: XXX
Calculated Checksum: XXX
```

If the checksum matches, the server sends a confirmation to the client. If the checksum does not match, the server reports an error message and acknowledges the client.

The client side will show the messages below and calculate the round-trip-time (RTT), in microseconds, from the time it sent the message to when it received a response.

```
Checksum sent: XXX
Server has successfully received the message.
RTT: XXX μs
```
