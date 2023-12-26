from dataclasses import dataclass

@dataclass
class SofaScore:
    BASE_ENDPOINT = 'https://api.sofascore.com/api/v1/sport/football/scheduled-events/'
    STAT_ENDPOINT = 'https://api.sofascore.com/api/v1/event/UNIQUEGAMEID/statistics'
    INDIVIDUAL_ENDPOINT = 'https://api.sofascore.com/api/v1/event/'

