# IS496: Computer Networks (Spring 2023)
# Name and Netid of each member:
# Member 1: Ken Wu (shwu2)
# Member 2: Thomas Huang (yenshuo2)
# Member 3: Jack Chuang (yzc2)

# Import any necessary libraries below
import socket
import sys
import struct
from pg1lib import *


BUFFER = 2048

############## Beginning of Part 1 ##############


def part1():
    print("********** PART 1 **********")
    PORT = 41025
    sin = ('', PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    except socket.error as e:
        print('Failed to create socket.')
        print(e)
        sys.exit()

    try:
        s.bind(sin)

    except socket.error as e:
        print('Failed to bind socket.')
        print(e)
        sys.exit()

    print("Waiting ...")

    while True:
        data, addr = s.recvfrom(BUFFER)
        if not data:
            break

        print(f"Client message: {data.decode('utf-8')}")
        s.sendto(b"1", addr)
        break

    s.close()


############## End of Part 1 ##############


############## Beginning of Part 2 ##############

def part2():
    print("********** PART 2 **********")
    PORT = int(sys.argv[1])
    publickey = getPubKey()
    sin = ('', PORT)

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    except socket.error as e:
        print('Failed to create socket.')
        print(e)
        sys.exit()

    try:
        s.bind(sin)

    except socket.error as e:
        print('Failed to bind socket.')
        print(e)
        sys.exit()

    while True:
        print("Waiting ...")
        print()
        bytesPair = s.recvfrom(BUFFER)
        if not bytesPair:
            break

        encryptedPublicKey = encrypt(
            publickey, bytesPair[0])
        s.sendto(encryptedPublicKey, bytesPair[1])

        secondBytesPair = s.recvfrom(BUFFER)
        checksumFromClient, messageFromClient = struct.unpack(
            "L {}s".format(len(secondBytesPair[0]) - 8), secondBytesPair[0])

        decryptedMessage = decrypt(
            messageFromClient)
        print(
            f"******** New Message ********\n\nReceived message:\n{decryptedMessage.decode('utf-8')}\n")
        print(
            f"Received Client Checksum: {checksumFromClient}")

        dataToCheckSum = checksum(decryptedMessage)
        print(f"Calculated Checksum: {dataToCheckSum}")
        print()

        if dataToCheckSum != checksumFromClient:
            print("The checksum does not match...")

            s.sendto(b"0", secondBytesPair[1])

        else:
            s.sendto(b"1", secondBytesPair[1])

    s.close()

############## End of Part 2 ##############


if __name__ == '__main__':
    if len(sys.argv) == 1:
        part1()
    else:
        part2()
