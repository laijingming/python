import requests


def is_odd(n):
    return n % 2 == 1


res = requests.post(
    'http://dushitime.test.commpad.cn/cmd_t.php?tpass=abcddd123&uid=1000465&sevid=1',
    json={
        "huodong2": {
            "hd3063Info": {}
        }
    }
)
print(res.text)
