from time import sleep
from pypresence import Presence
from config import Config

class DiscordRichPresence:
    def __init__(self, config: Config):
        self.config = config
        self.rpc = Presence(self.config.CLIENT_ID)
        self.current_status = None

    def __enter__(self):
        self.rpc.connect()
        print("Rich Presence started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rpc.close()

    def update_presence(self):
        new_status = self.config.as_dict()

        if new_status != self.current_status:
            self.rpc.update(**new_status)
            self.current_status = new_status

    def run(self):
        try:
            while True:
                self.update_presence()
                sleep(self.config.UPDATE_INTERVAL)
        except KeyboardInterrupt:
            print("Rich Presence stopped.")

if __name__ == "__main__":
    with DiscordRichPresence(Config) as discord_presence:
        discord_presence.run()
