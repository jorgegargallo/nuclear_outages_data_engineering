## Project Structure

The project is organized as follows:

```
nuclear_outages_data_engineering/
│
├── data/
│   ├── raw/                # Directory for raw data files
│   ├── processed/          # Directory for processed data files
│
│
├── src/                    # Source code for the project
│   ├── ingest/             # Scripts for data ingestion
│   ├── process/            # Scripts for data processing
│   ├── utils/              # Additional tools
│
├── tests/                  # Unit tests for validating the codebase
│                   
│
├── README.md               # Project overview and instructions
│
└── requirements.txt        # Python dependencies for the project
│
└── dev.env                 # Environment variables

```

## API Access Code

The `src/api/fetch_data.py` script is used to interact with external APIs to fetch data. It provides a reusable function to make GET requests to APIs and handle responses. 

### Configuration
- Ensure you configure the API endpoint and authentication details as required for your use case.
- For the EIA Nuclear Dataset, an `API_Key` is required. It is recommended to store sensitive information like API keys in a `.env` file for security and ease of configuration.

### Using a `.env` File
- Create a `.env` file in the root directory of your project.
- Add the API key in the following format:
    ```
    API_KEY=your_api_key_here
    ```
- The `.env` file must be named exactly `.env` to ensure it is correctly loaded by environment variable management libraries (e.g., `python-dotenv`).

### Security Note
- Do not commit the `.env` file to version control. Add `.env` to your `.gitignore` file to prevent accidental exposure of sensitive information.

The `src/api/fetch_data.py` script is used to interact with external APIs to fetch data. It provides a reusable function to make GET requests to APIs and handle responses. Ensure you configure the API endpoint and authentication details as required for your use case. For EIA Nueclear Dataset a API_Key is required
