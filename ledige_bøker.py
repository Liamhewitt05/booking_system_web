import json
from dataclasses import dataclass

@dataclass
class Bok:
    """klasse som holder bok navn og antall"""

    navn: str
    antall: int

def last_inn_ledige_bøker():
    """leser ledige bøker"""
    data = open("Ledige_bøker.json", "r").read()
    data = json.loads(data)
    liste = []
    for bok_navn, value in data["alle_boker"].items():
        liste.append(Bok(navn=bok_navn, antall=value["antall"]))
    return liste

navn = input("Lån bok:\n")

ledige_bøker = last_inn_ledige_bøker()
funnet_bok = None
for bok in ledige_bøker:
    if bok.navn == navn:
        funnet_bok = bok

if funnet_bok is not None:
    print("Riktig")
else:
    print("feil")