# HYPERWEEB ENGINE VERSION 2.0
import streamlit as st
import time
import display_genres as dg
import recommendation as rec
import random
from app_banner_gifs import banners_list as banner


from songs import song_link as slink


if 'cat1' not in st.session_state:
    st.session_state.cat1 = 'None'
if 'cat2' not in st.session_state:
    st.session_state.cat2 = 'None'
if 'cat3' not in st.session_state:
    st.session_state.cat3 = 'None'
if 'cat4' not in st.session_state:
    st.session_state.cat4 = 'None'
if 'cat5' not in st.session_state:
    st.session_state.cat5 = 'None'

slink_index = 0
if 'tab2_rerun' not in st.session_state:
    st.session_state.tab2_rerun = False
else:
    if st.session_state.tab2_rerun == False:
        slink_index = random.randint(1, len(slink))

# The list that we will use in the streamlit selectbox 
anime_list = dg.glist.copy()

st.header('Hyperweeb - anime recommendations')


welcome_text = """Welcome to our anime recommendation web app! Select the genres on the sidebar given on the left to get anime recommendations :smile:"""
middle_text = """First select the genres on the sidebar given on the left, then click on the button given below to get your anime suggestions :smile:"""
ending_text = """Thank for using our web app! Here are your anime recommendations :smile:"""


def set_categories_none():
    st.session_state.cat1 = 'None'
    st.session_state.cat2 = 'None'
    st.session_state.cat3 = 'None'
    st.session_state.cat4 = 'None'
    st.session_state.cat5 = 'None'


# App sidebar
st.sidebar.write('##### :orange[Choose the genres...]')
# categories
cat1 = st.sidebar.selectbox(label="Genre-1", 
                            options = anime_list, key = 'cat1', 
                            index = anime_list.index(st.session_state.cat1))
cat2 = st.sidebar.selectbox(label='Genre-2', 
                            options = anime_list, key = 'cat2',
                            index = anime_list.index(st.session_state.cat2))
cat3 = st.sidebar.selectbox(label='Genre-3', 
                            options = anime_list, key = 'cat3',
                            index  = anime_list.index(st.session_state.cat3))
cat4 = st.sidebar.selectbox(label='Genre-4', 
                            options = anime_list, key = 'cat4',
                            index = anime_list.index(st.session_state.cat4))
cat5 = st.sidebar.selectbox(label="Genre-5", 
                            options = anime_list, key = 'cat5',
                            index = anime_list.index(st.session_state.cat5))

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


# tabs
tab_names = ['Main page', 'Anime songs and soundtracks']
tab1, tab2 = st.tabs(tabs = tab_names)

collection = []


# Tab-1
with tab1:

    st.write(welcome_text)

    n = len(banner) - 1
    banner_number = random.randint(0, n)
    current_banner = banner[banner_number]
    st.image(image = current_banner, width=550)


    st.write(middle_text)
    b = st.button(label="Generate", type='primary')

    if b == True:
        try:

            m = len(user_recom_list)
            r1 = user_recom_list[random.randint(0, m)]
            r2 = user_recom_list[random.randint(0, m)]
            r3 = user_recom_list[random.randint(0, m)]
            r4 = user_recom_list[random.randint(0, m)]
            r5 = user_recom_list[random.randint(0, m)]
            r6 = user_recom_list[random.randint(0, m)]
            collection = [r1, r2, r3, r4, r5, r6]

        except IndexError as e:
            st.caption("""Some exception occured! Make sure to fill at least one genre given on the left sidebar :sweat_smile:""")
            st.caption('Wait for a few seconds. The app will reboot soon!')


            with st.spinner(text = "Rebooting the app..."):
                time.sleep(4.5)

            st.caption('Web app has been :green[rebooted!]')
            st.rerun()
        
        st.markdown('#### Recommendations...')
        for i, c in enumerate(collection):
            st.write(f'{i+1}) {c}')
            time.sleep(0.5)
        st.write("\n")
        st.write(ending_text)
        st.write("\n")
        st.write('##### Click on the button below if you want to search again...')

        # APP reboot system / Clear recommendations
        rerun_button = st.button(label='Clear recommendations', type='primary', on_click = set_categories_none)
        st.caption("""Credits - This data-science app is created by Aditya Pradhan, a student of VIT BHOPAL UNIVERSITY.
                For more info click on 'Developer's linkedin' and 'Developer's github' on the side bar. We hope you liked our product...""")
    
    
        if rerun_button == True:
            st.rerun()


# Tab-2
with tab2:
    st.write('Click on the button given below to generate sountracks. Everytime you click on the button, it will generate a different a sountrack...')
    btn_sountrack = st.button(label = 'Generate sountrack', type = 'primary')



    st.write()
    if btn_sountrack:
        with st.spinner(text = 'Fetching video data...'):
            time.sleep(1.5)
            with st.spinner(text = 'Fetching sountrack data...'):
                time.sleep(3)
        
        st.write("Here's your sountrack...")
        
        if slink_index == len(slink):
            slink_index -= 1

        st.video(data = (list(slink.values()))[slink_index])
