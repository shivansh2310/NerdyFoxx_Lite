import streamlit as st

st.set_page_config(page_title="NerdyFoxx-Lite", page_icon='👨‍🎓')

st.write("#")

st.error("##### A collection of 100+ handpicked documentary from Youtube on variety of Topics ")

st.info("###### I had a terrible vision: I saw an encyclopedia walk up to a polymath and open him up. —Karl Kraus ")

st.markdown("### 👨‍🔧 NerdyFoxx-Lite by [NerdyFoxx : Clan Of Misfits](https://nerdyfoxx-wiki.simple.ink/)")

st.image("https://miro.medium.com/max/1400/1*gvPeHGfl9UTy6lx0YtBnxg.jpeg")

st.info("Original Project Repository on [Github](https://github.com/shivansh2310/NerdyFoxx_Lite)")

st.markdown("---")

with st.expander("Info About The Creator"):
    st.markdown("""
    #
    - Hi my name is Shivansh Kumar and I am from India.
    - I am a Computer Science Engineer and a Financial Engineer in making.
    - I love to watch Documentaries and I want to share this passion with others.  
    - You can reach me at my [Twitter](https://twitter.com/Mr_7i74N)    
    #""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
### 📄 Categories

##### <a href="Science_&_Technology" target='_self'>Science_&_Technology</a>
##### <a href="Finance" target='_self'>Finance</a>
##### <a href="Biographies" target='_self'>Biographies</a>
##### <a href="Sports" target='_self'>Sports</a>
##### <a href="Business" target='_self'>Business</a>
##### <a href="NerdyFoxx-Selective" target='_self'>NerdyFoxx-Selective</a>

---
### 📓 Disclaimer 

This web app provides access to a curated collection of documentaries available on YouTube. While we strive to ensure the quality and relevance of the content featured on our platform, please note the following:

**Third-Party Content**: The documentaries embedded on this web app are hosted on YouTube and are the intellectual property of their respective creators, producers, and copyright holders.

**No Endorsement**: The inclusion of documentaries on our platform does not imply endorsement or affiliation with the creators, producers, or subjects featured in the content. We do not endorse the views, opinions, or content presented in these documentaries.

**Copyright Compliance**: We make every effort to ensure that the documentaries featured on our platform comply with copyright laws and regulations. If you believe that your copyright or intellectual property rights have been infringed upon, please contact us immediately using the contact information provided below.

**Removal Requests**: If you are the owner of a documentary featured on our platform and wish to request its removal, please contact us with the following information:


-- Your full name and contact information.
            
-- Documentary title and URL.
            
-- Reason for removal request, including any relevant copyright or ownership details. 
            
**No Financial Transactions**: Our web app does not charge any fees or subscriptions for access to the embedded documentaries. We are committed to providing free and open access to educational and informative content for our users.

**Limited Liability**: While we strive to maintain the accuracy, relevance, and availability of the content featured on our platform, we assume no responsibility for the content, availability, or functionality of third-party websites or services, including YouTube.

Contact Information:

For removal requests, copyright inquiries, or general feedback, please contact us at [Shivansh.business23@gmail.com].

---

### 👨‍🏫 Contributors

- [Shivansh Kumar](https://twitter.com/Mr_7i74N)
---

### ❔ How can you contribute to this project?

**Spread the Word**: Help us reach more people by sharing our web app with your friends, family, and social networks. Spread the word about the documentaries and educational content available on our platform.

**Suggest Documentaries**: Have a favorite documentary that you think should be featured on our platform? Share your suggestions with us! We welcome recommendations for documentaries that inspire, educate, and entertain.

**Provide Feedback**: We value your feedback! Let us know what you think about our web app, including its design, functionality, and content selection. Your input helps us improve the user experience and tailor our platform to better meet your needs.

**Report Issues**: Encountered a technical issue or bug while using our web app? Please report it to us! We appreciate your help in identifying and resolving any issues that may arise.

**Contribute Resources**: Are you a documentary filmmaker, educator, or content creator? We welcome contributions of high-quality documentaries and educational resources to expand our content library and enrich the learning experience for our users.

**Volunteer Expertise**: Are you skilled in web development, design, marketing, or content curation? Consider volunteering your expertise to help us enhance our web app and reach a wider audience. We value collaboration and welcome contributions from passionate individuals like you!

**Support Our Mission**: If you believe in our mission to provide free and open access to educational and informative content, consider supporting our project through donations, sponsorships, or partnerships. Your support helps us sustain and grow our platform for the benefit of our community.

---

### 💌 Supporters and partners

---
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=shivansh2310&repo=NerdyFoxx_Lite&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
            
##### 🖼️ Project made by [Shivansh Kumar](https://github.com/shivansh2310/) 

""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True) 