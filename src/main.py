from asyncio import sleep, CancelledError, run
from pypresence import Presence
from config import Config

class DiscordRichPresence:
    def __init__(self, config: Config):
        self.config = config
        self.rpc = Presence(self.config.CLIENT_ID)
        self.current_status = None

    async def __aenter__(self):
        self.rpc.connect()
        print("Rich Presence started")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.rpc.close()

    async def update_presence(self):
        new_status = self.config.as_dict()

        if new_status != self.current_status:
            self.rpc.update(**new_status)
            self.current_status = new_status

    async def run(self):
        try:
            while True:
                await self.update_presence()
                await sleep(self.config.UPDATE_INTERVAL)
        except CancelledError:
            print("Rich Presence stopped.")

if __name__ == "__main__":
    
    async def main():
        async with DiscordRichPresence(Config) as discord_presence:
            await discord_presence.run()

    run(main())
 