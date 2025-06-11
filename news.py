import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
MONGO_URL = "mongodb+srv://tintin:tintin@cluster0.qot4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your MongoDB URL
client = MongoClient(MONGO_URL)
db = client.news_database
collection = db.news_articles

st.set_page_config(page_title="News Entry Dashboard", layout="centered")
st.title("📰 Add News Article")

with st.form("news_form"):
    image = st.text_input("Image URL")
    headline = st.text_input("Headline")
    description = st.text_area("Description")
    ad_image = st.text_input("Ad Image URL")
    link = st.text_input("News Link (URL)")

    submitted = st.form_submit_button("Submit Article")

    if submitted:
        if all([image, headline, description, ad_image, link]):
            news_doc = {
                "image": image,
                "headline": headline,
                "description": description,
                "adImage": ad_image,
                "link": link
            }
            result = collection.insert_one(news_doc)
            st.success(f"News article submitted successfully! ID: {result.inserted_id}")
        else:
            st.error("Please fill in all fields before submitting.")

# Optional: Show existing entries
if st.checkbox("Show Existing Articles"):
    st.subheader("Stored News Articles")
    articles = collection.find().sort("_id", -1)
    for article in articles:
        st.markdown(f"**Headline:** {article['headline']}")
        st.image(article['image'], width=300)
        st.write(article['description'])
        st.markdown(f"[Read More]({article['link']})")
        st.image(article['adImage'], width=300)
        st.markdown("---")
