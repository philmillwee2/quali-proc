# quali-proc

Performs bulk download of .json files for processing purposes.

## Installation

```
pip install -r requirements.txt
pip install -e .
```

## Usage

You'll need a data folder in the project directory. Store original JSON files in the data/results folder.

```
Usage: proc.py [OPTIONS] FTPASSWD HOST_ADDRESS GAME_PORT

  FTPASSWD        base64 file w/ the FTP username and password.
  HOST_ADDRESS    IP or FQDN of the FTP server.
  GAME_PORT       Port used by ACC server.

Options:
  --port TEXT          Port used for connecting to FTP server.  [required]
  --results_path TEXT  Path to store results mirrored from FTP server.
  --help               Show this message and exit.
```

To use this app run the **proc.py** file using the `python3` command. Assume you have a server at 192.168.1.1, and the ACC service runs on port 9200.

```
python3 proc.py --port 21 .ftpasswd 192.168.1.1 9200
```

## Development

### Installation

This will setup the virtual environment and install any dependencies that you need for development.

```
make setup
```

### Usage

This will require activating the virtual environment where you're doing your development work.

```
source .venv/bin/activate
```

### Cleaning Environments

```
make clean
```
