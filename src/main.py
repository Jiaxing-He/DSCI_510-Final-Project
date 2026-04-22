import pandas as pd
import re
from scipy.stats import pointbiserialr
from amazon import amazon_reviews
from imdb import imdb_reviews
from steam_api import steam_reviews
from langdetect import detect

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r"<.*?>", "", text)   # remove HTML tags
    text = re.sub(r"\s+", " ", text).strip()
    return text

def get_review_length(text):
    return len(str(text).split())

def load_amazon(file_path):
    df = pd.read_csv(file_path)

    df = df[["Score", "Text"]].copy()
    df = df.dropna(subset=["Score", "Text"])

    df = df[df["Score"].isin([1, 2, 4, 5])].copy()
    df["label"] = df["Score"].apply(lambda x: 0 if x in [1, 2] else 1)

    df = df.rename(columns={"Text": "review"})
    df["review"] = df["review"].apply(clean_text)
    df["review_length"] = df["review"].apply(get_review_length)
    df["source"] = "Amazon"

    return df[["source", "review", "review_length", "label"]]


def load_imdb(file_path):
    df = pd.read_csv(file_path)

    df = df[["review", "sentiment"]].copy()
    df = df.dropna(subset=["review", "sentiment"])

    df["label"] = df["sentiment"].map({"negative": 0, "positive": 1})
    df = df.dropna(subset=["label"])

    df["review"] = df["review"].apply(clean_text)
    df["review_length"] = df["review"].apply(get_review_length)
    df["source"] = "IMDb"

    return df[["source", "review", "review_length", "label"]]


def load_steam(file_path):
    df = pd.read_csv(file_path)

    df = df[["review", "label"]].copy()
    df = df.dropna(subset=["review", "label"])

    if df["label"].dtype == object:
        df["label"] = df["label"].astype(str).str.lower().map({
            "negative": 0,
            "positive": 1
        })

    df = df.dropna(subset=["label"])
    df["label"] = df["label"].astype(int)

    df["review"] = df["review"].apply(clean_text)
    df["review_length"] = df["review"].apply(get_review_length)
    df["source"] = "Steam"

    return df[["source", "review", "review_length", "label"]]


def analyze_dataset(df, name):
    print(f"\n{'=' * 50}")
    print(f"{name} Analysis")
    print(f"{'=' * 50}")

    print("\nLabel counts:")
    print(df["label"].value_counts().sort_index())

    print("\nReview length statistics by label:")
    print(df.groupby("label")["review_length"].describe())

    corr, p_value = pointbiserialr(df["label"], df["review_length"])
    print("\nPoint-biserial correlation between review_length and label:")
    print(f"Correlation: {corr:.4f}")
    print(f"P-value: {p_value:.4f}")

    if corr > 0:
        print("Interpretation: Longer reviews tend to be more positive.")
    elif corr < 0:
        print("Interpretation: Longer reviews tend to be more negative.")
    else:
        print("Interpretation: No linear relationship found.")

def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False

def main():
    app_id = 2868840
    steam_data = steam_reviews(app_id=app_id, target_reviews=600)

    steam_data = steam_data[steam_data["review"].apply(is_english)]
    steam_data.to_csv("../data/steam_samples.csv", encoding="utf-8-sig", index=False)

    amazon_data = amazon_reviews()
    amazon_data.to_csv("../data/amazon_samples.csv", index=False)

    imdb_data = imdb_reviews()
    imdb_data.to_csv("../data/imdb_samples.csv", index=False)

    amazon_file = "../data/amazon_samples.csv"
    imdb_file = "../data/imdb_samples.csv"
    steam_file = "../data/steam_samples.csv"

    amazon_df = load_amazon(amazon_file)
    imdb_df = load_imdb(imdb_file)
    steam_df = load_steam(steam_file)

    analyze_dataset(amazon_df, "Amazon")
    analyze_dataset(imdb_df, "IMDb")
    analyze_dataset(steam_df, "Steam")

    app_id_1 = 570
    steam_data_1 = steam_reviews(app_id=app_id_1, target_reviews=600)
    steam_data_1 = steam_data_1[steam_data_1["review"].apply(is_english)]
    steam_data_1.to_csv("../data/steam_samples_1.csv", encoding="utf-8-sig", index=False)
    steam_file_1 = "../data/steam_samples_1.csv"
    steam_df_1 = load_steam(steam_file_1)
    analyze_dataset(steam_df_1, "Steam")

    app_id_2 = 1172470
    steam_data_2 = steam_reviews(app_id=app_id_2, target_reviews=600)
    steam_data_2 = steam_data_2[steam_data_2["review"].apply(is_english)]
    steam_data_2.to_csv("../data/steam_samples_2.csv", encoding="utf-8-sig", index=False)
    steam_file_2 = "../data/steam_samples_2.csv"
    steam_df_2 = load_steam(steam_file_2)
    analyze_dataset(steam_df_2, "Steam")

if __name__ == "__main__":
    main()