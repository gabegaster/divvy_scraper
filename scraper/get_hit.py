from scraper.models import Hit, Station
import urllib, json, time
from dateutil.parser import parse

DIVVY_URL = "http://divvybikes.com/stations/json"

def query():
    raw_str = urllib.urlopen(DIVVY_URL).read()
    data = json.loads(raw_str)
    t = parse(data['executionTime'])
    log_me()
    hit = Hit(execution_time=t)
    hit.save()
    for station_json in data['stationBeanList']:
        station = make_station(station_json, hit)
        station.save()

def log_me():
    f = open(os.path.join(os.getenv("HOME"),"divvy_query_log.txt"),"a")
    f.write("query made : %s"%time.ctime())
    f.close()
    print "  execution time ",t

def make_station(obj, hit):
    s = Station(hit=hit)
    s.available_bikes = obj['availableBikes']
    s.available_docks = obj['availableDocks']
    s.city = obj['city']
    s.bean_id = obj['id']
    s.landmark = obj['landMark']
    s.location = obj['location']
    s.longitude = obj['longitude']
    s.stAddress = obj['stAddress1']
    s.station_name = obj['stationName']
    s.status_key = obj['statusKey']
    s.status_value = obj['statusValue']
    s.test_station = obj['testStation']
    s.total_docks = obj['totalDocks']
    return s

if __name__ == "__main__":
    query()
