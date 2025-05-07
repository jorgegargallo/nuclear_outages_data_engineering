import requests
#from src.utils.logger import logger
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os

def get_nuclear_data():
    
    load_dotenv()
    api_key = os.getenv("EIA_API_KEY")
    if not api_key:
        raise ValueError("EIA_API_KEY is not set. Please check your .env file.")
    output_path="data/raw/nuclear_outages_raw.csv"
    url = f"https://api.eia.gov/v2/nuclear-outages/us-nuclear-outages/data/?api_key={api_key}&frequency=daily&data[0]=capacity&data[1]=outage&data[2]=percentOutage&start=2007-01-01&end=2025-01-01&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"


    try:  
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        records = data["response"]["data"]

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df =pd.DataFrame(records)

        df.to_csv(output_path, index=False)
        #logger.info(f"Data saved to {output_path}")
        
        return df

    except requests.exceptions.RequestException as e:
        #logger.error(f"Request failed: {e}")
        print(f"Request failed: {e}")
    except KeyError as e:
        #logger.error(f"Unexpected response structure: {e}")
        print(f"Unexpected response structure: {e}")