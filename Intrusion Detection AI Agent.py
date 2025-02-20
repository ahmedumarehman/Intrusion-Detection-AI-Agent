import random

class IntrusionDetectionAgent:
    def __init__(self):
        self.alerts = []
    
    def perceive(self, source_ip, request_rate, anomalies_count, packet_size, protocol_type):
        """Analyzes network traffic and classifies it as normal or suspicious."""
        if request_rate > 100:
            self.act(source_ip, "High Request Rate")
        elif anomalies_count > 5:
            self.act(source_ip, "High Anomalies Count")
        elif packet_size > 4000:
            self.act(source_ip, "Large Packet Size")
        elif protocol_type == "ICMP" and request_rate > 100:
            self.act(source_ip, "Potential DDoS Attack - High ICMP Traffic")
        else:
            print(f"Traffic from {source_ip} is normal.")
    
    def act(self, source_ip, reason): # """Logs alerts for suspicious activity."""
       
        alert = f"ALERT! Suspicious activity detected from {source_ip} - {reason}"
        self.alerts.append(alert)
        print(alert)

def generate_random_ip():#"""Generates a random IP address within 192.168.56.101 - 192.168.56.255."""
    
    return f"192.168.56.{random.randint(101, 255)}"

def generate_traffic(): #"""Simulates random network traffic data."""
    
    return {
        "source_ip": generate_random_ip(),
        "request_rate": random.randint(10, 200),
        "anomalies_count": random.randint(0, 10),
        "packet_size": random.randint(100, 5000),
        "protocol_type": random.choice(["TCP", "UDP", "ICMP"]),
    }

# Instantiate the Intrusion Detection Agent
agent = IntrusionDetectionAgent()

# Generate and analyze 10 traffic samples
for _ in range(10):
    traffic_data = generate_traffic()
    agent.perceive(**traffic_data)
