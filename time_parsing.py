
from datetime import datetime

# current date and time
now = datetime.now()

# timestamp = datetime.timestamp(now)
# print("timestamp =", timestamp)
print(now.date())
print(datetime.now().date())

x = datetime.now().date()
print(type(x))
