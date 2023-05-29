#Write a Python program to convert unix timestamp string to readable date
from datetime import datetime
timestamp=1920293487
date_time=datetime.fromtimestamp(timestamp)
print("Date from timestamp:",date_time)
date=date_time.strftime("%d/%m/%Y")
print("converted Unix timestamp:",date)