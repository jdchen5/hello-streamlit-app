# hello_world.py

import streamlit as st

# Set page title
st.set_page_config(page_title="Hello World App")

# Display a title
st.title("Hello World Streamlit App")

# Add some text
st.write("Welcome to your first Streamlit application!")

# Add a simple input
name = st.text_input("What's your name?", "Visitor")

# Add a button
if st.button("Say Hello"):
    # Display greeting with the name input
    st.write(f"Hello, {name}! 👋")
    
    # Add some colored text
    st.success("Your Streamlit app is working correctly!")
    
# Add a simple counter
if "counter" not in st.session_state:
    st.session_state.counter = 0
    
if st.button("Click me to count"):
    st.session_state.counter += 1
    
st.write(f"Button clicked {st.session_state.counter} times")

# Display some simple markdown
st.markdown("## This is a markdown header")
st.markdown("- Item 1")
st.markdown("- Item 2")
st.markdown("- Item 3")

# Add a debug checkbox
debug = st.checkbox("Show debug info")
if debug:
    st.write("Debug information:")
    st.write(f"Streamlit version: {st.__version__}")
    st.write("Session state:", st.session_state)