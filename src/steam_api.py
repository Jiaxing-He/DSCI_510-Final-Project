import requests
import pandas as pd

# For target_reviews, the input should be multiple of 100
def steam_reviews(app_id: int, target_reviews: int, language: str = "english"):
    url = f"https://store.steampowered.com/appreviews/{app_id}"
    all_reviews = []
    negative_cursor = "*"
    positive_cursor = "*"
    while len(all_reviews) < target_reviews:
        params_negative = {
            "json": 1,
            "filter": "recent",
            "language": language,
            "review_type": "negative",
            "purchase_type": "all",
            "num_per_page": 50,
            "cursor": negative_cursor,
        }

        params_positive = {
            "json": 1,
            "filter": "recent",
            "language": language,
            "review_type": "positive",
            "purchase_type": "all",
            "num_per_page": 50,
            "cursor": positive_cursor,
        }
        response_negative = requests.get(url, params=params_negative, timeout=30)
        response_positive = requests.get(url, params=params_positive, timeout=30)

        response_negative.raise_for_status()
        response_positive.raise_for_status()

        negative_reviews = response_negative.json()
        positive_reviews = response_positive.json()


        for review in negative_reviews["reviews"]:
            negative_text = review.get("review", "").replace("\n", " ").strip()
            all_reviews.append({"review": negative_text, "label": 0})

        for review in positive_reviews["reviews"]:
            positive_text = review.get("review", "").replace("\n", " ").strip()
            all_reviews.append({"review": positive_text, "label": 1})

        negative_cursor = negative_reviews.get("cursor")
        positive_cursor = positive_reviews.get("cursor")

    df = pd.DataFrame(all_reviews)

    return df

