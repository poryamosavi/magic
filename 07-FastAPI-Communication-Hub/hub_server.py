from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

app = FastAPI(title='Central Multi-Module Communication Hub')
message_bus: list[dict] = []

class DataContract(BaseModel):
    sender: str
    receiver: str
    topic: str
    value: Any

@app.post('/publish')
def publish_packet(packet: DataContract):
    record = packet.model_dump()
    message_bus.append(record)
    return {'status': 'queued', 'bus_depth': len(message_bus)}

@app.get('/consume/{module_name}')
def consume_packets(module_name: str):
    matched = [m for m in message_bus if m['receiver'] == module_name]
    if not matched:
        raise HTTPException(status_code=404, detail='No packets available for target module')
    return {'receiver': module_name, 'count': len(matched), 'packets': matched}
