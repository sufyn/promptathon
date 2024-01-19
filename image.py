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
    if image:
        print(image)
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
tab1, tab2, tab3 = st.tabs(["Round 1", "Round 2", "Round 3"])
with tab1:
    # Input URL
    st.divider()
    st.write('ROUND 1')
    prompt1 = st.text_input("Enter Your Prompt:", value="",key="r1")
    
    if prompt1:
        with st.status("Processing...", state="running", expanded=True) as status:
            st.write("Generating Image ...")
            img1 = image(prompt1)
            # Download image
            st.divider()
            st.image(img1,width=800,caption=prompt1)
            st.write("Checking Your Accuracy...")
            accuracy1 = accuracy(prompt1)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.write(accuracy1)
    
    
    st.divider()
    st.header("Image to be generated", anchor=False)
    st.image('astro.jpg',width=600)

with tab2:

    st.write('ROUND 2')
    prompt2 = st.text_input("Enter Your Prompt:", value="",key="r2")
    
    if prompt2:
        with st.status("Processing...", state="running", expanded=True) as status:
            st.write("Generating Image ...")
            img2 = image(prompt2)
            # Download image
            st.divider()
            st.image(img2,width=800,caption=prompt2)
            st.write("Checking Your Accuracy...")
            accuracy2 = accuracy(prompt2)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.write(accuracy2)
    
    
    st.divider()
    st.header("Image to be generated", anchor=False)
    st.image('astro.jpg',width=600)

with tab3:

    st.write('ROUND 3')
    prompt3 = st.text_input("Enter Your Prompt:", value="",key="r3")
    
    if prompt3:
        with st.status("Processing...", state="running", expanded=True) as status:
            st.write("Generating Image ...")
            img3 = image(prompt3)
            # Download image
            st.divider()
            st.image(img3,width=800,caption=prompt3)
            st.write("Checking Your Accuracy...")
            accuracy3 = accuracy(prompt3)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.write(accuracy3)
    
    
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
