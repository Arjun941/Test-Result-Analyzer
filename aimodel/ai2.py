from pathlib import Path
import google.generativeai as genai
def initialize():
   # Set up the API key
    genai.configure(api_key="AIzaSyCWwy075_Lg2XP1hmdGHI4XYl7MBxw_vQg")

    # Set up the model
    generation_config = {
    "temperature": 0.3,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    return model
def process(model,image):
    # Prepare prompt parts
    prompt_parts = [
        "Analyze the following medical test report image and output the information mentioned below, whichever is available. Translate the report so that a normal user can understand, highlighting key points about their health condition and measures to improve it. Also, show a warning if the test result mentioned is expired, as per data. Compare the given data rate to the user's health condition on an overall scale of 100. Also, rate different metrics on a scale from normal to severe.\n\n",
        {
            "mime_type": "image/jpeg",
            "data": image_path.read_bytes()
        }
    ]

    # Generate content
    response = model.generate_content(prompt_parts)
    return response.text
if __name__ == "__main__":
    model = initialize()
    # Va
    image_path = Path("testrep3.jpg")
   
    result = process(model,image_path)

    print(result) 