import urllib
import re

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


if __name__ == '__main__':
    year = 2013
    month = 11

    for i in range(1,31):
        aurora_parser = AuroraParser(year, month, i)
        print i, aurora_parser.aurora_value
