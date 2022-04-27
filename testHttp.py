# from telnetlib import STATUS
import requests
url='https://wr1vl7f6hf.execute-api.us-east-1.amazonaws.com/Prod/getUserNotes/'


def getCreated_date(item):
    return item.get("created_date")

#1 200
headers = {'Bearer': '25d73ffca742'}
response = requests.post(url,headers=headers)
assert response.status_code==200 , str(response.status_code)+": es incorrecto , debe ser 200"
assert len(response.json()['data']) <11 , "Exceso de notas"
assert sorted(response.json()['data'],key=getCreated_date,reverse=True) == response.json()['data'] , "Los datos no esta ordenado"

headers = {'Bearer': '6579e96f76ba'}
response = requests.post(url,headers=headers)
assert response.status_code==200 , str(response.status_code)+": es incorrecto , debe ser 200"
assert len(response.json()['data']) <11 , "Exceso de notas"
assert sorted(response.json()['data'],key=getCreated_date,reverse=True) == response.json()['data'] , "Los datos no esta ordenado"


# Prueba de error 403
response = requests.post(url)
assert response.status_code==403 , "fallo en el status-Code 403"
assert response.json()["message"]=="The Authentication header is malformed or missing." , "fallo en el mensaje de status 403"


# Prueba de error 400
headers = {'Bearer': '25d73ffca74'}
response = requests.post(url,headers=headers)
assert response.status_code==400 , "fallo en el status-Code 400"
assert response.json()["message"]=="Token is invalid or empty (Bearer )." , "fallo en el mensaje de status 400"

print("Todo las pruebas fueron aprobado")




