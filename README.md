# Aarna Property Management — Streamlit site

Multipage marketing site: Services, About, Residents, Contact. Copy and contact details live in `business_config.py`.

## Run locally

```bash
cd UI
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run Home.py
```

## Streamlit Cloud

1. Push this `UI` folder as the **repo root** (so `Home.py` is at the top level).
2. App **Settings** → **Main file path**: **`Home.py`**.
3. Optional: **Secrets** → `FORMSPREE_ENDPOINT = "https://formspree.io/f/..."` so the contact form emails you.

**Page filenames** (`2_About_Us.py`, etc.): Streamlit builds URL pathnames from the name after the leading `123_`. Two files like `2_About.py` and `3_About.py` both map to `/About` and crash on Streamlit 1.56+. Do not add duplicate stems.

## Files

| Path | Role |
|------|------|
| `Home.py` | Landing page |
| `pages/1_Services.py` | Services |
| `pages/2_About_Us.py` | About |
| `pages/3_For_Residents.py` | Residents / applicants |
| `pages/4_Contact_Us.py` | Contact form |
| `business_config.py` | Business copy, email, phones, address |
| `theme.py` | Layout + CSS |
| `assets/logo.svg` | Square mark (fallback) |
| `assets/logo-full.svg` | Header wordmark |
| `.streamlit/config.toml` | Theme / client options |
| `requirements.txt` | Dependencies |

## License

For **Aarna Property Management Services, LLC** internal use; respect third‑party font/logo licenses.
