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
    <p class="aarna-muted">{cfg.ABOUT_LEAD}</p>
    <p class="aarna-muted">{cfg.ABOUT_BODY}</p>
    <p class="aarna-muted">{cfg.SERVICE_AREA}</p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="aarna-section-title" style="margin-top:1.5rem;">Why owners choose us</p>', unsafe_allow_html=True)

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
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/4_Contact_Us.py", label="Start a conversation", icon="✉️", use_container_width=True)
with c2:
    st.page_link("pages/1_Services.py", label="View services", icon="📋", use_container_width=True)

theme.render_footer()
