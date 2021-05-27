from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
from requests_toolbelt import threaded
import requests

t_setup = False

# Setup telegram to send updates - scraping takes a lot of time!
# Create a telegram bot if you don't have on https://core.telegram.org/bots#6-botfather
# Install python-telegram-bot  - pip install python-telegram-bot
t_id = '' #put telegram ID
c_id = '' #put telegram bot chat ID
if t_id and c_id:
    import telegram
    bot = telegram.Bot(token=t_id)
    t_setup = True

headers = {
    'authority': 'steamspy.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://steamspy.com/login/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '',
 }

if not headers['cookie']:
    raise ValueError('Need a login cookie to scrape from SteamSpy.')


def initialize_session(session):
    for (k, v) in headers.items():
        session.headers[k] = v
    return session


def multi_call(ids):
    olist = []
    idsout = []
    responses, errors = threaded.map([{'url': 'https://steamspy.com/app/%i' % (i), 'method': 'GET'} for i in ids],
                                     initializer=initialize_session)
    for r in responses:
        soup = BeautifulSoup(r.response.text, 'html.parser')
        try:
            owners = int(soup.text.split('Owners:')[1].split('Owners')[0].replace(',', ''))
            olist.append(owners)
        except:
            olist.append(-1)
        idsout.append(int(r.request_kwargs['url'].split('/')[-1]))
    return olist, idsout

def test_response():
    response = requests.get('https://steamspy.com/app/10', headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        owners = int(soup.text.split('Owners:')[1].split('Owners')[0].replace(',',''))
        return True
    except:
        return False



idlist = pd.read_csv('games-features.csv')['QueryID']
idlist = idlist[~idlist.duplicated()]
ownerdf = pd.Series(data=np.zeros((len(idlist))), index=idlist)
userscore = pd.Series(data=np.zeros((len(idlist))), index=idlist)


bs = 25

for i in range(len(ownerdf) // bs + 1):

    if (ownerdf[i * bs:(i + 1) * bs] != 0).any():
        continue

    t1 = time.time()
    ids = ownerdf.index[i * bs:(i + 1) * bs]
    olist, idsout = multi_call(ids)

    if ((i + 1) * bs) % 250 == 0:
        if not test_response():
            if t_setup:
                bot.sendMessage(chat_id=c_id, text='SteamSpy failed...')
            raise ValueError('Cannot fetch new values.')

    if ((i + 1) * bs) % 10000 == 0:
        ownerdf.to_csv('steamspy_owners.csv')
        if t_setup:
            bot.sendMessage(chat_id=c_id, text='SteamSpy saving, done %i/%i' % ((i + 1) * bs, len(ownerdf)))

    ownerdf[idsout] = olist

    print('Done %i/%i time remaining %0.02f mn' % (
    (i + 1) * bs, len(ownerdf), ((len(ownerdf) // bs - i) * (time.time() - t1) / 60.0)), end='\r')

ownerdf.to_csv('steamspy_owners.csv')

print((ownerdf!=-1).sum(), ownerdf.shape)

""" Get Userscores """

def multi_call_userscore(ids):
    olist = []
    idsout = []
    responses, errors = threaded.map([{'url': 'https://steamspy.com/app/%i' % (i), 'method': 'GET'} for i in ids],
                                     initializer=initialize_session)
    for r in responses:
        soup = BeautifulSoup(r.response.text, 'html.parser')
        try:
            score = int(soup.text.split('Old userscore:')[1].split('%')[0])
            olist.append(score)
        except:
            olist.append(-1)
        idsout.append(int(r.request_kwargs['url'].split('/')[-1]))
    return olist, idsout


bs = 25

for i in range(len(userscore) // bs + 1):

    if (userscore[i * bs:(i + 1) * bs] != 0).any():
        continue

    t1 = time.time()
    ids = userscore.index[i * bs:(i + 1) * bs]
    olist, idsout = multi_call_userscore(ids)

    if ((i + 1) * bs) % 250 == 0:
        if not test_response():
            if t_setup:
                bot.sendMessage(chat_id=c_id, text='SteamSpy failed...')
            raise ValueError('Cannot fetch new values.' )

    if ((i + 1) * bs) % 10000 == 0:
        userscore.to_csv('steamspy_userscore.csv')
        bot.sendMessage(chat_id=c_id, text='SteamSpy saving, done %i/%i' % ((i + 1) * bs, len(userscore)))

    userscore[idsout] = olist

    print('Done %i %i/%i time remaining %0.02f mn' % ((userscore > 0).sum(), (i + 1) * bs, len(userscore),
                                                      ((len(userscore) // bs - i) * (time.time() - t1) / 60.0)),
          end='\r')

userscore.to_csv('steamspy_userscore.csv')