# Aarna Property Management Services — Streamlit site

Professional multipage site for prospects: services, about, residents, and contact (optional Formspree).

## Run locally

```bash
cd UI
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run Home.py
```

## Deploy on Streamlit Community Cloud

1. Create a **new GitHub repository** and upload **everything inside this `UI` folder** as the repo root (so `Home.py` is at the top level of the repository).
2. Sign in at [Streamlit Community Cloud](https://streamlit.io/cloud) and **New app** → pick the repo and branch.
3. Set **Main file path** to **`Home.py`** (required — this is the home page and fixes the sidebar label “streamlit app”).
4. Deploy.

### Optional: deliver contact form to your inbox

1. Create a free form endpoint at [Formspree](https://formspree.io/) (or similar).
2. In Streamlit Cloud → your app → **Settings** → **Secrets**, add:

   ```toml
   FORMSPREE_ENDPOINT = "https://formspree.io/f/your-form-id"
   ```

3. Redeploy. Submissions from **Contact** will POST to that URL.

If you skip secrets, the form still works as a demo and tells visitors to email or call using `business_config.py`.

## Customize copy and contact info

Edit **`business_config.py`**: company name, taglines, email, office/mobile phones (`PHONE_OFFICE_*`, `PHONE_MOBILE_*`), street address, service area, hours, services, and resident/owner copy blocks.

## Project layout

| Path | Purpose |
|------|---------|
| `Home.py` | Home / hero (sidebar: **Home**) |
| `pages/1_Services.py` | Services |
| `pages/2_About.py` | About |
| `pages/3_Residents.py` | Residents & applicants |
| `pages/4_Contact.py` | Contact form + direct channels |
| `theme.py` | Shared styles and chrome |
| `assets/logo.svg` | Brand mark (square) |
| `assets/logo-full.svg` | Horizontal wordmark (header) |
| `.streamlit/config.toml` | Theme tokens & client options |

Sidebar order: **Home** → Services → About → Residents → Contact.

## License

Use and modify for **Aarna Property Management Services, LLC** operations. Third-party logos or fonts remain subject to their respective licenses.
