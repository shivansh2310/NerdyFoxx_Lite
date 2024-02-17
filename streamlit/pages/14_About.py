import streamlit as st

st.set_page_config(page_title="About", page_icon='🖼️')

st.markdown("## 🖼️ About this app")

st.markdown("This Streamlit app is a user-friendly interface designed by [Shivansh Kumar](https://github.com/shivansh2310/) to build a curated list of amazing Documentaries from Youtube")

st.image("https://images.unsplash.com/photo-1484910292437-025e5d13ce87?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2114&q=80")

st.markdown("""
### 🎥 Documentary Collection
       
Explore a curated collection of over 100+ handpicked documentaries covering a wide range of topics and themes. From history and science to finace and sports, our documentary library offers a diverse selection of captivating films to educate, inspire, and entertain.

### 🌐 Features

- **Easy navigation**: Navigate through our extensive documentary collection with ease using intuitive search and browse features. Discover documentaries by category, topic, or keyword, and find your next cinematic adventure effortlessly.
- **Rich Content**: Immerse yourself in thought-provoking narratives, stunning visuals, and insightful storytelling that bring each documentary to life. Experience the beauty of our world and uncover hidden truths through the lens of documentary filmmaking.

### 🚀 Usage

Start exploring our documentary collection today! Simply browse through the different categories, click on a documentary title to watch, and immerse yourself in the fascinating world of documentary filmmaking. Whether you're a history buff, science enthusiast, or nature lover, there's something for everyone to discover.

### ⭕ Disclaimer

This web app is created as a personal project to share a passion for documentary filmmaking and is not affiliated with any specific documentary production companies or organizations. All documentaries featured on this platform belong to their respective creators and copyright holders.

### 👨‍🏫 Acknowledgements

I extend my gratitude to the filmmakers, producers, and creators who have crafted the captivating documentaries featured on this platform. Their dedication to storytelling and commitment to exploring the world around us inspire us all to see beyond the surface and embrace the power of documentary filmmaking.

### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=shivansh2310&repo=NerdyFoxx_Lite&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   

If you liked the project please leave a star. """, unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 