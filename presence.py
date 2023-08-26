from pypresence import Presence
import time
import configparser
import

config = configparser.ConfigParser() 
config.read("settings.ini")
client_id = config['system']['id']
def update_presence():
    RPC = Presence(client_id)
    RPC.connect()
    discordPresence = {
        "state": config['config']['state'],
        "details": config['config']['details'],
        "start": config['config']['start'],
        "large_image": config['config']['large_image'],
        "large_text": config['config']['large_text'],
    }
    RPC.update(**discordPresence)
    print("Presence is start!")
if __name__ == "__main__":
    print("""
    ▀█▀ ▒█▀▄▀█ ▒█▀▀▄ 
    ▒█░ ▒█▒█▒█ ▒█░▒█ 
    ▄█▄ ▒█░░▒█ ▒█▄▄▀
    """)
    update_presence()
    os.system("pause")