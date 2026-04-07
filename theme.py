"""Shared Streamlit layout, CSS, and helpers for the Aarna site."""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

import business_config as cfg

_ASSETS = Path(__file__).resolve().parent / "assets"
_LOGO_MARK = _ASSETS / "logo.svg"
_LOGO_FULL = _ASSETS / "logo-full.svg"


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


def _svg_data_uri(path: Path) -> str | None:
    if not path.is_file():
        return None
    raw = path.read_bytes()
    b64 = base64.standard_b64encode(raw).decode("ascii")
    return f"data:image/svg+xml;base64,{b64}"


def inject_css() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap');

            html {
                scroll-padding-top: 5.5rem;
            }

            html, body {
                font-family: "DM Sans", "Segoe UI", system-ui, sans-serif;
            }
            [class*="stMarkdown"] h1, [class*="stMarkdown"] h2,
            .aarna-section-title, .aarna-hero h1, .aarna-card h3 {
                font-family: "Plus Jakarta Sans", "DM Sans", system-ui, sans-serif;
            }

            /* App canvas — subtle premium background */
            .stApp {
                background: linear-gradient(165deg, #e8eef5 0%, #f2f5f9 22%, #fafbfc 55%, #ffffff 100%) !important;
            }

            /* Keep Streamlit header visible but separated; push main content below it */
            header[data-testid="stHeader"] {
                background: rgba(255, 255, 255, 0.97) !important;
                border-bottom: 1px solid #dde5ee !important;
                backdrop-filter: blur(10px);
            }
            div[data-testid="stDecoration"] {
                display: none;
            }

            section[data-testid="stMain"] > div {
                padding-top: 0.75rem;
            }

            .main .block-container {
                padding-top: 3.5rem !important;
                padding-bottom: 4rem !important;
                padding-left: clamp(1rem, 4vw, 2.75rem) !important;
                padding-right: clamp(1rem, 4vw, 2.75rem) !important;
                max-width: 1140px !important;
            }

            .main a, div[data-testid="stMarkdownContainer"] a {
                color: #155a7d;
                font-weight: 500;
                text-decoration: none;
            }
            .main a:hover, div[data-testid="stMarkdownContainer"] a:hover {
                color: #2a9d7a;
                text-decoration: underline;
            }

            footer { visibility: hidden !important; height: 0 !important; }

            /* Alerts — calmer, on-brand */
            div[data-testid="stAlert"] {
                border-radius: 12px !important;
                border: 1px solid #c5e4d9 !important;
                background: linear-gradient(90deg, #e8f6f2 0%, #f0faf7 100%) !important;
            }

            .aarna-hero {
                background: linear-gradient(145deg, #0c2238 0%, #143a5c 42%, #1a4a6e 78%, #0f2744 100%);
                color: #f4f7fa;
                padding: 2.75rem 2.25rem;
                border-radius: 18px;
                margin-bottom: 2rem;
                box-shadow: 0 20px 50px rgba(15, 39, 68, 0.28), 0 0 0 1px rgba(255,255,255,0.06) inset;
            }
            .aarna-hero h1 {
                font-size: clamp(1.85rem, 4.2vw, 2.45rem);
                font-weight: 700;
                margin: 0 0 0.85rem 0;
                letter-spacing: -0.03em;
                line-height: 1.18;
            }
            .aarna-hero p.lead {
                font-size: 1.08rem;
                opacity: 0.96;
                margin: 0 0 0.6rem 0;
                line-height: 1.6;
                max-width: 42rem;
            }
            .aarna-hero p.sub {
                font-size: 0.94rem;
                opacity: 0.9;
                margin: 0;
                line-height: 1.55;
                max-width: 40rem;
            }
            .aarna-badge {
                display: inline-block;
                background: rgba(61, 184, 156, 0.22);
                color: #c5f5e8;
                font-size: 0.7rem;
                font-weight: 600;
                letter-spacing: 0.16em;
                padding: 0.4rem 0.75rem;
                border-radius: 8px;
                margin-bottom: 1.1rem;
                text-transform: uppercase;
                border: 1px solid rgba(61, 184, 156, 0.35);
            }

            .aarna-card {
                background: #ffffff;
                border: 1px solid #e1e8f0;
                border-radius: 14px;
                padding: 1.45rem 1.35rem;
                height: 100%;
                box-shadow: 0 2px 16px rgba(15, 39, 68, 0.055);
                border-left: 3px solid #3db89c;
            }
            .aarna-card h3 {
                font-size: 1.08rem;
                margin: 0 0 0.55rem 0;
                color: #0f2744;
                font-weight: 600;
            }
            .aarna-card p {
                margin: 0;
                font-size: 0.95rem;
                color: #4a5a6e;
                line-height: 1.6;
            }

            .aarna-section-title {
                font-size: 1.45rem;
                font-weight: 700;
                color: #0f2744;
                margin: 0 0 0.85rem 0;
                letter-spacing: -0.025em;
            }
            .aarna-muted {
                color: #5a6b7c;
                font-size: 0.97rem;
                line-height: 1.62;
            }

            .aarna-trust-bar {
                display: flex;
                flex-wrap: wrap;
                gap: 0.65rem 1.35rem;
                margin: 1.65rem 0 0.15rem 0;
                padding: 0;
                list-style: none;
            }
            .aarna-trust-bar li {
                font-size: 0.87rem;
                color: #c5dde8;
                padding-left: 1.15rem;
                position: relative;
                line-height: 1.45;
            }
            .aarna-trust-bar li::before {
                content: "";
                position: absolute;
                left: 0;
                top: 0.5em;
                width: 7px;
                height: 7px;
                border-radius: 50%;
                background: #3db89c;
                box-shadow: 0 0 0 2px rgba(61, 184, 156, 0.35);
            }

            .aarna-steps {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
                gap: 1.1rem;
                margin-top: 0.65rem;
            }
            .aarna-step {
                background: #ffffff;
                border: 1px solid #e4e9f0;
                border-radius: 14px;
                padding: 1.2rem 1.1rem;
                box-shadow: 0 2px 12px rgba(15, 39, 68, 0.04);
            }
            .aarna-step strong {
                display: block;
                color: #0f2744;
                font-size: 0.95rem;
                margin-bottom: 0.4rem;
                font-family: "Plus Jakarta Sans", sans-serif;
            }
            .aarna-step span {
                color: #5a6b7c;
                font-size: 0.9rem;
                line-height: 1.55;
            }

            .aarna-footer {
                margin-top: 3.5rem;
                padding-top: 1.75rem;
                border-top: 1px solid #dde5ee;
                font-size: 0.8rem;
                color: #7a8a9c;
                line-height: 1.55;
            }

            .aarna-topbar {
                display: flex;
                align-items: flex-start;
                gap: 1.15rem;
                flex-wrap: wrap;
                margin-bottom: 1.65rem;
            }
            .aarna-topbar-card {
                background: #ffffff;
                border: 1px solid #e1e8f0;
                border-radius: 16px;
                padding: 1.35rem 1.5rem;
                box-shadow: 0 8px 32px rgba(15, 39, 68, 0.08);
            }
            .aarna-topbar .tagline {
                margin: 0.35rem 0 0 0;
                font-size: 0.9rem;
                color: #5a6b7c;
                max-width: 38rem;
                line-height: 1.55;
            }

            /* Sidebar — navigation reads like a site menu */
            div[data-testid="stSidebarContent"] {
                background: linear-gradient(180deg, #0a1f35 0%, #0f2744 45%, #122a47 100%) !important;
                border-right: 1px solid rgba(255,255,255,0.06);
            }
            div[data-testid="stSidebarContent"] p,
            div[data-testid="stSidebarContent"] span,
            div[data-testid="stSidebarContent"] label {
                color: #e8eef4 !important;
            }
            div[data-testid="stSidebarNav"] {
                padding-top: 0.35rem;
            }
            div[data-testid="stSidebarNav"] ul {
                gap: 0.15rem;
            }
            div[data-testid="stSidebarNav"] li {
                margin: 0.1rem 0;
            }
            div[data-testid="stSidebarNav"] a {
                border-radius: 10px !important;
                padding: 0.5rem 0.65rem !important;
                margin: 0.1rem 0 !important;
            }
            div[data-testid="stSidebarNav"] a span {
                color: #e8eef4 !important;
                font-weight: 500 !important;
                font-size: 0.92rem !important;
                letter-spacing: 0.01em;
            }
            div[data-testid="stSidebarNav"] a:hover span {
                color: #7ee8d0 !important;
            }
            div[data-testid="stSidebarNav"] li:has(a[aria-current="page"]) {
                background: rgba(61, 184, 156, 0.18) !important;
                border-radius: 10px;
            }
            div[data-testid="stSidebarNav"] a[aria-current="page"] span {
                color: #7ee8d0 !important;
                font-weight: 600 !important;
            }

            /* In-page navigation buttons */
            div[data-testid="stPageLink-NavButton"] a,
            div[data-testid="stPageLinkNavButton"] a {
                display: flex !important;
                align-items: center;
                justify-content: center;
                padding: 0.7rem 1rem !important;
                border-radius: 12px !important;
                border: 1px solid #d0dbe8 !important;
                background: #ffffff !important;
                font-weight: 600 !important;
                color: #0f2744 !important;
                box-shadow: 0 2px 8px rgba(15, 39, 68, 0.06) !important;
                transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
            }
            div[data-testid="stPageLink-NavButton"] a:hover,
            div[data-testid="stPageLinkNavButton"] a:hover {
                border-color: #3db89c !important;
                box-shadow: 0 6px 20px rgba(61, 184, 156, 0.18) !important;
            }

            div[data-testid="stButton"] button[kind="primary"] {
                background: linear-gradient(180deg, #42c9a8 0%, #3db89c 100%) !important;
                border-color: #2fa889 !important;
                color: #06261f !important;
                font-weight: 600 !important;
                border-radius: 10px !important;
                padding: 0.5rem 1.25rem !important;
                box-shadow: 0 4px 14px rgba(61, 184, 156, 0.35) !important;
            }
            div[data-testid="stButton"] button[kind="primary"]:hover {
                background: linear-gradient(180deg, #4dd4b2 0%, #36a88e 100%) !important;
                border-color: #2a9d7a !important;
            }

            /* Form fields — slightly softer */
            div[data-baseweb="input"] > div {
                border-radius: 10px !important;
            }
            div[data-baseweb="select"] > div {
                border-radius: 10px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_top_bar() -> None:
    full_uri = _svg_data_uri(_LOGO_FULL)
    mark_uri = _svg_data_uri(_LOGO_MARK)
    parts: list[str] = ['<div class="aarna-topbar aarna-topbar-card">']
    if full_uri:
        parts.append(
            f'<div><img src="{full_uri}" style="max-width:min(100%,300px);height:auto;display:block;" '
            f'alt="{cfg.COMPANY_NAME}"/></div>'
        )
    elif mark_uri:
        parts.append(
            f'<div style="display:flex;align-items:center;gap:0.85rem;">'
            f'<img src="{mark_uri}" width="56" height="56" alt="{cfg.SHORT_NAME} mark"/>'
            f'<strong style="font-size:1.05rem;color:#0f2744;font-family:Plus Jakarta Sans,sans-serif;">'
            f"{cfg.COMPANY_NAME}</strong></div>"
        )
    else:
        parts.append(
            f'<div><strong style="font-size:1.1rem;color:#0f2744;font-family:Plus Jakarta Sans,sans-serif;">'
            f"{cfg.COMPANY_NAME}</strong></div>"
        )
    parts.append(
        f'<div style="flex:1;min-width:200px;"><p class="tagline">{cfg.SERVICE_AREA}</p></div>'
        "</div>"
    )
    st.markdown("".join(parts), unsafe_allow_html=True)


def render_footer() -> None:
    st.markdown(
        f"""
        <div class="aarna-footer">
            © {cfg.COMPANY_NAME}. Information on this site is general in nature and does not constitute a contract,
            lease, or offer. {cfg.CREDENTIALS_LINE}
        </div>
        """,
        unsafe_allow_html=True,
    )
