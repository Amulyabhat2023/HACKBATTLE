import streamlit as st

st.set_page_config(page_title="VITVFreshie!", page_icon=":tada:", layout= "wide")

st.sidebar.title("Navigation")
option= st.sidebar.radio('Pages', options= ['Home', 'Map', 'PYPs', 'Ask your senior', 'Find your mate', 'Hostel essentials'])
with st.container():
    st.subheader("Hello freshers :wave:, Welcome to VIT!")
    st.write("The VITVfreshie web helps freshers feel at home. This web provides the kick start required for the initial start at VIT Vellore.")

with st.container():
    st.write("---")
    st.header("Features")
    st.write("##")
    st.write("No idea how to find your way around VIT?  Get access to the VIT map")
    st.write("Want to know the question paper pattern of CAT and FAT? A collection of PYPs is all set for your use")
    st.write("Lot of queries troubling your mind?  Talk to your seniors and clear your doubts")
    st.write("Get to know your roommates and students from your region ")
    st.write("Be hostel ready with a full list of Hostel Essentials ")

if option== 'Home':
    st.header("Home")
    st.write("We are a team comprised of freshers. Not too long ago, we were entirely new to the campus and had to face a lot of confusion in our minds. We had no idea whom to contact or where to go in order to get better clarity about the university. This led us to join multiple Whatsapp groups, out of which some even turned out to be scams. We were in constant dilemma as we had no idea what to do.")
    st.write("'When we thought and ideated on the basis of this problem, we came up with an idea. An app, more like a social platform, where the freshers can put in their doubts and our beloved seniors can answer them. The queries can range from trivial ones such as “where is PRP?”, to more academic ones such as, “What’s the best way to ace CAT?” to emotional ones such as “How to make friends?”.'")
    st.write("'In order to make our freshers feel comfortable, we are planning to integrate a feature to allow them to post the queries anonymously. Additionally, the app will also consist of features such as “VIT campus map”, “Find your roommate”, “Events list” and much more, to make the freshers feel at home .'")

if option== 'Map':
    st.header("MAP")
    st.write("[The MAP of VIT campus to guide u along the university](https://www.mirlabs.org/socpar16/venue_clip_image002.jpg)")

if option== 'PYPs':
    st.header("Previous Year Papers")
    st.write("[Link for previous year papers](https://drive.google.com/drive/folders/1ft579_REKlGjp6HDkkgIhH55W1ljJKVm?usp=drive_link)")

if option== 'Hostel essentials':
    st.header("Make sure you get all you essentials before reporting to the hostel")
    st.write("[Hostel Essentials](https://thenomadicpanda.files.wordpress.com/2019/08/hostel-packing-list-20-essentials-you-have-to-take-e1565864843733.png)")

if option== 'Ask your senior':
    st.header("Hello freshers, welcome to VIT!")
    with st.container():
        st.title("How can we help you?")
        cont = """<form action="https://formsubmit.co/vitvfreshie@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">  
         <input type="text" name="name" placeholder="NAME" required>
         <input type="text" name="Register Number" placeholder="Register Number" required>
         <input type="text" name=""Query" placeholder="Enter your query" required>
         <button type="submit">Submit</button>
    </form>
    """

    st.markdown(cont, unsafe_allow_html=True)





