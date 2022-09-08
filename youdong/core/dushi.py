import requests
base_url = 'http://dushitime.test.commpad.cn/cmd_t.php?tpass=abcddd123&sevid=1&uid='


def cmd(uid, data):
    url = base_url + str(uid)
    return requests.post(url, json=data)


def modify(uid, data):
    url = base_url + 'api/test_py_json.php?uid=' + str(uid)
    return requests.post(url, json=data)
