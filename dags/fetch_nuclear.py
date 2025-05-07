import requests
from src.utils.logger import logger
import pandas as pd
from pathlib import Path

def get_nuclear_data():
    start="2024-01-01",
    end="2025-01-01",
    output_path="data/raw/nuclear_outages_raw.csv"
    url = "https://api.eia.gov/v2/nuclear-outages/us-nuclear-outages/data/?frequency=daily&data[0]=capacity&data[1]=outage&data[2]=percentOutage&start=2024-01-01&end=2025-01-01&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
    logger.info(f"Fetching data from EIA API between {start} and {end}")

    try:  
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        records = data["response"]["data"]

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        df =pd.Dataframe(records)

        df.to_csv(output_path, index=False)
        logger.info(f"Data saved to {output_path}")
        
        return df

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
    except KeyError as e:
        logger.error(f"Unexpected response structure: {e}")
   