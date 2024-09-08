import streamlit as st
from streamlit_monaco import st_monaco
from app import generate_code_with_images

# Set up the page configuration
st.set_page_config(page_title="AI Website Generator", layout='wide', initial_sidebar_state="collapsed")

# Custom CSS for improved UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    .main-title {
        font-weight: 700;
        font-size: 3rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #6e48aa, #9d50bb);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    .stButton>button {
        width: 100%;
        border-radius: 30px;
        height: 3.5em;
        font-weight: 700;
        font-size: 1.1em;
        background: linear-gradient(135deg, #6e48aa, #9d50bb);
        color: white;
        border: none;
        transition: all 0.3s ease;
        margin-bottom: 2rem;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #9d50bb, #6e48aa);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }
    .editor-container, .preview-container {
        border: 2px solid #9d50bb;
        border-radius: 15px;
        padding: 1.5rem;
        background-color: #2a2a2a;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
        height: 600px;
        overflow: auto;
    }
    .preview-container {
        background-color: #ffffff;
    }
    .stTextInput>div>div>input {
        color: black;
        border: 2px solid #9d50bb;
        border-radius: 30px;
        padding: 0.75rem 1.5rem;
        font-size: 1.1em;
    }
    .stTextInput>label {
        color: #6e48aa;
        font-weight: 700;
        font-size: 1.2em;
    }
    .section-title {
        color: #6e48aa;
        font-weight: 700;
        font-size: 1.8em;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #888;
        font-size: 0.9em;
    }
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        .stButton>button {
            margin-bottom: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown('<h1 class="main-title">AI WEBSITE GENERATOR</h1>', unsafe_allow_html=True)

# Initialize session state for Monaco editor's code
if 'code' not in st.session_state:
    st.session_state.code = "<h1>Hi, click the generate button</h1>"

# Layout with input field and buttons
user_input = st.text_input("Describe your website code request...", "")

col1, col2 = st.columns(2)
with col1:
    generate_button = st.button("Generate Code", key="generate", use_container_width=True)
with col2:
    run_button = st.button("Run Code", key="run", use_container_width=True)

if generate_button:
    gencode = generate_code_with_images(user_input)
    st.session_state.code = gencode

# Layout for code editor and live preview
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3 class="section-title">Code Editor</h3>', unsafe_allow_html=True)
    code = st_monaco(
        language="html",
        value=st.session_state.code,
        height=600,
        theme="vs-dark"
    )

# Save changes from Monaco editor
if run_button:
    st.session_state.code = code  # Save the latest editor content to the session state

with col2:
    st.markdown('<h3 class="section-title">Live Preview</h3>', unsafe_allow_html=True)
    st.components.v1.html(st.session_state.code, height=600, scrolling=True)

# Add a footer
st.markdown("""
    <div class="footer">
        <p>Made By Habib</p>
    </div>
""", unsafe_allow_html=True)