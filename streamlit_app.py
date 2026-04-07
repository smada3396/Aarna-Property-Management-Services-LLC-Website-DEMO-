"""Aarna Property Management Services — public marketing home page."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

theme.setup_page("Home")
theme.inject_css()
theme.render_top_bar()

st.markdown(
    f"""
    <div class="aarna-hero">
        <div class="aarna-badge">Property management</div>
        <h1>{cfg.TAGLINE}</h1>
        <p class="lead">{cfg.HERO_SUBTITLE}</p>
        <p class="sub">Explore services, learn how we work, and reach out when you are ready to talk.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class="aarna-card">
            <h3>For property owners</h3>
            <p>Transparent reporting, leasing support, and maintenance handled with care for your asset.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="aarna-card">
            <h3>For residents</h3>
            <p>Respectful communication, fair processes, and timely responses when something needs attention.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="aarna-card">
            <h3>For your portfolio</h3>
            <p>Consistent operations whether you own one door or a growing set of units.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<p class="aarna-section-title" style="margin-top:2rem;">Get started</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="aarna-muted">Use the sidebar to move between sections, or jump straight to contact.</p>',
    unsafe_allow_html=True,
)

b1, b2, b3 = st.columns([1, 1, 2])
with b1:
    st.page_link("pages/1_Services.py", label="View services", icon="📋")
with b2:
    st.page_link("pages/2_Contact.py", label="Contact us", icon="✉️")
with b3:
    st.page_link("pages/3_About.py", label="About the company", icon="ℹ️")

theme.render_footer()
