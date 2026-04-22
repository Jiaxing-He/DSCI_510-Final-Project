from steam_api import steam_reviews
from amazon import amazon_reviews
from imdb import imdb_reviews
from langdetect import detect


app_id = 2868840
steam_data = steam_reviews(app_id=app_id, target_reviews=500)
def is_english(text):
    try:
        return detect(text) == "en"
    except:
        return False

steam_data = steam_data[steam_data["review"].apply(is_english)]
steam_data.to_csv("../data/steam_samples.csv", encoding="utf-8-sig", index=False)
print(steam_data.head(10))

amazon_data = amazon_reviews()
amazon_data.to_csv("../data/amazon_samples.csv", index=False)
print(amazon_data)

imdb_data = imdb_reviews()
imdb_data.to_csv("../data/imdb_samples.csv", index=False)
print(imdb_data)
