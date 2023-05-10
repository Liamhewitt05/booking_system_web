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

### Setup development PC
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

### To setup the database

Windows
```bash
.env\Scripts\activate.bat
python main.py
```

Linux / MacOS
```bash
. ./.env/bin/activate
python init_db.py
```

### To create a web service in Azure

Log into Azure

```bash
az login
az account set --subscription "S561-DttM Experimentation"
az deployment group create --resource-group liam-test --template-file Iac\main.bicep
```

## Running Locally

From the root of your cloned repo run the following:

### To run the web server

```bash
python flask run --debug
```

## Running in Azure

https://bookingappcs4m76cgqrrga.azurewebsites.net/

## Refleksjon

* har tidligere brukt json filer for å lagre data, men har funnet ut at databaser funker bedre fordi flere kan bruke samtidig.
* Hadde en plan fra starten, men bestemte meg for å endre noe. Planen var egt flask og react, men ble til Flask, Jinja og vanlig html. Hadde jeg hat mer tid hadde jeg muligens prøvd react.
* Måtte skrive om mye av koden for å gjøre den enklere å lese og forstå.
* Prøvde å lage en nettside i azure som jeg har lært i jobbskyggingen jeg har gjort på onsdag.
* Har laget en backlogg i trello, men kunne vært litt flinkere å oppdatere den oftere. Den viser også framtidig arbeid jeg vil gjøre. https://trello.com/b/EvbGbQOn/77-yff-fri-koding 

