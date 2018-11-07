import requests, urllib.parse, os
import logging, json

WEBEXTEAMKEY = ""
ROOM_ID = ""
WEBEXTEAMAPIURL = "https://api.ciscospark.com/v1/"

proxies = None


def make_request(url_ext, method, post_data=""):
    url = WEBEXTEAMAPIURL + url_ext
    headers = {
        "Authorization": WEBEXTEAMKEY,
        "Content-Type": "application/json"
    }
    # headers = json.dumps(headers_obj)
    if method == "POST":
        if proxies:
            resp = requests.post(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.post(url, data=post_data, headers=headers)
        if int(resp.status_code / 100) == 2:
            return resp.json()
        return False
    if method == "GET":
        if post_data:
            parameters = urllib.parse.urlencode(post_data)
            url = url + "?" + parameters

        if proxies:
            resp = requests.get(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.get(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            return resp.json()
        return False
    if method == "PUT":
        if proxies:
            resp = requests.put(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.put(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            return True
        return False
    if method == "DELETE":
        if proxies:
            resp = requests.delete(url, data=post_data, headers=headers, proxies=proxies)
        else:
            resp = requests.delete(url, data=post_data, headers=headers)
        if resp.status_code / 100 == 2:
            logger.info("DELETE", url, resp)
            return True
    return False


def sent_notification(msg):
    data = {
        "roomId": ROOM_ID,
        "markdown": msg
    }

    try:
        rep = make_request("messages", "POST", json.dumps(data))

    except Exception as e:
        pass
