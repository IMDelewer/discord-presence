
# Discord Rich Presence with Python (Async)

This project implements Discord Rich Presence using Python's `pypresence` library with asynchronous support through `asyncio`. It allows you to display custom status in Discord, with images and buttons, and manage the configuration through a dedicated [config.py](src/config.py) file.

## Features
- Asynchronous updates using `asyncio`.
- Custom configuration stored in `config.py`.
- Supports large and small images.
- Custom buttons with URLs.
- Automatic status update every specified interval.
- Only updates presence when values change (optimized for performance).

## Installation

1. Clone the repository or download the code.
2. Install the required dependencies:
   ```bash
   pip install pypresence
   ```

3. Configure your Discord Rich Presence by editing `config.py`:
   ```python
   class DiscordConfig:
       CLIENT_ID = "your_client_id"  # Replace with your Discord Application Client ID
       LARGE_IMAGE = "large_image_key"  # Optional: Large image key from your Discord Developer Portal
       SMALL_IMAGE = None  # Optional: Small image key or leave it None
       STATE = "Playing AlphaCraft"
       DETAILS = "Building Minecraft plugin"
       BUTTONS = [
           {"label": "Join Us", "url": "https://your-url.com"},
           {"label": "Learn More", "url": "https://your-other-url.com"}
       ]
       UPDATE_INTERVAL = 15  # Time interval for updating the status (in seconds)
   ```

4. Run the project:
   ```bash
   python main.py
   ```

## How to Use

- **Configurable Fields:**
   - `CLIENT_ID`: Your application's Discord Client ID (required).
   - `LARGE_IMAGE`: The key for the large image you want to display (optional).
   - `SMALL_IMAGE`: The key for the small image (optional, can be `None`).
   - `STATE`: A short status line (e.g., "Playing AlphaCraft").
   - `DETAILS`: A detailed description (e.g., "Building Minecraft plugin").
   - `BUTTONS`: List of buttons with `label` and `url` (optional).
   - `UPDATE_INTERVAL`: How frequently to update the presence (in seconds).

- **Images:**
   - You must upload your images to Discord Developer Portal and use their keys in the `LARGE_IMAGE` and `SMALL_IMAGE` fields.

- **Status Update:**
   - The status will only update if there are changes, reducing the number of unnecessary updates.

## Example Configuration

```python
class DiscordConfig:
    CLIENT_ID = "123456789012345678"  # Your actual Client ID
    LARGE_IMAGE = "minecraft_logo"
    SMALL_IMAGE = None  # No small image
    STATE = "Playing MineCraft"
    DETAILS = "Building Minecraft plugin"
    BUTTONS = [
        {"label": "Join Us", "url": "https://discord.gg/yourserver"},
        {"label": "Learn More", "url": "https://yourwebsite.com"}
    ]
    UPDATE_INTERVAL = 15  # Update every 15 seconds
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contribution

Feel free to submit pull requests, suggest improvements, or report issues.
