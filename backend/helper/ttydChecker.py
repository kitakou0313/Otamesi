import urllib.request


def comfirmTtydStart(podName):
    req = urllib.request.Request("http://" + podName+":7681")
    try:
        with urllib.request.urlopen(req) as res:
            return res.status
    except urllib.error.HTTPError as err:
        return err.code
    except urllib.error.URLError as err:
        return err
