from aurora_alarm.settings import API_URL

import json
import urllib2


def get_object_from_api(url):
    """
    This utility function get JSON from provided url. It loads just first object and returns it as Python object.
    API_URL is set in settings.py.
    """
    url = API_URL + url

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    f = urllib2.urlopen(req)
    data = f.read()
    f.close()

    return json.loads(data)['results'][0]
