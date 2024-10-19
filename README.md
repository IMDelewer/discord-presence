<div align="center">
    <img src="src/images/icon.png" alt="Discord Rich Presence" width="200" height="200" />
</div>

<div align="center">
    <h1>Discord Rich Presence</h1>
</div>


## Description

Discord Rich Presence is a tool for displaying your status in Discord, allowing you to integrate various parameters such as current activity, image, and other information.

## Русская версия

Вы можете прочитать README на русском языке [здесь](src/docs/README_RU.MD).

---

### Tags

- **Programming Language**: Python
- **Python Version**: 3.7 and above
- **Libraries**:
  - `pypresence`
  - `asyncio` (for asynchronous execution)

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/IMDelewer/repo.git
    cd repo
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the `config.py` file according to your requirements.
2. Run the application:

    ```bash
    python src/main.py
    ```

## Configuration

In the `config.py` file, you can configure the following parameters:

- `CLIENT_ID`: Your application ID in Discord.
- `UPDATE_INTERVAL`: The interval for updating the status (in seconds).
- Additional parameters that you wish to set.

## Features

- Update your status in Discord.
- Customize your status and image.
- Works with asynchronous updates.

## Notes

- Make sure you have Python 3.7 or above installed.
- Use `.png` or `.jpg` files for images.

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for more information.

## Contribution

If you would like to contribute to this project, please fork the repository, make your changes, and create a pull request.

