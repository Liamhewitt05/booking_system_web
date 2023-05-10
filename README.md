# Booking system 

Booking system for various items or rooms (school)

## Prerequisites

Before starting, install the following tools:

- Python 3.10 or later
- Pip package manager

For more information on these tools, see the public documentation on
[Python](https://www.python.org/downloads/) or
[Pip](https://pip.pypa.io/en/stable/installing/)

## Initial Setup

From the root of your cloned repo, generate a virtual environment with a
specific version of python.

Windows
```bash
python -m venv .env
.env\Scripts\activate.bat
```

Linux / MacOS
```bash
python3 -m venv .env
. ./.env/bin/activate
```

Next install any necessary packages.

```bash
pip install -r requirements.txt
```

## Running

From the root of your cloned repo run:

Windows
```bash
.env\Scripts\activate.bat
python main.py
```

Linux / MacOS
```bash
. ./.env/bin/activate
python main.py
```

## Refleksjon

* har tidligere brukt json filer for å lagre data, men har funnet ut at databaser funker bedre fordi flere kan bruke samtidig.
* Hadde en plan fra starten, men bestemte å endre noe FLASK + REACT -> FLASK WITH JINJA + HTML. MNight try using React later if time.
* I had to refactor my code to make it easier to understand.