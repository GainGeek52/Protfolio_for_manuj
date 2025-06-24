import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

# Page config
st.set_page_config(page_title="Manuj Dinesh Chaudhari - Portfolio", page_icon="🧪", layout="wide")

# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Assets
lottie_coding = load_lottieurl("https://lottie.host/7a521f83-d37b-4d5d-a0d3-dd7b38720c14/YYybsWAJRN.json")

# Navigation
selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Skills", "Contact"],
    icons=["house", "code-slash", "gear", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#262730"},
        "icon": {"color": "#4CAF50", "font-size": "25px"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#1F1F1F",
        },
        "nav-link-selected": {"background-color": "#1F1F1F"},
    },
)

if selected == "Home":
    # Header Section
    with st.container():
        left_column, right_column = st.columns((2,1))
        with left_column:
            st.title("Breaking Bad into Code 🧪")
            st.subheader("Hi, I'm Manuj Dinesh Chaudhari")
            st.write(
                """
                I am not in danger, Skyler. I AM the danger!
                
                - 🚀 Full Stack Developer
                - 💻 React & Python Enthusiast
                - 🔬 Experimenting with New Technologies
                """
            )
            st.write("[GitHub](https://github.com/webcrafter011)")
            st.write("[LinkedIn](https://www.linkedin.com/in/manuj-chaudhari-54b7bb242)")
        
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

elif selected == "Projects":
    st.header("Projects")
    
    # Project 1
    with st.container():
        st.write("---")
        st.subheader("iPhone Site Clone")
        st.write(
            """
            A pixel-perfect recreation of Apple's iPhone website using modern web technologies.
            - React.js for dynamic UI components
            - Tailwind CSS for styling
            - Responsive design principles
            """
        )
        st.write("[View Project](https://github.com/your-username/iphone-clone)")

    # Project 2
    with st.container():
        st.write("---")
        st.subheader("Mobile Shop")
        st.write(
            """
            E-commerce platform for mobile phones with advanced features.
            - Full shopping cart functionality
            - User authentication
            - Payment integration
            """
        )
        st.write("[View Project](https://github.com/your-username/mobile-shop)")

elif selected == "Skills":
    st.header("Skills & Technologies")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Frontend")
        st.write("""
        - React.js
        - TypeScript
        - Tailwind CSS
        - HTML5/CSS3
        - JavaScript
        """)
        
    with col2:
        st.subheader("Backend")
        st.write("""
        - Python
        - Node.js
        - Express
        - MongoDB
        - SQL
        """)
        
    with col3:
        st.subheader("Tools & Others")
        st.write("""
        - Git
        - Docker
        - AWS
        - Vercel
        - Streamlit
        """)

elif selected == "Contact":
    st.header("Get In Touch")
    
    # Contact form
    contact_form = """
    <form action="https://formsubmit.co/manujchaudhari123@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)

# Add custom CSS
st.markdown("""
<style>
/* Form styling */
form {
    background-color: #262730;
    padding: 20px;
    border-radius: 10px;
}
input[type=text], input[type=email], textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #4CAF50;
    border-radius: 4px;
    box-sizing: border-box;
    margin-top: 6px;
    margin-bottom: 16px;
    background-color: #1F1F1F;
    color: white;
}
button[type=submit] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
button[type=submit]:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True) 