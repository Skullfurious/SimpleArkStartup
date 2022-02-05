## Simple Ark Startup

This project is a simple Ark Server startup script that is written in Python 3. It provides a dynamic difficulty option as well so you can have a bit more of a fluid experience over a period of time.

## Requirements

First lets check and see if Python came pre-installed on your server.

```bash
python --version
```

If you get Python 3.8.10 or greater you should be good to go. Keep in mind that this script assumes your distribution is following the new guidelines of the official Ubuntu distribution and python3 is named python system wide. If you get an error run the following command:

```bash
apt-get install python-is-python3 -y
```

## Installation

Download or clone this repository to your desired folder. The folder will require a symlink to the ark server's directory named `arkserverdirectory` (Where steam installed it). The symlink looks like the following on my system:
```bash
arkserverdirectory -> /home/ark/.steam/steam/steamcmd/ark
```
You can create one like I have by using the command
```bash
ln -s ./arkserverdirectory /home/ark/.steam/steam/steamcmd/ark
```
## Usage

Simply run `./main.py` and it should generate a configuration file. Edit the configuration file to your liking and run `./main.py` once more.

**Warning: The password options cannot contain spaces.**
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
