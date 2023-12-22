import asyncio
import aiohttp
from config import RequestConfig
from tabulate import tabulate
from datetime import datetime, timedelta

async def send_request(url, headers = RequestConfig.HEADERS, get=True):
    
    # account for request caching 
    headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'

    async with aiohttp.ClientSession() as session:
        if get:
            async with session.get(url, headers=headers) as response:
                return await response.json()
        else:
            async with session.post(url, headers=headers) as response:
                return await response.json()

async def fetch_event_data(request_queue):
    tasks = [asyncio.ensure_future(send_request(url)) for url in request_queue]
    responses = await asyncio.gather(*tasks)
    return responses

async def generate_live_games(url):
    response = await send_request(url = url, get=True)
    return response


# generate_date_list will return a list of dates formatted as 'YYYY-MM-DD'
# The start date is the current day the code is being ran, the end_date is the date you want the data retrieved to
# Example: start_date = 2023/12/12 and end_date = 2023/01/01

def generate_date_list(start_date, end_date):
    date_list = []
    
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    while current_date >= end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date -= timedelta(days=1)
    
    return date_list
