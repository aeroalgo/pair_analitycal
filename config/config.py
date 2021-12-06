from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")

ma_type = {
    'all': 'random',
    '6': 'DEMA',
    '1': 'EMA',
    '5': 'LRMA',
    '4': 'AMA',
    '0': 'SMA',
    '8': 'T3',
    '7': 'TEMA',
    '2': 'WMA',
}
