
# Import Streamlit
import streamlit as st
from ai import initialize,process
from pathlib import Path


# Create a title for your app
st.title('Test Analyzer')
model = initialize()
    
image_path = Path("testrep3.jpg")
   
result = process(model,image_path)
st.write(result)
st.image(image_path)