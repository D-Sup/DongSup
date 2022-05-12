from datetime import datetime, timedelta
yesterday = datetime.today() - timedelta(1)
print(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))
print(yesterday.strftime('%A, %B %d, %Y %H:%M:%S'))