"""Information for current and prospective residents."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

theme.setup_page("Residents")
theme.inject_css()
theme.render_top_bar()

st.markdown('<p class="aarna-section-title">Residents & applicants</p>', unsafe_allow_html=True)
st.markdown(
    f"<p class='aarna-muted'>{cfg.RESIDENT_INTRO}</p>",
    unsafe_allow_html=True,
)

for title, body in cfg.RESIDENT_TOPICS:
    st.markdown(
        f"""
        <div class="aarna-card" style="margin-bottom:0.85rem;">
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <p class="aarna-muted" style="margin-top:1rem;">
        We are committed to fair housing and equal opportunity. Housing decisions are made in accordance with
        applicable federal, state, and local law.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()
c1, c2 = st.columns(2)
with c1:
    theme.page_link_with_icon("pages/4_Contact_Us.py", "Contact the office", "contact", use_container_width=True)
with c2:
    theme.page_link_with_icon("Home.py", "Back to home", "home", use_container_width=True)

theme.render_footer()
