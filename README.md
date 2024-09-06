
# GamePicker

**GamePicker** is a simple Python command-line program that helps you and your friends choose a game to play together. By using the Steam API, GamePicker finds common games owned by all participants and randomly selects a game to play.

## Features

- Retrieves owned games from multiple Steam accounts.
- Finds common games across all accounts.
- Randomly selects a game from the list of common games.
- Lightweight and easy to use from the command line.

## Quick Start

You can download the latest version of **GamePicker** as a standalone executable file:

1. Go to the [Releases](https://github.com/Pr4c0w1ty/GamePicker/releases) page.
2. Download the `.exe` file from the latest release.
3. Run the downloaded file on your Windows machine.

*Note: Running the executable does not require Python to be installed on your system.*
*but you still need to have your Steam API key*

## Getting a Steam API Key
To use GamePicker, you need to obtain a Steam API key. Follow these steps:

- Go to the [Steam API Key Registration](https://steamcommunity.com/dev/apikey) page.
- Log in with your Steam account credentials.
- Enter a domain name. If you don’t have a domain, you can use localhost or any placeholder domain.
- Click on "Register" to obtain your API key.
- Copy the API key provided, you will use it in the GamePicker program.
  
## Prerequisites

- Python 3.x installed on your system.
- A valid Steam API key.
- `requests` library installed. You can install it using:
```bash
pip install requests
```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Pr4c0w1ty/GamePicker.git
cd GamePicker
```
    
## Usage
1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the program:
```bash
python GamePicker.py
```
4. Enter your Steam API key when prompted.

5. Enter the number of Steam accounts you want to check.

6. Enter each SteamID64 when prompted.

7. Enter how many games do you want to choose.

### Example
```bash
$ python GamePicker.py
Enter your Steam API key: YOUR_STEAM_API_KEY
Enter the number of accounts: 2
Enter the SteamID64 of user 1: 76561198073427512
Enter the SteamID64 of user 2: 76561198073427512
There are 195 common games. How many do you want to choose from? 1
https://store.steampowered.com/app/440/
```
## Issues
If you encounter any problems or have suggestions for improvement, feel free to open an issue on the [GitHub Issues](https://github.com/Pr4c0w1ty/GamePicker/issues) page.
## Contributing

**Contributions are always welcome!**

Please fork the repository and submit a pull request for any changes.


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the [LICENSE](https://github.com/Pr4c0w1ty/GamePicker/blob/main/LICENSE) file for details.


