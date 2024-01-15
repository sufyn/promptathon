import streamlit as st


def image(prompt):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/dataautogpt3/OpenDalleV1.1"
    key = st.secrets['auth_token'] 
    headers = {"Authorization": key }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content
    image_bytes = query({
        "inputs": prompt,
    })
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))
    return image


def accuracy(prompt):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    key = st.secrets['auth_token'] 
    headers = {"Authorization": key}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
            "source_sentence": "Astronaut riding a horse",
            "sentences": [
                prompt
            ]
        },
    })
    return output




# Set page title
st.set_page_config(page_title="IEEE CS PROMPATHON", page_icon="📜", layout="wide")

# Set title
st.title("IEEE CS PROMPATHON", anchor=False)
st.header("Compare Your Prompts with AI (OpenDalleV1.1 and all-MiniLM-L6-v2)", anchor=False)
st.write('by sufyaan')

# Input URL
st.divider()
prompt = st.text_input("Enter Your Prompt:", value="")

if prompt:
    with st.status("Processing...", state="running", expanded=True) as status:
        st.write("Generating Image ...")
        img = image(prompt)
        # Download image
        st.divider()
        st.image(img,width=800,caption=prompt)
        st.write("Checking Your Accuracy...")
        accuracy = accuracy(prompt)
        status.update(label="Finished", state="complete")
    # Show Summary
    st.subheader("Accuracy:", anchor=False)
    st.write(accuracy)


st.divider()
st.header("Image to be generated", anchor=False)
st.image('astro.jpg',width=600)

st.divider()
st.header("Demo with Prompts", anchor=False)
st.image('cat.png',
         width=500,
         caption='Prompt: black fluffy gorgeous dangerous cat animal creature, large orange eyes, big fluffy ears, piercing gaze, full moon, dark ambiance, best quality, extremely detailed')

st.divider()
st.image('korean.png',
         width=500,
         caption='Prompt: cinematic film still of Kodak Motion Picture Film: (Sharp Detailed Image) An Oscar winning movie for Best Cinematography a woman in a kimono standing on a subway train in Japan Kodak Motion Picture Film Style, shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy')
