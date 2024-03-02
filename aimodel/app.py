import streamlit as st
from ai import initialize, process
from pathlib import Path
from PIL import Image  # For image handling

# Initialize the model under cache to improve performance
@st.cache_resource(allow_output_mutation=True)
def init_model():
    try:
        model = initialize()
        return model
    except Exception as e:
        st.error(f"Error initializing model: {e}")
        raise e  # Re-raise to prevent app from loading incorrectly

# Load the model
model = init_model()

# Allow user image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Handle image upload and processing
if uploaded_file is not None:
    try:
        # Read the uploaded image using PIL
        image = Image.open(uploaded_file)

        # Process the image and obtain the result using the model
        result = process(model, image)

        # Display the image and result in a visually appealing manner
        st.image(image, width=300)  # Resize image for better presentation
        st.write(f"Result: {result}")

    except Exception as e:
        st.error(f"Error processing image: {e}")

# If no image is uploaded, display a placeholder message
else:
    st.info("No image uploaded yet. Please upload an image to see the result.")
