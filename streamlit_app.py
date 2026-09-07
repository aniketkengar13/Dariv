import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="DERIVA — Calculus, Made Visible",
    page_icon="∂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome so the site renders edge-to-edge
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).with_name("deriva_app.html").read_text(encoding="utf-8")

components.html(html, height=5200, scrolling=True)
