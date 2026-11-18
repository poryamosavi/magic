import requests

HUB_URL = 'http://127.0.0.1:8000'

def send_telemetry_01(readings: list[float]):
    avg_val = round(sum(readings) / len(readings), 3)
    contract_payload = {
        'sender': 'Node_Processor_01',
        'receiver': 'Analytics_Engine',
        'topic': 'sensor_telemetry',
        'value': {'average': avg_val, 'samples': readings}
    }
    res = requests.post(f'{HUB_URL}/publish', json=contract_payload, timeout=5)
    return res.json()
