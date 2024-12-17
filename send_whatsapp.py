import requests

url_whatsapp = "https://api.wassenger.com/v1/messages"

headers_whatsapp = {
    "Content-Type": "application/json",
    "Token": "1c791710eb14b270858ccdf54ff683d8f0ad41a839af45aed542404cc2d2d13e74c302fd122a96d7"
}


def send_payment_whatsapp(message,groupid):

    payload = {
    "group": groupid,
    "message": message
    }
    
    response = requests.post(url_whatsapp, json=payload, headers=headers_whatsapp)

    return response.json()