"""Services overview."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

theme.setup_page("Services")
theme.inject_css()
theme.render_top_bar()

st.markdown('<p class="aarna-section-title">What we offer</p>', unsafe_allow_html=True)
st.markdown(
    f"<p class='aarna-muted'>Every engagement is scoped to your property type, location, and goals. "
    f"{cfg.SERVICE_AREA}</p>",
    unsafe_allow_html=True,
)

st.info(cfg.SCREENING_HIGHLIGHT)

cols = st.columns(2)
for i, item in enumerate(cfg.SERVICES):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div class="aarna-card" style="margin-bottom:1rem;">
                <h3>{item["title"]}</h3>
                <p>{item["body"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<p class="aarna-section-title" style="margin-top:1.5rem;">Also available where needed</p>', unsafe_allow_html=True)
st.markdown(
    "<p class='aarna-muted'>We layer these in based on your property and agreement—not every item applies to every home.</p>",
    unsafe_allow_html=True,
)
for line in cfg.SERVICE_EXTRAS:
    st.markdown(f"- {line}")

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/2_Contact.py", label="Request a conversation", icon="✉️", use_container_width=True)
with c2:
    st.page_link("streamlit_app.py", label="Back to home", icon="🏠", use_container_width=True)

theme.render_footer()
