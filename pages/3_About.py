"""About the company."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

theme.setup_page("About")
theme.inject_css()
theme.render_top_bar()

st.markdown('<p class="aarna-section-title">About Aarna</p>', unsafe_allow_html=True)

st.markdown(
    f"""
    <p class="aarna-muted">
        <strong>{cfg.COMPANY_NAME}</strong> provides professional property management with an emphasis on
        clear communication, dependable operations, and respect for both owners and residents.
        We believe well-run properties retain value, reduce friction, and support stronger neighborhoods.
    </p>
    <p class="aarna-muted">
        Replace this paragraph with your founding story, markets served, and any differentiators
        (e.g. years in business, portfolio focus, technology tools). Keeping this page current builds trust
        with prospects who compare firms online.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="aarna-section-title" style="margin-top:1.5rem;">Why work with us</p>', unsafe_allow_html=True)

for title, body in cfg.WHY_US:
    st.markdown(
        f"""
        <div class="aarna-card" style="margin-bottom:0.75rem;">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"<p class='aarna-muted' style='margin-top:1rem;'><em>{cfg.CREDENTIALS_LINE}</em></p>",
    unsafe_allow_html=True,
)

st.divider()
st.page_link("pages/2_Contact.py", label="Start a conversation", icon="✉️")

theme.render_footer()
