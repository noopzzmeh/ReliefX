import requests
url = "https://activity-y-titanium-delays.trycloudflare.com/api/reliefx/infer"
payload = {"incident_id": "INC200", "data": [10, 50, 90]}
resp = requests.post(url, json=payload)
print(resp.status_code, resp.text)
