from machine import deepsleep
import network
try:
    import urequests as requests
except ModuleNotFoundError:
    import requests

# CONFIG
WIFI_SSID = ''
WIFI_PASSWORD = ''

TOKEN = ''
URL = f"https://api.telegram.org/bot{TOKEN}/"
CHAT_ID = ''

# Connect to WiFi network
def wifi_connect():
    print('\nConnect to network...')
    # create station interface
    wlan = network.WLAN(network.STA_IF)
    # activate the interface
    wlan.active(True)
    # check if the station is connected to an AP
    if not wlan.isconnected():
        # connect to an AP
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    
    # get the interface's IP/netmask/gw/DNS addresses
    print('\nNetwork config:')
    print(wlan.ifconfig())


# Send message to Telegram
def send_message(text, chat_id):
    url = f"{URL}sendMessage?text={text}&chat_id={chat_id}"
    response = requests.get(url)
    content = response.text
    return content


# INIT
if __name__ == '__main__':
    wifi_connect()
    send_message('🏠: Электричество в норме ⚡️', CHAT_ID)

    # put the device to sleep for 1 min
    print('\nSleep...')
    deepsleep(60000)