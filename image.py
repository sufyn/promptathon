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
    print(image_bytes)
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))
    return image


def accuracy1(prompt1):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    key = st.secrets['auth_token'] 
    headers = {"Authorization": key}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
            "source_sentence": "A pair of hands holding a VR headset, the user's eyes wide with wonder as they explore a vibrant virtual world filled with fantastical creatures",
            "sentences": [
                prompt
            ]
        },
    })
    return output
def accuracy2(prompt2):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    key = st.secrets['auth_token'] 
    headers = {"Authorization": key}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
            "source_sentence": "A drone soaring through a dense rainforest, its cameras capturing breathtaking biodiversity while simultaneously monitoring environmental health",
            "sentences": [
                prompt
            ]
        },
    })
    return output
def accuracy3(prompt3):
    import requests

    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
    key = st.secrets['auth_token'] 
    headers = {"Authorization": key}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
            "source_sentence": "A quantum computer bathed in liquid nitrogen, its intricate circuitry glowing with the potential to unlock the secrets of the universe",
            "sentences": [
                prompt
            ]
        },
    })
    return output
def finalaccuracy(prompt1,prompt2,prompt3):
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
                prompt1,
                prompt2,
                prompt3
                
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
tab1, tab2, tab3, tab4 = st.tabs(["Round 1", "Round 2", "Round 3", "Accuracy"])
with tab1:
    # Input URL
    
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
            accuracy1 = accuracy1(prompt1)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.subheader(accuracy1[0])
        
        st.header('Doing Good!!!')
    
    
    st.divider()
    st.header("Image to be generated", anchor=False)
    st.image('vr.jpg',width=600)
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
            accuracy2 = accuracy2(prompt2)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.subheader(accuracy2[0])
    
        st.header('Performing Better!!!')

    st.divider()
    st.header("Image to be generated", anchor=False)
    st.image('drone.jpg',width=600)


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
            accuracy3 = accuracy3(prompt3)
            status.update(label="Finished", state="complete")
        # Show Summary
        st.subheader("Accuracy:", anchor=False)
        st.subheader(accuracy3[0])
        
        st.header('Nice Try!!!')
        st.write(accuracy1[0])
        st.write(accuracy2[0])
        st.write(accuracy3[0])
        faccuracy=(accuracy1[0]+accuracy2[0]+accuracy3[0])/3
        st.subheader('Final Score:')
        st.subheader(faccuracy)
    
    st.divider()
    st.header("Image to be generated", anchor=False)
    st.image("quantum.png",width=600)

with tab4:
    with st.status("Processing...", state="running", expanded=True) as status:
            
            st.subheader("Accuracy:")
            st.write("Checking Your Accuracy...")
            prompt1 = st.text_input("Enter Your Prompt:", value="",key="r11")
            a1 = accuracy1(prompt1)
            st.write(a1[0])
            prompt2 = st.text_input("Enter Your Prompt:", value="",key="r22")
            a2 = accuracy2(prompt2)
            st.write(a2[0])
            prompt3 = st.text_input("Enter Your Prompt:", value="",key="r33")
            a3 = accuracy3(prompt3)
            st.write(a3[0])
        
            status.update(label="Finished", state="complete")
            st.write('Final:')
            st.write(a1[0])
            st.write(a2[0])
            st.write(a3[0])
            faccuracy=(a1[0]+a2[0]+a3[0])/3
            st.subheader('Final Score:')
            st.subheader(faccuracy)

st.divider()
st.header("Demo with Prompts", anchor=False)
st.image('cat.png',
         width=500,
         caption='Prompt: black fluffy gorgeous dangerous cat animal creature, large orange eyes, big fluffy ears, piercing gaze, full moon, dark ambiance, best quality, extremely detailed')

st.divider()
st.image('korean.png',
         width=500,
         caption='Prompt: cinematic film still of Kodak Motion Picture Film: (Sharp Detailed Image) An Oscar winning movie for Best Cinematography a woman in a kimono standing on a subway train in Japan Kodak Motion Picture Film Style, shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy')
