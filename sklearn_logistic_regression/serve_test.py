import requests

headers = {
    'Content-Type': 'application/json; format=pandas-split',
}

data = '{"columns":["x"], "data":[[1], [-1]]}'

response = requests.post('http://localhost:5000/invocations', headers=headers, data=data)
print(response.json())