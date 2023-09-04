import streamlit 
streamlit.title("My Mom's New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), default=['Avocado', 'Strawberries'], key=None, help=None, on_change=None, args=None, kwargs=None, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")
# fruits_to_show = my_fruit_list.loc[fruits_selected]
# streamlit.dataframe(fruits_to_show)
fruits_list = list(my_fruit_list)
streamlit.write('Fruit list:', fruits_list)
options = streamlit.multiselect(
    'Pick some fruits:',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

streamlit.write('You selected:', options)
