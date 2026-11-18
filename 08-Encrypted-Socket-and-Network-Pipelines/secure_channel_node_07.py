import hashlib
import hmac
import json
import socket

SECRET_KEY = b'engineering_shared_secret_key_07'

def sign_payload_07(data: dict) -> str:
    raw = json.dumps(data, sort_keys=True).encode('utf-8')
    signature = hmac.new(SECRET_KEY, raw, hashlib.sha256).hexdigest()
    return json.dumps({'payload': data, 'hmac_sha256': signature})

def verify_payload_07(signed_json: str) -> bool:
    envelope = json.loads(signed_json)
    raw = json.dumps(envelope['payload'], sort_keys=True).encode('utf-8')
    expected = hmac.new(SECRET_KEY, raw, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, envelope['hmac_sha256'])

if __name__ == '__main__':
    msg = sign_payload_07({'channel': 7, 'status': 'ENCRYPTED_LINK_OK'})
    print('Verified:', verify_payload_07(msg))
