from steam_api import steam_reviews

app_id = 2868840
data = steam_reviews(app_id=app_id, target_reviews=500)
print(data)


