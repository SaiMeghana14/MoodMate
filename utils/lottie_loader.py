import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    """
    Load a Lottie animation from a local JSON file.
    """
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Lottie file not found: {filepath}")
        return None

def load_lottieurl(url: str):
    """
    Load a Lottie animation from a URL.
    """
    try:
        r = requests.get(url)
        if r.status_code != 200:
            st.error(f"Failed to load Lottie from URL: {url}")
            return None
        return r.json()
    except Exception as e:
        st.error(f"Error loading Lottie from URL: {e}")
        return None

def render_lottie(source: str, height: int = 300, is_url: bool = False):
    """
    Render a Lottie animation in Streamlit.
    
    :param source: File path or URL of the Lottie animation
    :param height: Height of the animation
    :param is_url: If True, loads from URL; otherwise, from local file
    """
    animation = load_lottieurl(source) if is_url else load_lottiefile(source)
    if animation:
        st_lottie(animation, height=height)
