from dataclasses import dataclass

# have default headers to supply

class RequestConfig:
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
               'Cache-Control': 'max-age-0'}