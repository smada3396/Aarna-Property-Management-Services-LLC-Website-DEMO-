"""Contact form and direct channels."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import theme

try:
    import requests
except ImportError:
    requests = None  # type: ignore

theme.setup_page("Contact")
theme.inject_css()
theme.render_top_bar()

st.markdown('<p class="aarna-section-title">Contact</p>', unsafe_allow_html=True)
st.markdown(
    "<p class='aarna-muted'>Tell us a little about your property or question. "
    "We will follow up using the contact information you provide.</p>",
    unsafe_allow_html=True,
)

def _forms_endpoint() -> str:
    try:
        return str(st.secrets["FORMSPREE_ENDPOINT"]).strip()
    except Exception:
        return ""


with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(
            f"""
            <div class="aarna-card">
                <h3 style="margin-top:0;">Direct</h3>
                <p style="margin:0 0 0.5rem 0;"><strong>Email</strong><br/>
                <a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></p>
                <p style="margin:0 0 0.5rem 0;"><strong>Phone</strong><br/>
                <a href="tel:{cfg.PHONE_TEL}">{cfg.PHONE_DISPLAY}</a></p>
                <p style="margin:0;"><strong>Location</strong><br/>{cfg.ADDRESS_LINE1}
                {("<br/>" + cfg.ADDRESS_LINE2) if cfg.ADDRESS_LINE2 else ""}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        endpoint = _forms_endpoint()
        if not endpoint:
            st.info(
                "Optional: add **FORMSPREE_ENDPOINT** in Streamlit Cloud secrets to deliver this form to your inbox. "
                "Until then, submissions are acknowledged on screen only — use email or phone for real inquiries."
            )

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full name", placeholder="Jane Owner")
            email = st.text_input("Email", placeholder="you@example.com")
            phone = st.text_input("Phone (optional)", placeholder=cfg.PHONE_DISPLAY)
            topic = st.selectbox(
                "Topic",
                [
                    "Owner — full management",
                    "Owner — leasing only / one-time",
                    "Resident / applicant question",
                    "Vendor / partnership",
                    "Other",
                ],
            )
            message = st.text_area(
                "How can we help?",
                placeholder="Property location, unit count, timeline, or other details.",
                height=160,
            )
            submitted = st.form_submit_button("Send message", type="primary")

        if submitted:
            if not name.strip() or not email.strip() or not message.strip():
                st.error("Please fill in your name, email, and a short message.")
            elif endpoint and requests:
                try:
                    resp = requests.post(
                        endpoint,
                        data={
                            "name": name.strip(),
                            "email": email.strip(),
                            "phone": phone.strip(),
                            "topic": topic,
                            "message": message.strip(),
                            "_subject": f"Aarna site: {topic}",
                        },
                        timeout=20,
                    )
                    if resp.ok:
                        st.success("Thank you — your message was sent. We will get back to you shortly.")
                    else:
                        st.warning(
                            "The form service returned an error. Please email us directly at the address on the left."
                        )
                except Exception:
                    st.warning(
                        "We could not reach the form service. Please email us directly at the address on the left."
                    )
            else:
                st.success(
                    "Thanks — your message is noted here for demo purposes. "
                    f"For a real inquiry, email **{cfg.EMAIL}** or call **{cfg.PHONE_DISPLAY}**."
                )

st.divider()
st.page_link("streamlit_app.py", label="Back to home", icon="🏠")

theme.render_footer()
