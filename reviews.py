import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

reviews.head()

updated_reviews = reviews.groupby('country').agg({"country": "count", "points": "mean"}).round(1)
updated_reviews_2 = updated_reviews.rename(columns={"country": "count"})
updated_reviews_2.sort_values('count', ascending = False, inplace = True)
updated_reviews_2

updated_reviews_2.to_csv('C:/Users/randa/github-classroom/CLCK-Data-May2023/wine-reviews-exercise-randallcode/data/reviews-per-country.csv')