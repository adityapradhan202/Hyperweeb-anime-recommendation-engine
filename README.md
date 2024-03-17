# Hyperweeb - Documentation

## Hyperweeb - Anime Recommendation Engine
Hyperweeb is a data science powered web application that helps anime enthusiasts discover their next favorite show!  This app analyzes user-selected genres and recommends anime based on those preferences.

## How to use this web app?
Simply click on this link to go to the app - https://hyperweeb-engine.streamlit.app/  
**Note** -  In some cases you might face issues while using this web app on your mobile phones, but it in most of the cases it works perfectly fine. It is recommended to use this link on your laptop's or computer's web browser.

## Features
- User-friendly interface for selecting anime genres
- Personalized recommendations based on genre preferences
- Leverages basic datascience techniques to clean and preprocess the real world data to get the dataset on which this app works
- Generates anime recommendation with remarkable accuracy and precision

## Getting started
Now this section of the documentation talks about how to do the coding part and deployment! Read it carefully to understand the process of how this app is created and deployed.  


#### Teck stack used in this project 
1. [Numpy](https://numpy.org/)
2. [Pandas](https://pandas.pydata.org/)
3. [Streamlit](https://streamlit.io/)


#### Dataset used in this project 
The real world anime data used in this app is from [Kaggle](https://www.kaggle.com/), a machine learning and data science community.  
Data set - https://www.kaggle.com/datasets/gianinamariapetrascu/top-250-anime-2023


#### Step by step process
1. First clean the dataset using pandas, use data cleaning and preprocessing techniques.
2. Then create a logic to filter anime based on the genres that the user chooses. The logic is very simple, you can checkout - [recoomdation.py](https://github.com/adityapradhan202/Hyperweeb-anime-recommendation/blob/main/recommendation.py).
3. Then use Streamlit to create the web app. Add buttons, sidebar, captions, texts, images and gif etc. If you don't know how to use Streamlit then you can refer to the [Streamlit API Documentation](https://docs.streamlit.io/)
4. ##### App Deployment
    1. Add all the files to a public repository on your GitHub account.
    2. Go to [Streamlit Cloud Community](https://streamlit.io/cloud) and create an account.
    3. Then select the 'New app' option on the dashboard. Fill all the details, for example, your github repo link, the branch, and link of the file which contains your streamlit app code. Once the app is deployed, anyone with the app link can use the app on the web browser :smile:

## App images
#### Image - 1
![app_img_1](https://github.com/adityapradhan202/Hyperweeb-anime-recommendation/blob/main/hw_img_1.png?raw=true)
#### Image - 2
![app_img_2](https://github.com/adityapradhan202/Hyperweeb-anime-recommendation/blob/main/hw_img_2.png?raw=true)
#### Image - 3
![app_img_3](https://github.com/adityapradhan202/Hyperweeb-anime-recommendation/blob/main/hw_img_3.png?raw=true)

## License
This project is licensed under MIT LICENSE [(see LICENSE.txt for details)](https://github.com/adityapradhan202/Hyperweeb-anime-recommendation/blob/main/LICENSE)

## A note from the developer...
I know that this is a very basic data science app, but what more can you expect from a beginner 😅 But I think it's a good app, and you can use it whenever you need anime recommendation. I have tested this app, and it is remarkably accurate. And to be honest, I made this app for my college friends, so that they can get some good anime recommendations. In future I might integrate some anime related APIs to display the posters of the movies and anime series along with the textual recommendations. Also, I might try to use techniques like collaborative filtering to make this app! 😄

