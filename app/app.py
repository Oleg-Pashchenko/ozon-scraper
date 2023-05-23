import time

from app.database import Database
from app.scraper import Scraper


def start_app():
    database = Database()
    scraper = Scraper()
    fl = False
    while True:
        if not fl:
            table_name = 'kamran'
            fl = True
        else:
            fl = False
            table_name = 'oleg'
        dbobj = database.get_code(table_name)
        print(table_name, dbobj)
        if not dbobj:
            time.sleep(10)
            continue
        try:
            item = scraper.scrape_item(dbobj.s_name)
        except Exception:
            item = []
        print(item)
        database.update_item(item, dbobj, table_name)
