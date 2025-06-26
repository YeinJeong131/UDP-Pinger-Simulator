# UDP-Pinger-Simulator

This project simulates a basic **UDP Ping client-server** system to evaluate **Round-Trip Time (RTT)** and simulate **packet loss** in an unreliable network environment.

## 📌 Overview

This simulation involves:
- A **UDP Server** that randomly drops packets with a defined probability.
- A **UDP Client** that sends 10 ping messages to the server and calculates RTT for each.

The goal is to understand how network unreliability can affect RTT and how clients behave in response to dropped packets.

---

## 🛠 Files

| File | Description |
|------|-------------|
| `UDPPingerServer_YeinJeong_14650170.py` | Simulates a server that listens for UDP pings and randomly drops packets |
| `UDPPingerClient_YeinJeong_14650170.py` | Sends 10 UDP pings and measures round-trip time for each |

---

## ⚙️ How It Works

### Server (`UDPPingerServer`)
- Listens on a predefined port.
- Randomly chooses whether to respond or simulate a drop (e.g. 40% drop rate).
- Responds with the same message if not dropped.

### Client (`UDPPingerClient`)
- Sends 10 ping messages with timestamp.
- Waits up to 1 second for a reply.
- If reply received: RTT is calculated.
- If timeout: Packet is considered lost.

---

## ✅ Sample Output

```bash
Ping 1 RTT: 37 ms
Ping 2 RTT: 41 ms
Ping 3 Request timed out
...
Ping 10 RTT: 35 ms

Packets Sent: 10
Packets Received: 7
Packet Loss Rate: 30%
```
## 💡 Learning Objectives
Through this project, I learned:
- How to use Python’s socket library for UDP communication.
- How to simulate packet loss using randomization.
- How to calculate RTT using timestamps.
- How to handle timeouts in socket programming with settimeout().

## 📎 How to Run
Run the server:
```bash
python UDPPingerServer_YeinJeong_14650170.py
```

In a new terminal, run the client:
```bash
python UDPPingerClient_YeinJeong_14650170.py
```
> Make sure both scripts are in the same folder and no firewall is blocking UDP port.
