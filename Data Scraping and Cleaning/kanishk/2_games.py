#!/usr/env/bin python


"""
File taken from https://github.com/CraigKelly/steam-data
Create games.json using ID's in idlist.csv.
"""

# pylama:ignore=E501

import csv
import json
import time
import requests
import logging


logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

def parse_id(i):
    """Since we deal with both strings and ints, force appid to be correct."""
    try:
        return int(str(i).strip())
    except:
        return None


def id_reader():
    """Read the previous created idlist.csv."""
    with open("idlist.csv") as basefile:
        reader = csv.DictReader(basefile)
        for row in reader:
            yield parse_id(row['ID']), row['Name']


def previous_results():
    """Return a set of all previous found ID's."""
    all_ids = set()
    with open("games.json") as f:
        for line in f:
            rec = json.loads(line)
            appid = parse_id(rec.get('query_appid', None))
            if appid:
                all_ids.add(appid)
    return all_ids


def main():
    """Entry point."""
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('requests').setLevel(logging.DEBUG)
    log = logging.getLogger('games')

    defaults = {
        'cc': 'US',
        'l': 'english',
        'v': '1',
    }
    log.info("Default parameters: %s", repr(defaults))

    URL = "http://store.steampowered.com/api/appdetails/"
    LIMIT = 350
    WAIT_TIME = (1 * 60) + 10  # 5 minutes plus a cushion

    log.info("Getting previous results from games.json")
    previos_ids = previous_results()

    log.info("Opening games.json")
    with open("games.json", "a") as f:
        count, batch_count = 0, 0

        log.info("Opening idlist.csv")
        for appid, appname in id_reader():
            if appid in previos_ids:
                print("Skipping previously found id %d", appid, end='\r')
                count += 1
                continue

            req_data = dict(defaults)
            req_data['appids'] = str(appid)

            resp_data = requests.get(URL, params=req_data)
 
            # Loop is an artifact of Steam's past suppot for multiple appid
            # queries: we use it to insure we got back what we asked for - the
            # details for appid
            try:
                resp_data.json() 
            except Exception as E:
                print('Something wrong with resp_data for %i, skipping'%appid)
                continue
            while resp_data.json() is None:
                print('None response found for appid %i, waiting...'%appid)
                log.info("count is %i, batch count is %d, waiting for %d secs", count, batch_count, WAIT_TIME)
                time.sleep(WAIT_TIME)
                batch_count = 0
                resp_data = requests.get(URL, params=req_data)
            
            for result_appid, game in resp_data.json().items():
                if parse_id(result_appid) != appid:
                    log.error("Invalid - %s does not match requested id %d", result_appid, appid)

                game['query_appid'] = appid
                game['query_appname'] = appname
                f.write(json.dumps(game) + '\n')

                count += 1

            batch_count += 1
#             if batch_count >= LIMIT:
#                 log.info("batch count is %d, waiting for %d secs", batch_count, WAIT_TIME)
#                 time.sleep(WAIT_TIME)
#                 batch_count = 0
            print(count, end='\r')
    log.info("Game records written: %d", count)


if __name__ == "__main__":
    main()
