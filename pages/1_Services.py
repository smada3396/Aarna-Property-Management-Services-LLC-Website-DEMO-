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
    "<p class='aarna-muted'>Every engagement is scoped to your property type and goals. "
    "Below are typical pillars of our management approach.</p>",
    unsafe_allow_html=True,
)

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

st.divider()
st.page_link("pages/2_Contact.py", label="Request a conversation", icon="✉️")

theme.render_footer()
