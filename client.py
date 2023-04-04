# IS496: Computer Networks (Spring 2023)
# Name and Netid of each member:
# Member 1: Ken Wu (shwu2)
# Member 2: Thomas Huang (yenshuo2)
# Member 3: Jack Chuang (yzc2)

# Import any necessary libraries below
import socket
import sys
import time
import struct
from pg1lib import *

BUFFER = 2048

############## Beginning of Part 1 ##############


def part1():
    print("********** PART 1 **********")
    PORT = 41025
    message = b"Hello World"
    # HOST = socket.gethostbyname(socket.gethostname())
    HOST = socket.gethostbyname("student00.ischool.illinois.edu")
    addr = (HOST, PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    except socket.error as msg:
        print('Failed to create socket.')
        print(msg)
        sys.exit()

    s.sendto(message, addr)

    while True:
        data, addr = s.recvfrom(BUFFER)
        if not data:
            break

        print(f"Acknowledgement: {data.decode('utf-8')}")
        break

    s.close()

############## End of Part 1 ##############

############## Beginning of Part 2 ##############


def part2():
    startTime = time.time()
    print("********** PART 2 **********")
    HOST = socket.gethostbyname(sys.argv[1])
    PORT = int(sys.argv[2])
    message = sys.argv[3]

    addr = (HOST, PORT)
    publicKey = getPubKey()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    except socket.error as msg:
        print('Failed to create socket.')
        print(msg)
        sys.exit()

    s.sendto(publicKey, addr)

    bytesPair = s.recvfrom(BUFFER)

    decryptedPublicKey = decrypt(bytesPair[0])

    dataToCheckSum = checksum(message.encode())
    print(f"Checksum sent: {dataToCheckSum}")

    encryptMessage = encrypt(message.encode(), decryptedPublicKey)
    package = struct.pack("L {}s".format(
        len(encryptMessage)), dataToCheckSum, encryptMessage)
    s.sendto(package, addr)

    secondBytesPair = s.recvfrom(BUFFER)

    res_code = int(secondBytesPair[0].decode())
    if res_code == 1:
        print("Server has successfully received the message!")
        endTime = time.time()
        duration = endTime - startTime
        print(f"RTT: {duration * 1000} μs")
    else:
        print("The checksum does not match...")

    s.close()

############## End of Part 2 ##############


if __name__ == '__main__':
    if len(sys.argv) == 1:
        part1()
    else:
        part2()
