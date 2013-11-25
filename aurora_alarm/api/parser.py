import json
import re
import urllib
import urllib2


class AuroraParser():
    """
    Class for parsing Aurora daily forecast from http://www.gi.alaska.edu/AuroraForecast/Europe/.
    """

    def __init__(self, year, month, day):
        self.aurora_value = None
        self.url = "http://www.gi.alaska.edu/AuroraForecast/Europe/" + str(year) + "/" + str(month) + "/" + str(day)
        self.contents = ''
        self.download()
        self.get_aurora_value()

    def download(self):
        """
        Function downloads HTML document from the provided URL.
        """
        browser = urllib.urlopen(self.url)
        response = browser.getcode()

        if response == 200:
            self.contents = browser.read()
        else:
            print "Website is not reachable!"

    def get_aurora_value(self):
        """
        Function parses aurora value from HTML. It checks for all 10 different values.
        If something goes wrong, returns None.
        """

        try:
            self.aurora_value = (
                 re.search(r'"level-0n">(\d)', self.contents) or re.search(r'"level-1n">(\d)', self.contents)
              or re.search(r'"level-2n">(\d)', self.contents) or re.search(r'"level-3n">(\d)', self.contents)
              or re.search(r'"level-4n">(\d)', self.contents) or re.search(r'"level-5n">(\d)', self.contents)
              or re.search(r'"level-6n">(\d)', self.contents) or re.search(r'"level-7n">(\d)', self.contents)
              or re.search(r'"level-8n">(\d)', self.contents) or re.search(r'"level-9n">(\d)', self.contents)
            ).group(1)
        except:
            self.aurora_value = None


# TODO: Simplify!
def save_value_to_database(date, value):
    """
    This function sends POST request to API.
    """
    API_URL = "http://127.0.0.1:8000/api/" #TODO: Read this setting from aurora_alarm settings.

    # check if value for this date already exist
    url = API_URL + "aurora_daily_forecast/?date=" + date

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    f = urllib2.urlopen(req);
    data = f.read();
    f.close();
    object = json.loads(data)


    # if there is no data for this date in database, save this value
    if object["count"] == 0:
        url = API_URL + "aurora_daily_forecast/"
        data = {"current_value": value, "first_value": value, "date": date}

        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')

        f = urllib2.urlopen(req, json.dumps(data))
        f.close()

    # data for that date already exists, just update value
    else:
        object_id = object["results"][0]["id"]
        first_value = object["results"][0]["first_value"]

        url = API_URL + "aurora_daily_forecast/" + str(object_id) + "/"
        data = {"current_value": value, "first_value": first_value, "date": date}

        req = urllib2.Request(url)
        req.get_method = lambda: 'PUT'
        req.add_header('Content-Type', 'application/json')

        f = urllib2.urlopen(req, json.dumps(data))
        f.close()

def run_parser():
    """
    Parse all aurora activity values between 2010-01-01 and 2013-12-12.
    """

    for year in range(2011, 2014):
        for month in range (1,13):
            for i in range(1,31):
                aurora_parser = AuroraParser(year, month, i)
                date = str(year) + "-" + str(month) + "-" + str(i)

                print date, aurora_parser.aurora_value

                # Save values to django database. Call REST api and send POST request for each daily aurora value.
                if aurora_parser.aurora_value != None:
                    try:
                        save_value_to_database(date, aurora_parser.aurora_value)
                    except:
                        print "Can't save to the database."


if __name__ == '__main__':
    run_parser()
