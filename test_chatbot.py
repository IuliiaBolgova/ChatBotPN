import requests

# Отправляем POST-запрос на сервер Flask
response = requests.post('http://127.0.0.1:5001/chat', json={'message': 'I would like to take a mini photosession, could you give me more info for this package?'})

print(response.json())
