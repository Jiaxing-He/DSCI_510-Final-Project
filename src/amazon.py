from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from config import AMAZON_DATASET, AMAZON_SAMPLE_SIZE

def amazon_reviews():
    api = KaggleApi()
    api.authenticate()

    print("Qualified")


    api.dataset_download_files(
        AMAZON_DATASET,
        path="../data",
        unzip=True
    )

    df = pd.read_csv("../data/Reviews.csv")

    sampled_df = df.groupby("Score", group_keys=False).sample(n=AMAZON_SAMPLE_SIZE, random_state=42)

    return sampled_df

