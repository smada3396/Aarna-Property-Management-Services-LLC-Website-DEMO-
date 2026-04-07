"""Aarna Property Management Services — public marketing home page."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

theme.setup_page("Home")
theme.inject_css()
theme.render_top_bar()

trust_items = "".join(
    f"<li><strong>{title}</strong> — {desc}</li>" for title, desc in cfg.HOME_TRUST_POINTS
)
st.markdown(
    f"""
    <div class="aarna-hero">
        <div class="aarna-badge">Property management · Maryland</div>
        <h1>{cfg.TAGLINE}</h1>
        <p class="lead">{cfg.HERO_SUBTITLE}</p>
        <p class="sub">{cfg.RESPONSE_POLICY}</p>
        <ul class="aarna-trust-bar">
            {trust_items}
        </ul>
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
            <p>Transparent reporting, leasing support, and maintenance handled with documented care for your asset and your time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="aarna-card">
            <h3>For residents</h3>
            <p>Clear processes, respectful communication, and timely follow-up when something needs attention at home.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="aarna-card">
            <h3>For your portfolio</h3>
            <p>Consistent operations whether you own one door or a growing set of rentals in the region.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<p class="aarna-section-title" style="margin-top:2rem;">How we work with owners</p>', unsafe_allow_html=True)
st.markdown(
    "<p class='aarna-muted'>A straightforward path from first conversation to day-to-day management.</p>",
    unsafe_allow_html=True,
)

steps_html = "".join(
    f'<div class="aarna-step"><strong>{title}</strong><span>{desc}</span></div>'
    for title, desc in cfg.PROCESS_STEPS
)
st.markdown(f'<div class="aarna-steps">{steps_html}</div>', unsafe_allow_html=True)

st.markdown('<p class="aarna-section-title" style="margin-top:2.25rem;">Explore the site</p>', unsafe_allow_html=True)
st.markdown(
    "<p class='aarna-muted'>Review services, learn more about our approach, or reach out when you are ready.</p>",
    unsafe_allow_html=True,
)

b1, b2, b3, b4 = st.columns(4)
with b1:
    st.page_link("pages/1_Services.py", label="Services", icon="📋", use_container_width=True)
with b2:
    st.page_link("pages/2_About_Us.py", label="About", icon="ℹ️", use_container_width=True)
with b3:
    st.page_link("pages/3_For_Residents.py", label="Residents", icon="🏡", use_container_width=True)
with b4:
    st.page_link("pages/4_Contact_Us.py", label="Contact", icon="✉️", use_container_width=True)

theme.render_footer()
