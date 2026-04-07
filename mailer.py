"""Send contact form notifications to the business inbox via SMTP (e.g. Gmail)."""

from __future__ import annotations

import smtplib
from email.message import EmailMessage

import streamlit as st

import business_config as cfg


def smtp_ready() -> bool:
    try:
        return bool(str(st.secrets["SMTP_PASSWORD"]).strip())
    except Exception:
        return False


def send_contact_email(
    *,
    visitor_name: str,
    visitor_email: str,
    visitor_phone: str,
    property_hint: str,
    topic: str,
    message: str,
) -> tuple[bool, str]:
    """Send plain text email to cfg.EMAIL. Requires Streamlit secret SMTP_PASSWORD (Gmail app password)."""
    try:
        password = str(st.secrets["SMTP_PASSWORD"]).strip()
    except Exception:
        return False, "missing_config"

    try:
        smtp_user = str(st.secrets["SMTP_USER"]).strip()
    except Exception:
        smtp_user = cfg.EMAIL
    try:
        host = str(st.secrets["SMTP_HOST"]).strip()
    except Exception:
        host = "smtp.gmail.com"
    try:
        port = int(st.secrets["SMTP_PORT"])
    except Exception:
        port = 587

    to_addr = cfg.EMAIL
    lines = [
        f"Name: {visitor_name}",
        f"Email: {visitor_email}",
        f"Phone: {visitor_phone or '(not provided)'}",
        f"Property / area: {property_hint or '(not provided)'}",
        f"Topic: {topic}",
        "",
        "Message:",
        message,
        "",
        "Sent from the Aarna Property Management website contact form.",
    ]
    body = "\n".join(lines)

    msg = EmailMessage()
    msg["Subject"] = f"Website contact: {topic}"
    msg["From"] = smtp_user
    msg["To"] = to_addr
    msg["Reply-To"] = visitor_email
    msg.set_content(body)

    try:
        with smtplib.SMTP(host, port, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(smtp_user, password)
            smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        return False, "auth"
    except OSError:
        return False, "network"
    except Exception:
        return False, "send"

    return True, ""
