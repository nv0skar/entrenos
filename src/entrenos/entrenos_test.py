# Oscar AG - 2024

from entrenos import *

def test_read(path: str) -> Sessions:
    sessions = lee_entrenos(path)
    print('First 3 sessions: {}\nLast 3 sessions: {}\n'.format(sessions[:3], sessions[-3::]))
    return sessions

def test_tipos_entreno(sessions: Sessions):
    kinds = tipos_entreno(sessions)
    print('Types of training kinds: {}\n'.format(kinds))

def test_entrenos_duracion_superior(sessions: Sessions, threshold: int):
    sessions_threshold = entrenos_duracion_superior(sessions, threshold)
    print('Sessions with a duration greater than {}: {}\n'.format(threshold, sessions_threshold))

def test_suma_calorias(sessions: Sessions, dates: Tuple[datetime, datetime]):
    calories = suma_calorias(sessions, dates)
    print('Calories burned from {} through {}: {}\n'.format(dates[0], dates[1], calories))

if __name__ == '__main__':
    sessions = test_read(DEF_PATH)
    test_tipos_entreno(sessions)
    test_entrenos_duracion_superior(sessions, int(input('Duration threshold >> ')))
    test_suma_calorias(sessions, (datetime.strptime('01/01/2019', '%d/%m/%Y'), datetime.strptime('01/01/2020', '%d/%m/%Y')))
