from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def amazon_reviews():
    api = KaggleApi()
    api.authenticate()

    print("Qualified")


    api.dataset_download_files(
    "snap/amazon-fine-food-reviews",
        path="../data",
        unzip=True
    )

    df = pd.read_csv("../data/Reviews.csv")

    sampled_df = df.groupby("Score", group_keys=False).sample(n=200, random_state=42)

    return sampled_df

