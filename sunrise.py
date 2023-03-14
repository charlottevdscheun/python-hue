from huesdk import Hue
import requests
r = requests.get('https://discovery.meethue.com/').json()
hue = Hue(bridge_ip=r[0]["internalipaddress"], username="hsrDA1kgt9BmQXfXaX6AQuYJKCNSTOY-czvgnXfX")

light = hue.get_light(name="Bedroom")
# turn on
light.on()

# set color and saturation
light.set_color(hexa="#ff3103")
light.set_saturation(254)

# transition to brightest in  600ms * 30m = 1800
light.set_brightness(254, transition=18000)
