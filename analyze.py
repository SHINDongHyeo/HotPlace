import os
import django
import pandas as pd
import numpy as np
from trip.models import InstaHP

def solution(data):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "HotPlace.settings")
    django.setup()
    
    loc_url = []
    for i in data:
        loc_url.append((i.location, i.url, i.like))
    
    result = pd.DataFrame(loc_url)
    result.columns=["location","url","like"]
    result.drop_duplicates(["url"], inplace=True)
    result.sort_values(by="like",ascending=False, inplace=True)
    result.reset_index(drop=True, inplace=True)

    return result

