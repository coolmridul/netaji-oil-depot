import requests

url_whatsapp = "https://api.wassenger.com/v1/messages"

headers_whatsapp = {
    "Content-Type": "application/json",
    "Token": "76814737bd1d2336bf151cc1512466cc3f33be295acb5ebb2257db7f36520381aa0b9ae6f6bfefff"
}


def send_payment_whatsapp(message,groupid):

    payload = {
    "group": groupid,
    "message": message
    }
    
    response = requests.post(url_whatsapp, json=payload, headers=headers_whatsapp)

    return response.json()