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
        loc_url.append((i.location, i.url))
    
    result = pd.DataFrame(loc_url)
    print(result)

    result.drop_duplicates(ignore_index = True)
    result.to_csv("result.csv",mode="w")
    return result

