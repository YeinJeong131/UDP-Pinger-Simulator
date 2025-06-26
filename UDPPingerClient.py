from socket import *
from time import time, sleep
 
def udp_pinger_client():
    server_address = ('localhost', 12000)
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(1)

    sequence_number = 1
    rtts = []
    packet_loss = 0

    for i in range(10):
        message = f"Ping {sequence_number} {time()}"
        try:
            start_time = time()
            client_socket.sendto(message.encode(), server_address)
            response, _ = client_socket.recvfrom(1024)
            end_time = time()

            rtt = end_time - start_time
            rtts.append(rtt)
            print(f"Reply from server: {response.decode()} | RTT: {rtt:.4f} seconds")
        except timeout:
            print(f"Request timed out for sequence number {sequence_number}")
            packet_loss += 1

        sequence_number += 1

    if rtts:
        print(f"\n -- Ping Test Results --")
        print(f"Mininum RTT: {min(rtts): .4f} seconds")
        print(f"Maxinum RTT: {max(rtts): .4f} seconds")
        print(f"Average RTT: {sum(rtts) / len(rtts): .4f} seconds")
    print(f"Packet Loss Rate: {(packet_loss / 10) * 100}%")

    client_socket.close()

if __name__ == "__main__":
    udp_pinger_client() 

