# Analysis of Review Length and Sentiment
This project investigates whether longer user reviews are associated with more positive ratings. The study will analyze review data from online platforms of different fields to examine the relationship between review length and rating scores. By applying statistical analysis, the project aims to determine whether longer reviews tend to be more positive or negative.

# Data sources
| Data Source# | Name / short description | Source URL | Type | List of Fields | Format | Estimated Data Size |
|--------------|------------------|-----------|------|-------------|--------|----------------|
| 1 | Steam Reviews (ID: 570) | https://store.steampowered.com/appreviews/570 | API | review, label | JSON | 600 |
| 2 | Steam Reviews (ID: 2868840) | https://store.steampowered.com/appreviews/2868840 | API | review, label | JSON | 600 |
| 3 | Steam Reviews (ID: 1172470) | https://store.steampowered.com/appreviews/1172470 | API | review, label | JSON | 600 |
| 4 | Amazon Fine Food Reviews | https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews | File | review, scoring | csv | 500,000 |
| 5 | IMDB Movie Reviews | https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews| File | review, sentiment | csv | 50,000 |

# Results 
Steam showed a significant negative relationship, while Amazon and IMDb’s results are insignificant. In conclusion, User behaviors may be different across platforms. For steam particularly, longer reviews tended to be more negative.

# Installation
The user must have kaggle API keys to run the project.

Python packages:
pandas
kaggle
langdetect
scipy

# Running analysis 
_update these instructions_

From `src/` directory run:

`python main.py `

Results will appear in `results/` folder. All obtained will be stored in `data/`
