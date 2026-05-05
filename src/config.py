import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

AMAZON_FILE = os.path.join(DATA_DIR, "amazon_samples.csv")
IMDB_FILE = os.path.join(DATA_DIR, "imdb_samples.csv")
STEAM_FILE = os.path.join(DATA_DIR, "steam_samples.csv")
STEAM_FILE_1 = os.path.join(DATA_DIR, "steam_samples_1.csv")
STEAM_FILE_2 = os.path.join(DATA_DIR, "steam_samples_2.csv")

AMAZON_SAMPLE_SIZE = 200
IMDB_SAMPLE_SIZE = 300
STEAM_TARGET_REVIEWS = 600

AMAZON_DATASET = "snap/amazon-fine-food-reviews"
IMDB_DATASET = "lakshmi25npathi/imdb-dataset-of-50k-movie-reviews"

STEAM_APP_ID_1 = 2868840
STEAM_APP_ID_2 = 570
STEAM_APP_ID_3 = 1172470

STEAM_REVIEW_API_URL = "https://store.steampowered.com/appreviews/"