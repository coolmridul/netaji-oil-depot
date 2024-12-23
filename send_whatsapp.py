import requests

url_whatsapp = "https://api.wassenger.com/v1/messages"

headers_whatsapp = {
    "Content-Type": "application/json",
    "Token": "34ad67d75b6185d117c6f7134ed2fbb70e0afbfb7c5783c791bcfda7a4512161255ce04177a85dab"
}


def send_payment_whatsapp(message,groupid):

    payload = {
    "group": groupid,
    "message": message
    }
    
    response = requests.post(url_whatsapp, json=payload, headers=headers_whatsapp)

    return response.json()