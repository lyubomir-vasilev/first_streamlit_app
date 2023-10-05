import streamlit 

streamlit.title('My parents new healthy diner') 
streamlit.header('Breakfast Favoruites') 
streamlit.text('🥣 Omega 3 & Blueberry Oats') 
streamlit.text('🥗 Kale, Spinach, and Rocket Smoothie') 
streamlit.text('🐔 Hard-boiled Free range eggs') 
streamlit.text('🥑🍞 Avocado toast') 



streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
  
import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt') 
my_fruit_list = my_fruit_list.set_index('Fruits)
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
