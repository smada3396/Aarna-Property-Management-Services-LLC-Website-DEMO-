# Business copy and contact details for the public site (aligned with company brochure).

COMPANY_NAME = "Aarna Property Management Services, LLC"
SHORT_NAME = "Aarna"

TAGLINE = "Maryland property management built on clarity, care, and consistent execution."
HERO_SUBTITLE = (
    "We represent owners, support residents, and protect the long-term condition and income "
    "of single-family homes, townhomes, and small multifamily properties across the region."
)

# Contact — from brochure (2024)
EMAIL = "aarnapropertymanagement@gmail.com"

PHONE_OFFICE_DISPLAY = "(667) 280-0887"
PHONE_OFFICE_TEL = "+16672800887"
PHONE_MOBILE_DISPLAY = "(301) 910-0266"
PHONE_MOBILE_TEL = "+13019100266"

# Primary number for single tel: links and short CTAs
PHONE_DISPLAY = PHONE_OFFICE_DISPLAY
PHONE_TEL = PHONE_OFFICE_TEL

ADDRESS_LINE1 = "8415 Old Frederick Road"
ADDRESS_LINE2 = "Ellicott City, MD 21043"

SERVICE_AREA = (
    "Based in Ellicott City, Howard County, we serve Maryland with a strong presence in the Baltimore metro "
    "and nearby communities including Carroll, Frederick, and surrounding counties."
)

BUSINESS_HOURS = "Monday–Friday, 9:00 a.m.–5:00 p.m. ET (evenings and weekends by appointment)."
RESPONSE_POLICY = (
    "We aim to acknowledge new inquiries within one business day. "
    "Current residents should use the contact instructions provided in their lease or welcome packet."
)

CREDENTIALS_LINE = "Licensed & insured — credentials and references available upon request."

# Service pillars summarized from the company brochure
SERVICES = [
    {
        "title": "Leasing & screening",
        "body": (
            "Market analysis, marketing vacancies, rental applications, and lease signing—in coordination with "
            "real estate partners when you use a realtor. We conduct thorough screening: credit and criminal "
            "background review, rental history, and employment and income verification."
        ),
    },
    {
        "title": "Operations & compliance",
        "body": (
            "Rental inspections, rental license processing, move-in and move-out walkthroughs, escrow handling for "
            "security deposits, and attention to HOA rules and county regulations—including winterization and HOA "
            "coordination where applicable."
        ),
    },
    {
        "title": "Financial administration",
        "body": (
            "Electronic processing of rental payments so owners get paid on time, billing and collections with "
            "documentation of repairs when needed, and clear annual owner rental statements that summarize income, "
            "expenses (including management fees), charges, and portfolio profitability."
        ),
    },
    {
        "title": "Residents, maintenance & recovery",
        "body": (
            "Responsive handling of tenant inquiries and maintenance coordination across common trades. When "
            "necessary, we coordinate evictions and recovery of the rental in line with applicable law."
        ),
    },
]

SERVICE_EXTRAS = [
    "Electrical, plumbing, HVAC, handyman repairs, painting, and cleaning",
    "Flood restoration, gutters / power washing, and landscape coordination",
    "Focus on low vacancy and competitive time on market",
]

SCREENING_HIGHLIGHT = (
    "We conduct a thorough application and extensive screening on all prospective tenants—including credit and "
    "criminal screening, past rental history, and employment and income verification."
)

WHY_US = [
    (
        "Rigorous resident screening",
        SCREENING_HIGHLIGHT,
    ),
    (
        "Reliable rent and reporting",
        "Electronic rent processing with timely owner disbursements and streamlined owner statements that show "
        "profitability, balances, income, expenses, and rent activity.",
    ),
    (
        "Local, hands-on operations",
        "Maintenance addressed quickly and thoroughly—from everyday repairs to compliance with HOA and county expectations.",
    ),
]

HOME_TRUST_POINTS = [
    ("Howard County roots", "Office in Ellicott City—serving owners across the greater Maryland region."),
    ("Screening & compliance", "Structured applications, documentation, and regulatory awareness."),
    ("Owner peace of mind", "We handle day-to-day operations so you can focus on your investment."),
]

PROCESS_STEPS = [
    ("1. Intro call", "We learn your goals, property details, and timeline."),
    ("2. Scope & agreement", "We align on services, fees, and how you want to be updated."),
    ("3. Onboarding", "Leases, vendors, and systems are organized for a clean handoff."),
    ("4. Ongoing management", "Day-to-day operations with reporting you can actually use."),
]

ABOUT_LEAD = (
    f"{COMPANY_NAME} helps property owners run residential rentals with less friction and more predictability. "
    "Our office is in Ellicott City, Maryland; we emphasize clear expectations, timely follow-through, and "
    "documentation you can stand behind."
)

ABOUT_BODY = (
    "Whether you are local or out of state, a first-time landlord or scaling a small portfolio, "
    "we tailor management intensity to your property and risk profile. We believe neighborhoods are stronger "
    "when rentals are well maintained and relationships between owners and residents stay professional."
)

RESIDENT_INTRO = (
    "This site is mainly for property owners and prospects. If you rent from us, your lease and welcome "
    "materials are the official source for how to pay rent, request repairs, and reach your property team."
)

RESIDENT_TOPICS = [
    (
        "Maintenance requests",
        "Use the process spelled out in your lease (portal, email, or phone). "
        "For emergencies such as fire, gas smell, or major water intrusion, follow the emergency numbers "
        "you were given at move-in.",
    ),
    (
        "Rent and account questions",
        "Pay and correspond through the channel designated for your property so payments and notices are tracked correctly.",
    ),
    (
        "Applications and showings",
        "If you are applying for a vacancy we advertise, use the application link or instructions in the listing. "
        "We process applications fairly and in line with applicable law.",
    ),
    (
        "General questions for our office",
        "If you are unsure where to direct something, use the contact form and choose “Resident / applicant question,” "
        "or email us—include your property address so we can route your message.",
    ),
]


def has_public_phone() -> bool:
    return bool(str(PHONE_OFFICE_DISPLAY).strip() and str(PHONE_OFFICE_TEL).strip())
