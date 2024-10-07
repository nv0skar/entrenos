# Oscar AG - 2024

try: from typing import List, Tuple # For static type checking
except: pass

import csv

from collections import namedtuple
from pathlib import Path

from datetime import datetime

DEF_PATH = '{}/data/entrenos.csv'.format(Path.cwd())

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

Sessions = List[Entreno]

def lee_entrenos(path: str) -> Entreno:
    with open(path, encoding="utf-8") as f:
        _parsed = csv.reader(f)
        next(_parsed)
        sessions = []
        for l in _parsed: sessions.append(Entreno(l[0], datetime.strptime(l[1], '%d/%m/%Y %H:%M'), l[2], int(l[3]), int(l[4]), float(l[5]), int(l[6]), True if l[7] == 'S' else False))
        return sessions

def tipos_entreno(sessions: Sessions) -> List[str]:
    kinds = set()
    for session in sessions: kinds.add(session[0])
    return sorted(kinds)

def entrenos_duracion_superior(sessions: Sessions, threshold: int) -> Sessions:
    return list(filter(lambda session: True if session[3] > threshold else False, sessions))

def suma_calorias(sessions: Sessions, dates: Tuple[datetime, datetime]) -> Sessions:
    calories = 0
    for session in sessions:
        if dates[0] <= session[1] <= dates[1]:
            calories += session[4]
    return calories