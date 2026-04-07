"""Shared Streamlit layout, CSS, and helpers for the Aarna site."""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

import business_config as cfg

_ASSETS = Path(__file__).resolve().parent / "assets"
_LOGO_SVG = _ASSETS / "logo.svg"


def setup_page(
    page_title: str,
    *,
    layout: str = "wide",
    sidebar: str = "expanded",
) -> None:
    title = f"{cfg.SHORT_NAME} — {page_title}" if page_title else cfg.COMPANY_NAME
    st.set_page_config(
        page_title=title,
        page_icon="🏠",
        layout=layout,
        initial_sidebar_state=sidebar,
        menu_items={
            "Get help": None,
            "Report a bug": None,
            "About": None,
        },
    )


def _logo_data_uri() -> str | None:
    if not _LOGO_SVG.is_file():
        return None
    raw = _LOGO_SVG.read_bytes()
    b64 = base64.standard_b64encode(raw).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


def inject_css() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

            html, body, [class*="css"]  {
                font-family: "DM Sans", "Segoe UI", system-ui, sans-serif;
            }

            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 3rem;
                max-width: 1100px;
            }

            .aarna-hero {
                background: linear-gradient(135deg, #0f2744 0%, #1a4a6e 55%, #0f2744 100%);
                color: #f4f7fa;
                padding: 2.5rem 2rem;
                border-radius: 16px;
                margin-bottom: 2rem;
                box-shadow: 0 12px 40px rgba(15, 39, 68, 0.25);
            }
            .aarna-hero h1 {
                font-size: clamp(1.75rem, 4vw, 2.35rem);
                font-weight: 700;
                margin: 0 0 0.75rem 0;
                letter-spacing: -0.02em;
                line-height: 1.2;
            }
            .aarna-hero p.lead {
                font-size: 1.1rem;
                opacity: 0.95;
                margin: 0 0 0.5rem 0;
                line-height: 1.55;
                max-width: 38rem;
            }
            .aarna-hero p.sub {
                font-size: 0.95rem;
                opacity: 0.85;
                margin: 0;
                line-height: 1.5;
                max-width: 36rem;
            }
            .aarna-badge {
                display: inline-block;
                background: rgba(61, 184, 156, 0.25);
                color: #b8f0e0;
                font-size: 0.72rem;
                font-weight: 600;
                letter-spacing: 0.14em;
                padding: 0.35rem 0.65rem;
                border-radius: 6px;
                margin-bottom: 1rem;
                text-transform: uppercase;
            }

            .aarna-card {
                background: #ffffff;
                border: 1px solid #e4e9f0;
                border-radius: 12px;
                padding: 1.35rem 1.25rem;
                height: 100%;
                box-shadow: 0 2px 12px rgba(15, 39, 68, 0.06);
            }
            .aarna-card h3 {
                font-size: 1.05rem;
                margin: 0 0 0.5rem 0;
                color: #0f2744;
            }
            .aarna-card p {
                margin: 0;
                font-size: 0.95rem;
                color: #4a5a6e;
                line-height: 1.55;
            }

            .aarna-section-title {
                font-size: 1.35rem;
                font-weight: 700;
                color: #0f2744;
                margin: 0 0 1rem 0;
                letter-spacing: -0.02em;
            }
            .aarna-muted {
                color: #5a6b7c;
                font-size: 0.95rem;
                line-height: 1.55;
            }

            .aarna-footer {
                margin-top: 3rem;
                padding-top: 1.5rem;
                border-top: 1px solid #e4e9f0;
                font-size: 0.82rem;
                color: #7a8a9c;
                line-height: 1.5;
            }

            div[data-testid="stSidebarContent"] {
                background: linear-gradient(180deg, #0f2744 0%, #152a45 100%);
            }
            div[data-testid="stSidebarContent"] p, div[data-testid="stSidebarContent"] span,
            div[data-testid="stSidebarContent"] label {
                color: #e8eef4 !important;
            }
            div[data-testid="stSidebarNav"] a span {
                color: #f4f7fa !important;
            }
            div[data-testid="stSidebarNav"] a:focus span, div[data-testid="stSidebarNav"] a:hover span {
                color: #3db89c !important;
            }

            /* Primary buttons */
            div[data-testid="stButton"] button[kind="primary"] {
                background-color: #3db89c !important;
                border-color: #3db89c !important;
                color: #0f2744 !important;
                font-weight: 600 !important;
            }
            div[data-testid="stButton"] button[kind="primary"]:hover {
                background-color: #2fa889 !important;
                border-color: #2fa889 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_top_bar() -> None:
    uri = _logo_data_uri()
    cols = st.columns([1, 4])
    with cols[0]:
        if uri:
            st.markdown(
                f'<img src="{uri}" width="72" alt="{cfg.SHORT_NAME} logo"/>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(f"### {cfg.SHORT_NAME}")
    with cols[1]:
        st.markdown(
            f'<p style="margin:0;padding-top:0.5rem;color:#5a6b7c;font-size:0.95rem;">'
            f"<strong style=color:#0f2744>{cfg.COMPANY_NAME}</strong></p>",
            unsafe_allow_html=True,
        )


def render_footer() -> None:
    st.markdown(
        f"""
        <div class="aarna-footer">
            © {cfg.COMPANY_NAME}. This site is for general information and does not constitute a contract or offer.
            {cfg.CREDENTIALS_LINE}
        </div>
        """,
        unsafe_allow_html=True,
    )
