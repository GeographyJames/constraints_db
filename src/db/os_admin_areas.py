from .models import AdministrativeArea
from .sqlalchemy_config import engine, credentials_from_ini
from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy import select


OS_grid_tiles = [['SV', 'SW', 'SX', 'SY', 'SZ', 'TV', None],
                 [None, 'SR', 'SS', 'ST', 'SU', 'TQ', 'TR'],
                 [None, 'SM', 'SN', 'SO', 'SP', 'TL', 'TM'],
                 [None, None, 'SH', 'SJ', 'SK', 'TF', 'TG'],
                 [None, None, 'SC', 'SD', 'SE', 'TA', None],
                 [None, 'NW', 'NX', 'NY', 'NZ', 'OV', None],
                 [None, 'NR', 'NS', 'NT', 'NU', None, None],
                 ['NL', 'NM', 'NN', 'NO', None, None, None],
                 ['NF', 'NG', 'NH', 'NJ', 'NK', None, None],
                 ['NA', 'NB', 'NC', 'ND', None, None, None],
                 [None, 'HW', 'HX', 'HY', 'HZ', None, None],
                 [None, None, None, 'HT', 'HU', None, None],
                 [None, None, None, None, 'HP', None, None]]

if __name__ == "__main__":
    eng = engine(credentials_from_ini(Path("db_credentials.ini")), echo=True)
    session = Session(eng)
    for line in OS_grid_tiles:
        for tile in line:
            if tile:
                res = session.scalar(select(AdministrativeArea).where(AdministrativeArea.abbreviation == f"OS {tile}"))
                if not res:
                    session.add(AdministrativeArea(
                        name=f"National Grid {tile}",
                        abbreviation=f"OS {tile}",
                        parent_area_id=6))
    session.commit()


            

