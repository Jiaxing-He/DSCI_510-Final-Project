from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def imdb_reviews():
    api = KaggleApi()
    api.authenticate()

    print("Qualified")

    api.dataset_download_files(
        "lakshmi25npathi/imdb-dataset-of-50k-movie-reviews",
        path="../data",
        unzip=True
    )

    df = pd.read_csv("../data/IMDB Dataset.csv")

    sampled_df = df.groupby("sentiment", group_keys=False).sample(n=300, random_state=42)

    return sampled_df
