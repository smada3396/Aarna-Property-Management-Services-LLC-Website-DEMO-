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
    "<p class='aarna-muted'>Tell us about your property or question. We follow up using the contact information you provide.</p>",
    unsafe_allow_html=True,
)


def _forms_endpoint() -> str:
    try:
        return str(st.secrets["FORMSPREE_ENDPOINT"]).strip()
    except Exception:
        return ""


if cfg.has_public_phone():
    phone_block = (
        f'<p style="margin:0 0 0.35rem 0;"><strong>Phone</strong></p>'
        f'<p style="margin:0 0 0.15rem 0;">Office: '
        f'<a href="tel:{cfg.PHONE_OFFICE_TEL}">{cfg.PHONE_OFFICE_DISPLAY}</a></p>'
        f'<p style="margin:0 0 0.5rem 0;">Mobile: '
        f'<a href="tel:{cfg.PHONE_MOBILE_TEL}">{cfg.PHONE_MOBILE_DISPLAY}</a></p>'
    )
else:
    phone_block = (
        '<p style="margin:0 0 0.5rem 0;"><strong>Phone</strong><br/>'
        "<span>Leave your number in the form and we will call you back, or email us anytime.</span></p>"
    )

address_block = (
    f'<p style="margin:0 0 0.35rem 0;"><strong>Office</strong></p>'
    f'<p style="margin:0 0 0.75rem 0;">{cfg.ADDRESS_LINE1}<br/>{cfg.ADDRESS_LINE2}</p>'
)

with st.container():
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(
            f"""
            <div class="aarna-card">
                <h3 style="margin-top:0;">Reach us directly</h3>
                <p style="margin:0 0 0.5rem 0;"><strong>Email</strong><br/>
                <a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></p>
                {phone_block}
                {address_block}
                <p style="margin:0 0 0.75rem 0;"><strong>Service area</strong><br/>{cfg.SERVICE_AREA}</p>
                <p style="margin:0;font-size:0.9rem;color:#5a6b7c;"><strong>Hours</strong><br/>{cfg.BUSINESS_HOURS}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="aarna-card" style="margin-top:1rem;">
                <h3 style="margin-top:0;">What to expect</h3>
                <p style="margin:0;font-size:0.95rem;color:#4a5a6e;line-height:1.55;">{cfg.RESPONSE_POLICY}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        endpoint = _forms_endpoint()
        if not endpoint:
            st.info(
                "**Property owners:** for the fastest response, email us or use this form and we will reply from the office. "
                "**Tip for Streamlit Cloud:** add a `FORMSPREE_ENDPOINT` secret so submissions go straight to your inbox—"
                "see the README in this project."
            )

        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full name", placeholder="Your name")
            email = st.text_input("Email", placeholder="you@example.com")
            phone = st.text_input(
                "Phone (optional)",
                placeholder="Best number for a callback",
            )
            property_hint = st.text_input(
                "Property address or area (optional)",
                placeholder="City or full address if you already have a specific property",
            )
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
                placeholder="Unit count, timeline, current tenant status, or any details that help us respond.",
                height=170,
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
                            "property": property_hint.strip(),
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
                follow = f"**{cfg.EMAIL}**"
                if cfg.has_public_phone():
                    follow += f" or **{cfg.PHONE_DISPLAY}**"
                st.success(
                    "Thanks — your message was recorded in this session only (demo). "
                    f"For a real inquiry, please email {follow}."
                )

st.divider()
st.page_link("streamlit_app.py", label="Back to home", icon="🏠")

theme.render_footer()
