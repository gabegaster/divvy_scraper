import urllib, json, pymongo, os
from dateutil.parser import parse

DIVVY_URL = "http://divvybikes.com/stations/json"

def query():
    raw_str = urllib.urlopen(DIVVY_URL).read()
    data = json.loads(raw_str)
    client = pymongo.connection.Connection()
    client['divvy']['hits'].save(data)
    log_me(parse(data['executionTime']))

def log_me(t):
    file_name = os.path.join(os.getenv("HOME"),"divvy_query_log.txt")
    f = open(file_name, "a")
    f.write("query made : %s\n"%t)
    f.close()

if __name__ == '__main__':
    query()


