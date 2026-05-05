from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from config import IMDB_DATASET, IMDB_SAMPLE_SIZE

def imdb_reviews():
    api = KaggleApi()
    api.authenticate()

    print("Qualified")

    api.dataset_download_files(
        IMDB_DATASET,
        path="../data",
        unzip=True
    )

    df = pd.read_csv("../data/IMDB Dataset.csv")

    sampled_df = df.groupby("sentiment", group_keys=False).sample(n=IMDB_SAMPLE_SIZE, random_state=42)

    return sampled_df
