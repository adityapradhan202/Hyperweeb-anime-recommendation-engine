import pandas as pd
import numpy as np

anime_df = pd.read_csv('anime_data_2023.csv')

drop_cols = ['Rank', 'Start_date', 'End_date', 'Popularity', 'Members']
anime_df = anime_df.drop(drop_cols, axis=1)
anime_df['Genre'] = anime_df['Genre'].apply(lambda genres: str(genres).split(", "))

anime_df.to_csv('processed_data.csv')

if __name__ == "__main__":
    print('\nThe anime dataframe looks like this:\n')
    print(anime_df.head(10))