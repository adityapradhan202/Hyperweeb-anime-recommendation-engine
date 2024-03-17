import streamlit as st
import time
import display_genres as dg
import recommendation as rec
import random


st.header('Hyperweeb - anime recommendations')


st.image(image='https://64.media.tumblr.com/3447324ec71489854d2bf3d7319300d8/e327e281af8a5923-1b/s640x960/1692de9d032004c1cf179b515687e4a45e7fc023.gif')
welcome_text = """Welcome to our anime recommendation web app! Select the genres on the sidebar given on the left to get anime recommendations :smile:"""
middle_text = """First select the genres on the sidebar given on the left, then click on the button given below to get your anime suggestions :smile:"""
ending_text = """Thank for using our web app! Here are your anime recommendations :smile:"""


st.write(welcome_text)
st.sidebar.write('##### :orange[Choose the genres...]')
anime_list = dg.glist.copy()



# categories
cat1 = st.sidebar.selectbox(label="Genre-1", options = anime_list)
cat2 = st.sidebar.selectbox(label='Genre-2', options = anime_list)
cat3 = st.sidebar.selectbox(label='Genre-3', options = anime_list)
cat4 = st.sidebar.selectbox(label='Genre-4', options = anime_list)
cat5 = st.sidebar.selectbox(label="Genre-5", options = anime_list)

# developer's info - buttons on the sidebar
st.sidebar.write('##### :orange[Developers info...]')
github = st.sidebar.link_button(label="Developer's GitHub" ,url='https://github.com/adityapradhan202')
linkedin = st.sidebar.link_button(label="Developer's linkedIn", url='https://www.linkedin.com/in/adipradhan202/')
# some additional info



st.sidebar.write("##### :orange[A little gift for you...]")
st.sidebar.markdown("""We all know that the wifi of our college has so many restrictions. So, you can try [Yugen Anime TV](https://yugenanime.tv/) to watch your favorite animes :smile:""")
# gif - gojo and students dancing
st.sidebar.image(image='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGNvdXZxNnJtZ21haHZ0MzB4MHZrZnpyMHV1aGM2cWMwMnU0Y3Z2biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/Al9XitEIwGgLU9yMfS/giphy.gif')



list_cat = [cat1, cat2, cat3, cat4, cat5]
user_recom_list = rec.recommendations_app_version(category_list = list_cat)



st.write(middle_text)
b = st.button(label="Generate", type='primary')


if b == True:
    try:
        r1 = user_recom_list[random.randint(0, len(user_recom_list))]
        r2 = user_recom_list[random.randint(0, len(user_recom_list))]
        r3 = user_recom_list[random.randint(0, len(user_recom_list))]
        r4 = user_recom_list[random.randint(0, len(user_recom_list))]
        r5 = user_recom_list[random.randint(0, len(user_recom_list))]
        r6 = user_recom_list[random.randint(0, len(user_recom_list))]
        collection = [r1, r2, r3, r4, r5, r6]

    except IndexError as e:
        st.caption("""Some exception occured! Make sure to fill at least one genre given on the left sidebar. Web app will reboot in a while... Please wait for a few seconds :sweat_smile:""")
        time.sleep(8)
        st.markdown('Web app has been :green[rebooted!]')
        time.sleep(2)
        st.rerun()
        
    st.markdown('#### Recommendations...')
    for i, c in enumerate(collection):
        st.write(f'{i+1}) {c}')
        time.sleep(0.5)
    st.write("\n")
    st.write(ending_text)
    st.write("\n")
    st.write('##### Click on the button below if you want to search again...')

    rerun_button = st.button(label='Clear recommendations', type='primary')
    st.caption("""Credits - This data-science app is created by Aditya Pradhan, a student of VIT BHOPAL UNIVERSITY.
               For more info click on 'Developer's linkedin' and 'Developer's github' on the side bar. We hope you liked our product!""")
    
    if rerun_button == True:
        st.rerun()

