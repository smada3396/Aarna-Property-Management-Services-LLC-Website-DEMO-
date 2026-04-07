"""Shared Streamlit layout, CSS, and helpers for the Aarna site."""

from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st

import business_config as cfg

_ASSETS = Path(__file__).resolve().parent / "assets"
_LOGO_MARK = _ASSETS / "logo.svg"
_LOGO_FULL = _ASSETS / "logo-full.svg"

# Minimal stroke icons (currentColor) for navigation rows
_SVG_WRAP = '<div class="aarna-nav-svg" aria-hidden="true">{inner}</div>'
_NAV_ICONS: dict[str, str] = {
    "services": _SVG_WRAP.format(
        inner='<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
        '<line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/>'
        '<line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/>'
        '<line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>'
    ),
    "about": _SVG_WRAP.format(
        inner='<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>'
    ),
    "residents": _SVG_WRAP.format(
        inner='<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M3 21h18"/><path d="M5 21V7l7-3.5L19 7v14"/><path d="M9 21v-4h6v4"/>'
        '<path d="M10 10h.01"/><path d="M14 10h.01"/><path d="M10 14h.01"/><path d="M14 14h.01"/></svg>'
    ),
    "contact": _SVG_WRAP.format(
        inner='<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>'
        '<polyline points="22,6 12,13 2,6"/></svg>'
    ),
    "home": _SVG_WRAP.format(
        inner='<svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 24 24" fill="none" '
        'stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">'
        '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'
        '<polyline points="9 22 9 12 15 12 15 22"/></svg>'
    ),
}


def setup_page(
    page_title: str,
    *,
    layout: str = "wide",
    sidebar: str = "expanded",
) -> None:
    title = f"{cfg.SHORT_NAME} | {page_title}" if page_title else cfg.COMPANY_NAME
    kwargs: dict = {
        "page_title": title,
        "layout": layout,
        "initial_sidebar_state": sidebar,
        "menu_items": {
            "Get help": None,
            "Report a bug": None,
            "About": None,
        },
    }
    if _LOGO_MARK.is_file():
        kwargs["page_icon"] = str(_LOGO_MARK)
    st.set_page_config(**kwargs)


def page_link_with_icon(
    page: str,
    label: str,
    icon_key: str,
    *,
    use_container_width: bool = True,
    icon_col_weight: float = 2.25,
    label_col_weight: float = 9.75,
) -> None:
    """Row with a line icon and a Streamlit page link (no emoji)."""
    ic, lk = st.columns([icon_col_weight, label_col_weight], gap="small")
    with ic:
        svg = _NAV_ICONS.get(icon_key, "")
        st.markdown(f'<div class="aarna-ilink-wrap">{svg}</div>', unsafe_allow_html=True)
    with lk:
        st.page_link(page, label=label, icon=None, use_container_width=use_container_width)


def page_links_nav_row(
    entries: list[tuple[str, str, str]],
    *,
    use_container_width: bool = True,
) -> None:
    """Horizontal row of icon + page link groups (e.g. main site shortcuts on Home)."""
    cols = st.columns(len(entries), gap="small")
    for col, (page, label, icon_key) in zip(cols, entries, strict=True):
        with col:
            page_link_with_icon(
                page,
                label,
                icon_key,
                use_container_width=use_container_width,
                icon_col_weight=1.2,
                label_col_weight=3.4,
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
                scroll-padding-top: 6.5rem;
            }

            html, body {
                font-family: "DM Sans", "Segoe UI", system-ui, sans-serif;
            }
            [class*="stMarkdown"] h1, [class*="stMarkdown"] h2,
            .aarna-section-title, .aarna-hero h1, .aarna-card h3 {
                font-family: "Plus Jakarta Sans", "DM Sans", system-ui, sans-serif;
            }

            .stApp {
                background: linear-gradient(165deg, #e8eef5 0%, #f2f5f9 22%, #fafbfc 55%, #ffffff 100%) !important;
            }

            header[data-testid="stHeader"] {
                background: rgba(255, 255, 255, 0.98) !important;
                border-bottom: 1px solid #dde5ee !important;
                backdrop-filter: blur(10px);
            }
            div[data-testid="stDecoration"] {
                display: none;
            }

            div[data-testid="stToolbar"] {
                background: transparent !important;
            }

            section[data-testid="stMain"] > div {
                padding-top: 1.25rem !important;
            }

            .main .block-container {
                padding-top: 6rem !important;
                padding-bottom: 4rem !important;
                padding-left: clamp(1rem, 4vw, 2.75rem) !important;
                padding-right: clamp(1rem, 4vw, 2.75rem) !important;
                max-width: 1140px !important;
                font-size: 1.0625rem !important;
            }

            .aarna-ilink-wrap {
                display: flex;
                align-items: center;
                justify-content: center;
                min-height: 3.35rem;
                height: 100%;
                color: #0f2744;
            }
            .aarna-nav-svg {
                display: flex;
                align-items: center;
                justify-content: center;
                line-height: 0;
            }
            .aarna-nav-svg svg {
                display: block;
                vertical-align: middle;
            }

            /*
             * Icon + page_link: only the inner two-column Streamlit row (not an outer 3+ column row).
             * Matches blocks with a page link but no third top-level column.
             */
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))),
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) {
                align-items: center !important;
                margin-bottom: 0.55rem !important;
            }
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) > div[data-testid="column"],
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) > div[data-testid="column"] {
                display: flex !important;
                flex-direction: column !important;
                justify-content: center !important;
                align-self: stretch !important;
            }
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) > div[data-testid="column"] > div[data-testid="stVerticalBlock"],
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) > div[data-testid="column"] > div[data-testid="stVerticalBlock"] {
                justify-content: center !important;
                width: 100%;
            }
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) [data-testid="stMarkdownContainer"] p,
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) [data-testid="stMarkdownContainer"] p {
                margin: 0 !important;
                padding: 0 !important;
                line-height: 1 !important;
            }
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) div[data-testid="stPageLink-NavButton"],
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) div[data-testid="stPageLinkNavButton"] {
                display: flex !important;
                align-items: center !important;
                margin: 0 !important;
            }
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLink-NavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) div[data-testid="stPageLink-NavButton"] a,
            div[data-testid="stHorizontalBlock"]:has([data-testid="stPageLinkNavButton"]):not(:has(> div[data-testid="column"]:nth-child(3))) div[data-testid="stPageLinkNavButton"] a {
                margin: 0 !important;
            }

            /* Four-up nav row on Home: equal-height cells */
            div[data-testid="stHorizontalBlock"]:has(> div[data-testid="column"]:nth-child(4)) {
                align-items: stretch !important;
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

            div[data-testid="stAlert"] {
                border-radius: 12px !important;
                border: 1px solid #c5e4d9 !important;
                background: linear-gradient(90deg, #e8f6f2 0%, #f0faf7 100%) !important;
                font-size: 1.05rem !important;
            }

            .aarna-hero {
                background: linear-gradient(145deg, #0c2238 0%, #143a5c 42%, #1a4a6e 78%, #0f2744 100%);
                color: #f4f7fa;
                padding: 2.75rem 2.25rem;
                border-radius: 18px;
                margin-bottom: 2rem;
                box-shadow: 0 20px 50px rgba(15, 39, 68, 0.28), 0 0 0 1px rgba(255,255,255,0.06) inset;
            }
            .aarna-hero-brand {
                display: flex;
                align-items: center;
                gap: 1.25rem;
                flex-wrap: wrap;
                margin-bottom: 1.5rem;
                padding-bottom: 1.35rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.14);
            }
            .aarna-hero-logo {
                max-height: 76px;
                width: auto;
                max-width: min(100%, 300px);
                display: block;
            }
            .aarna-hero-logo-mark {
                width: 64px;
                height: 64px;
                flex-shrink: 0;
                display: block;
            }
            .aarna-hero-company {
                display: flex;
                flex-direction: column;
                gap: 0.2rem;
                min-width: 0;
            }
            .aarna-hero-co-primary {
                font-family: "Plus Jakarta Sans", system-ui, sans-serif;
                font-size: clamp(1.4rem, 3.2vw, 1.95rem);
                font-weight: 700;
                color: #f4f7fa;
                letter-spacing: -0.02em;
                line-height: 1.15;
            }
            .aarna-hero-co-sub {
                font-size: 0.82rem;
                font-weight: 600;
                letter-spacing: 0.14em;
                text-transform: uppercase;
                color: #7ee8d0;
            }
            .aarna-hero h1 {
                font-size: clamp(2.05rem, 4.5vw, 2.75rem);
                font-weight: 700;
                margin: 0 0 0.85rem 0;
                letter-spacing: -0.03em;
                line-height: 1.18;
            }
            .aarna-hero p.lead {
                font-size: 1.2rem;
                opacity: 0.96;
                margin: 0 0 0.6rem 0;
                line-height: 1.6;
                max-width: 42rem;
            }
            .aarna-hero p.sub {
                font-size: 1.05rem;
                opacity: 0.9;
                margin: 0;
                line-height: 1.55;
                max-width: 40rem;
            }
            .aarna-badge {
                display: inline-block;
                background: rgba(61, 184, 156, 0.22);
                color: #c5f5e8;
                font-size: 0.78rem;
                font-weight: 600;
                letter-spacing: 0.16em;
                padding: 0.45rem 0.85rem;
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
                font-size: 1.2rem;
                margin: 0 0 0.55rem 0;
                color: #0f2744;
                font-weight: 600;
            }
            .aarna-card p {
                margin: 0;
                font-size: 1.06rem;
                color: #4a5a6e;
                line-height: 1.62;
            }

            .aarna-section-title {
                font-size: 1.65rem;
                font-weight: 700;
                color: #0f2744;
                margin: 0 0 0.85rem 0;
                letter-spacing: -0.025em;
            }
            .aarna-muted {
                color: #5a6b7c;
                font-size: 1.08rem;
                line-height: 1.65;
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
                font-size: 0.98rem;
                color: #c5dde8;
                padding-left: 1.15rem;
                position: relative;
                line-height: 1.5;
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
                grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
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
                font-size: 1.06rem;
                margin-bottom: 0.4rem;
                font-family: "Plus Jakarta Sans", sans-serif;
            }
            .aarna-step span {
                color: #5a6b7c;
                font-size: 1.02rem;
                line-height: 1.58;
            }

            .aarna-footer {
                margin-top: 3.5rem;
                padding-top: 1.75rem;
                border-top: 1px solid #dde5ee;
                font-size: 0.92rem;
                color: #7a8a9c;
                line-height: 1.58;
            }

            .aarna-topbar-minimal {
                display: flex;
                align-items: center;
                gap: 1rem;
                flex-wrap: wrap;
                margin-bottom: 1.35rem;
                padding: 0.15rem 0;
            }
            .aarna-topbar-minimal-logo {
                max-height: 52px;
                width: auto;
                max-width: 240px;
                display: block;
            }
            .aarna-topbar-minimal-name {
                font-family: "Plus Jakarta Sans", system-ui, sans-serif;
                font-size: 1.12rem;
                font-weight: 600;
                color: #0f2744;
                letter-spacing: -0.02em;
                line-height: 1.25;
            }

            div[data-testid="stSidebarContent"] {
                background: linear-gradient(180deg, #0a1f35 0%, #0f2744 45%, #122a47 100%) !important;
                border-right: 1px solid rgba(255,255,255,0.06);
            }
            div[data-testid="stSidebarContent"] p,
            div[data-testid="stSidebarContent"] span,
            div[data-testid="stSidebarContent"] label {
                color: #e8eef4 !important;
            }
            div[data-testid="stSidebarNav"] { padding-top: 0.35rem; }
            div[data-testid="stSidebarNav"] ul { gap: 0.15rem; }
            div[data-testid="stSidebarNav"] li { margin: 0.1rem 0; }
            div[data-testid="stSidebarNav"] a {
                border-radius: 10px !important;
                padding: 0.5rem 0.65rem !important;
                margin: 0.1rem 0 !important;
            }
            div[data-testid="stSidebarNav"] a span {
                color: #e8eef4 !important;
                font-weight: 500 !important;
                font-size: 1.04rem !important;
                letter-spacing: 0.01em;
            }
            div[data-testid="stSidebarNav"] a:hover span { color: #7ee8d0 !important; }
            div[data-testid="stSidebarNav"] li:has(a[aria-current="page"]) {
                background: rgba(61, 184, 156, 0.18) !important;
                border-radius: 10px;
            }
            div[data-testid="stSidebarNav"] a[aria-current="page"] span {
                color: #7ee8d0 !important;
                font-weight: 600 !important;
            }

            div[data-testid="stPageLink-NavButton"] a,
            div[data-testid="stPageLinkNavButton"] a {
                display: flex !important;
                align-items: center;
                justify-content: flex-start;
                padding: 0.85rem 1.15rem !important;
                border-radius: 12px !important;
                border: 1px solid #d0dbe8 !important;
                background: #ffffff !important;
                font-weight: 600 !important;
                font-size: 1.1rem !important;
                color: #0f2744 !important;
                min-height: 3.35rem !important;
                box-sizing: border-box !important;
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
                font-size: 1.05rem !important;
                border-radius: 10px !important;
                padding: 0.55rem 1.35rem !important;
                box-shadow: 0 4px 14px rgba(61, 184, 156, 0.35) !important;
            }
            div[data-testid="stButton"] button[kind="primary"]:hover {
                background: linear-gradient(180deg, #4dd4b2 0%, #36a88e 100%) !important;
                border-color: #2a9d7a !important;
            }

            div[data-baseweb="input"] > div { border-radius: 10px !important; }
            div[data-baseweb="select"] > div { border-radius: 10px !important; }
            div[data-baseweb="select"] div[role="combobox"] span,
            ul[data-baseweb="menu"] li {
                font-size: 1.05rem !important;
            }
            div[data-baseweb="input"] input,
            div[data-baseweb="textarea"] textarea {
                font-size: 1.05rem !important;
            }
            [data-testid="stWidgetLabel"] p,
            label[data-testid="stWidgetLabel"] {
                font-size: 1.02rem !important;
            }

            .aarna-topbar-minimal-mark {
                width: 48px;
                height: 48px;
                flex-shrink: 0;
            }

            @media (prefers-color-scheme: dark) {
                .stApp {
                    background: linear-gradient(165deg, #0d1520 0%, #121c2b 35%, #151f30 100%) !important;
                }
                header[data-testid="stHeader"] {
                    background: rgba(13, 21, 32, 0.96) !important;
                    border-bottom: 1px solid #2a3a50 !important;
                }
                .main .block-container {
                    background: transparent !important;
                }
                .aarna-card, .aarna-step {
                    background: #1a2636 !important;
                    border-color: #2d3f56 !important;
                    box-shadow: 0 4px 24px rgba(0,0,0,0.35) !important;
                }
                .aarna-card h3, .aarna-section-title, .aarna-step strong {
                    color: #e8eef4 !important;
                }
                .aarna-card p, .aarna-muted, .aarna-step span {
                    color: #b4c0d4 !important;
                }
                .aarna-topbar-minimal-name {
                    color: #e8eef4 !important;
                }
                .aarna-footer {
                    border-top-color: #2d3f56 !important;
                    color: #8a9bb4 !important;
                }
                .main a, div[data-testid="stMarkdownContainer"] a {
                    color: #6ecfff !important;
                }
                .main a:hover, div[data-testid="stMarkdownContainer"] a:hover {
                    color: #7ee8d0 !important;
                }
                .aarna-ilink-wrap { color: #8ecfff !important; }
                div[data-testid="stAlert"] {
                    background: linear-gradient(90deg, #152535 0%, #1a3045 100%) !important;
                    border-color: #2d5a4a !important;
                }
                div[data-testid="stPageLink-NavButton"] a,
                div[data-testid="stPageLinkNavButton"] a {
                    background: #1e2d40 !important;
                    border-color: #3d5269 !important;
                    color: #e8eef4 !important;
                }
                div[data-testid="stMarkdownContainer"] p,
                div[data-testid="stMarkdownContainer"] li,
                div[data-testid="stMarkdownContainer"] label {
                    color: #c5d0e0 !important;
                }
                div[data-baseweb="input"] input,
                div[data-baseweb="textarea"] textarea {
                    background-color: #1a2636 !important;
                    color: #e8eef4 !important;
                    border-color: #3d5269 !important;
                    font-size: 1.05rem !important;
                }
                div[data-baseweb="select"] > div {
                    background-color: #1a2636 !important;
                    color: #e8eef4 !important;
                    border-color: #3d5269 !important;
                }
                [data-testid="stWidgetLabel"] p,
                label[data-testid="stWidgetLabel"] { color: #b4c0d4 !important; font-size: 1.02rem !important; }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero_brand_html() -> str:
    """Logo + Aarna Property Management name for the home hero (on navy background)."""
    full_uri = _svg_data_uri(_LOGO_FULL)
    mark_uri = _svg_data_uri(_LOGO_MARK)
    if full_uri:
        img = f'<img src="{full_uri}" class="aarna-hero-logo" alt="{cfg.COMPANY_NAME}"/>'
    elif mark_uri:
        img = f'<img src="{mark_uri}" class="aarna-hero-logo-mark" alt="{cfg.SHORT_NAME} logo"/>'
    else:
        img = ""
    names = (
        '<div class="aarna-hero-company">'
        '<span class="aarna-hero-co-primary">Aarna Property Management</span>'
        '<span class="aarna-hero-co-sub">Services, LLC</span>'
        "</div>"
    )
    return f'<div class="aarna-hero-brand">{img}{names}</div>'


def render_top_bar() -> None:
    """Compact logo + legal name only (no white card, no service area paragraph)."""
    full_uri = _svg_data_uri(_LOGO_FULL)
    mark_uri = _svg_data_uri(_LOGO_MARK)
    parts: list[str] = ['<div class="aarna-topbar-minimal">']
    if full_uri:
        parts.append(
            f'<img src="{full_uri}" class="aarna-topbar-minimal-logo" alt="{cfg.COMPANY_NAME}"/>'
        )
    elif mark_uri:
        parts.append(
            f'<img src="{mark_uri}" class="aarna-topbar-minimal-mark" alt=""/>'
        )
    parts.append(f'<span class="aarna-topbar-minimal-name">{cfg.COMPANY_NAME}</span></div>')
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
