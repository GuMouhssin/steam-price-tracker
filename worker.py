from db import init_db
from tracker import track_prices


init_db()


print("Running scheduled price check...")
track_prices()
print("Done.")