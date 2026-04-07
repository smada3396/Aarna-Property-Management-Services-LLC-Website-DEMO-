"""Contact form and direct channels."""

from __future__ import annotations

import streamlit as st

import business_config as cfg
import mailer
import theme

theme.setup_page("Contact")
theme.inject_css()
theme.render_top_bar()

st.markdown('<p class="aarna-section-title">Contact</p>', unsafe_allow_html=True)
st.markdown(
    "<p class='aarna-muted'>Tell us about your property or question. We follow up using the contact information you provide.</p>",
    unsafe_allow_html=True,
)


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
                <p style="margin:0;font-size:1.02rem;color:#5a6b7c;"><strong>Hours</strong><br/>{cfg.BUSINESS_HOURS}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="aarna-card" style="margin-top:1rem;">
                <h3 style="margin-top:0;">What to expect</h3>
                <p style="margin:0;font-size:1.05rem;color:#4a5a6e;line-height:1.58;">{cfg.RESPONSE_POLICY}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
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
                    "Owner: full management",
                    "Owner: leasing only or one time",
                    "Resident or applicant question",
                    "Vendor or partnership",
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
            elif not mailer.smtp_ready():
                st.warning(
                    f"This form cannot send mail until SMTP is configured for the app. "
                    f"Please write to **{cfg.EMAIL}** directly."
                )
            else:
                ok, err = mailer.send_contact_email(
                    visitor_name=name.strip(),
                    visitor_email=email.strip(),
                    visitor_phone=phone.strip(),
                    property_hint=property_hint.strip(),
                    topic=topic,
                    message=message.strip(),
                )
                if ok:
                    st.success("Thank you. Your message was sent. We will get back to you shortly.")
                elif err == "auth":
                    st.error("Email could not be sent (sign in problem). Please contact us by email or phone.")
                else:
                    st.warning(
                        f"We could not send your message right now. Please email **{cfg.EMAIL}** or call the office."
                    )

st.divider()
theme.page_link_with_icon("Home.py", "Back to home", "home", use_container_width=True)

theme.render_footer()
