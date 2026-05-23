import streamlit as st
import os
import google.generativeai as genai

# 1. Setup Page Configurations with your Custom Name
st.set_page_config(page_title="Aryan AI Tutor", page_icon="🎓", layout="centered")
st.title("🎓 Aryan AI Tutor")
st.subheader("Your 24/7 Socratic Companion for Classes 8th to 12th")

# 2. Retrieve the Free API Key securely from environment variables or sidebar
API_KEY = os.environ.get("GEMINI_API_KEY") or st.sidebar.text_input("Enter Gemini API Key:", type="password")

if not API_KEY:
    st.info("Please add your Gemini API Key to get started.", icon="🔑")
    st.stop()

# Configure the Google GenAI Engine
genai.configure(api_key=API_KEY)

# 3. Define the Advanced Teacher Personality (Upgraded Thinking Engine)
SYSTEM_INSTRUCTION = """
You are 'Aryan AI', a highly intellectual, patient, and world-class school educator specializing in the NCERT/CBSE curriculum for Classes 8 to 12. 

To ensure elite educational quality, follow these strict cognitive rules for every response:
1. Deep Diagnostic Step: Before typing any hint or explanation, secretly analyze the core concept behind the student's question. Identify common student misconceptions for this topic.
2. Conceptual Grounding: Never provide raw facts in isolation. Always ground your explanation using a vivid real-world analogy or a practical everyday example first.
3. Strict Socratic Scaffolding: For mathematical numericals, chemical equations, or physics derivations, absolutely DO NOT show the final numerical result. Instead:
   - Identify the variables given in the question or diagram.
   - Introduce the fundamental governing formula.
   - Break down the very first logical step, then ask the student an encouraging question to guide them toward solving the next part.
4. Micro-Formatting: Avoid large paragraphs. Use clean bold headings, crisp bullet points, and proper mathematical formatting to make the answer scannable and completely clear.
"""

# Initialize the Gemini model with advanced precision configuration settings
@st.cache_resource
def load_model():
    return genai.GenerativeModel(
        model_name="gemini-2.5-flash-lite",
        system_instruction=SYSTEM_INSTRUCTION,
        # This upgrades the precision, consistency, and logic of Aryan AI
        generation_config={
            "temperature": 0.3,  # Forces accurate, factual, and logical answers over creative guesses
            "top_p": 0.95,
        }
    )

model = load_model()

# 4. Manage Chat History in User Session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display existing chat messages
for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# 5. Handle User Inputs & Multimodal File Uploads
uploaded_file = st.file_uploader("📸 Upload a textbook problem or diagram", type=["png", "jpg", "jpeg"])

if user_question := st.chat_input("Ask Aryan AI any question from your school syllabus..."):
    
    # Display user question immediately
    with st.chat_message("user"):
        st.markdown(user_question)
        if uploaded_file is not None:
            st.image(uploaded_file, width=250)
        
    # Generate response from AI
    with st.chat_message("assistant"):
        with st.spinner("Aryan AI is analyzing..."):
            try:
                # If there is an uploaded image, process it properly using PIL
                if uploaded_file is not None:
                    from PIL import Image
                    # Convert the uploaded file bytes into a real image object
                    img = Image.open(uploaded_file)
                    
                    # Pass the text and the converted image object together
                    response = st.session_state.chat_session.send_message([user_question, img])
                else:
                    # Otherwise, just process the text question normally
                    response = st.session_state.chat_session.send_message(user_question)
                    
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error communicating with Aryan AI: {e}")