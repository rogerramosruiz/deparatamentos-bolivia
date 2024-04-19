from dotenv import load_dotenv
import os

load_dotenv(override=True)
POSTGRESDB_URL = os.getenv('POSTGRESDB_URL')