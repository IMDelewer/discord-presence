class Config:
    CLIENT_ID = "your_client_id"
    LARGE_IMAGE = "large_image_key"
    SMALL_IMAGE = "small_image_key"
    STATE = "Playing AlphaCraft"
    DETAILS = "Building Minecraft plugin"
    BUTTONS = [
        {"label": "Join Us", "url": "https://your-url.com"},
        {"label": "Learn More", "url": "https://your-other-url.com"}
    ]
    UPDATE_INTERVAL = 15

    @classmethod
    def as_dict(cls):

        config = {
            "state": cls.STATE,
            "details": cls.DETAILS,
            "large_image": cls.LARGE_IMAGE,
            "small_image": cls.SMALL_IMAGE,
            "buttons": cls.BUTTONS
        }

        return {k: v for k, v in config.items() if v is not None}