import pandas as pd
import numpy as np

processed_data = pd.read_csv('processed_data.csv')

# Recommendation function - for main.py
def recommendations(user_genres):
    recom_list = []
    user_genres_list = user_genres.split(", ")
    for i in range(len(user_genres_list)):
        user_genres_list[i] = user_genres_list[i].title()

    for index, x in enumerate(processed_data['Genre']):
        for y in user_genres_list:
            if y in x:
                recom_list.append(str(processed_data['Title'][index]))

    return np.array(recom_list)

# Recommendation function - for streamlit app
def recommendations_app_version(category_list):
    gen_rec = [] # genreated recommendations
    for index, df_gen_list in enumerate(processed_data['Genre']):
        for cat in category_list:
            if cat in df_gen_list:
                gen_rec.append(str(processed_data['Title'][index]))
    
    return np.array(gen_rec)




# Testing
if __name__ == "__main__":
    a = recommendations("Romance")
    print(a)