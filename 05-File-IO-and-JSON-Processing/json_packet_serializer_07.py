import json

def build_json_packet_07(sender: str, receiver: str, payload: list[float]) -> str:
    packet = {
        'packet_id': 7,
        'sender': sender,
        'receiver': receiver,
        'metrics': {'count': len(payload), 'avg': round(sum(payload)/max(len(payload), 1), 3)},
        'values': payload
    }
    return json.dumps(packet, indent=2)

if __name__ == '__main__':
    print(build_json_packet_07('Sensor_07', 'Central_Hub', [10.2, 14.8, 19.5]))
