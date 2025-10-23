# app.py - BakeStory Streamlit App

import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="BakeStory 🍰", layout="wide", page_icon="🍰")

# --- CUSTOM CSS FOR PASTEL THEME ---
st.markdown("""
<style>
body {
    background: #FFF0F5;
    color: #DB2777;
    font-family: 'Arial', sans-serif;
}
h1, h2, h3 {
    color: #EC4899;
}
.stButton>button {
    background-color: #F9A8D4;
    color: white;
    border-radius: 20px;
    padding: 0.5rem 1rem;
    margin-top: 5px;
}
.stButton>button:hover {
    background-color: #EC4899;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>🍰 BakeStory</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Where every bake tells a story of sweetness, love, and passion.</p>", unsafe_allow_html=True)

# --- TABS ---
tabs = ["Home", "Products", "Orders", "Customization", "Fun Facts", "Contact"]
selected_tab = st.radio("", tabs, index=0, horizontal=True)

# --- DISHES ---
dishes = [
    {"name": "Red Velvet Cake", "img": "https://flowera.in/uploads/tempDir/HEart-shape-Red-Velvet-cake-800X800.webp", "desc": "A rich, velvety delight with cream cheese frosting and a romantic touch."},
    {"name": "Cupcakes", "img": "https://i.pinimg.com/1200x/a3/62/1e/a3621e30539931908dfbe5242a251a8e.jpg", "desc": "Soft and sweet bite-sized cakes topped with luscious frosting swirls."},
    {"name": "Brownie", "img": "https://www.urbanbakes.com/wp-content/uploads/2022/08/Walnut-Brownies-URBAN-BAKES-3.1-768x1152.jpg", "desc": "Fudgy, gooey chocolate brownies loaded with crunchy walnuts."},
    {"name": "Cookies", "img": "https://cdn.loveandlemons.com/wp-content/uploads/2020/12/cookie-recipes.jpg", "desc": "Golden, crispy cookies baked to perfection for every sweet craving."},
    {"name": "Thoothukudi Macaroons", "img": "https://www.greatestbakery.in/wp-content/uploads/2024/10/thoothukudi-cashew-nut-Macaroon.jpg", "desc": "South India's signature airy macaroons made with cashews and love."},
    {"name": "Croissant", "img": "https://i.pinimg.com/736x/38/bb/f7/38bbf79ff5cd6e5ad137407bf8a66873.jpg", "desc": "Flaky, buttery French pastry perfect with tea or coffee."},
]

fun_facts = [
    "The world’s largest cupcake weighed over 1,200 pounds!",
    "Baking was once considered an art form in ancient Rome.",
    "The word 'cake' comes from the old Norse word 'kaka'.",
    "Cupcakes were originally called 'number cakes' due to their easy measurements!",
]

# --- HOME TAB ---
if selected_tab == "Home":
    st.subheader("Our Signature Dishes 🍰")
    cols = st.columns(3)
    for i, dish in enumerate(dishes):
        with cols[i % 3]:
            st.image(dish["img"], use_column_width=True)
            st.markdown(f"**{dish['name']}**")
            st.caption(dish["desc"])

# --- PRODUCTS TAB ---
elif selected_tab == "Products":
    st.subheader("Our Products")
    st.write("Discover our freshly baked range of cakes, cookies, macaroons, and pastries crafted with love.")
    cols = st.columns(3)
    for i, dish in enumerate(dishes):
        with cols[i % 3]:
            st.image(dish["img"], use_column_width=True)
            st.markdown(f"**{dish['name']}**")

# --- ORDERS TAB ---
elif selected_tab == "Orders":
    st.subheader("Place Your Order")
    st.write("Your favorite bakes are just a click away!")
    st.button("Order Now")

# --- CUSTOMIZATION TAB ---
elif selected_tab == "Customization":
    st.subheader("Customize Your Bake 🎨")
    base = st.selectbox("Select Base", ["Chocolate", "Vanilla", "Red Velvet", "Butter Scotch"])
    frosting = st.selectbox("Frosting Type", ["Whipped Cream", "Chocolate Ganache", "Buttercream"])
    toppings = st.text_input("Toppings (e.g., nuts, sprinkles, fruits)")
    if st.button("Submit Custom Order"):
        st.success(f"Custom order received: {base} with {frosting}, toppings: {toppings}")

# --- FUN FACTS TAB ---
elif selected_tab == "Fun Facts":
    st.subheader("Fun Facts About Baking 🎉")
    for fact in fun_facts:
        st.info(fact)

# --- CONTACT TAB ---
elif selected_tab == "Contact":
    st.subheader("Contact Us ☎️")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Message sent! We'll reach out to you soon.")
