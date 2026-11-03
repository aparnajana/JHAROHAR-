import streamlit as st
import qrcode
from io import BytesIO
from datetime import datetime

st.set_page_config(
    page_title="JHAROHAR | Preserving Roots, Celebrating Art",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Theme ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
:root { --forest:#173f32; --green:#2f6b50; --sage:#e5eee5; --cream:#fbf8ef; --gold:#c99b45; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: var(--cream); }
section[data-testid="stSidebar"] { background: #173f32; }
section[data-testid="stSidebar"] * { color: #fff !important; }
h1,h2,h3 { color: var(--forest); }
.hero {
    background: linear-gradient(115deg, #173f32 0%, #285b43 65%, #52785a 100%);
    padding: 2.4rem 2.6rem; border-radius: 22px; color: white; margin-bottom: 1.3rem;
}
.hero h1 { color: #fff; font-family: 'Playfair Display', serif; font-size: 3.1rem; margin: 0; letter-spacing: 2px; }
.hero p { color: #f5f0df; font-size: 1.08rem; margin: .45rem 0 0; }
.eyebrow { color: #e5c47c; text-transform: uppercase; letter-spacing: 3px; font-size: .78rem; font-weight: 700; }
.card {
    background: #fffdf7; border: 1px solid #e7e0cf; border-radius: 16px;
    padding: 1rem 1.1rem; min-height: 145px; box-shadow: 0 4px 18px rgba(23,63,50,.05);
}
.card h3 { margin: .2rem 0 .45rem; font-size: 1.15rem; }
.muted { color: #65756a; font-size: .92rem; }
.pill { display:inline-block; background:#e5eee5; color:#285b43; border-radius:99px; padding:.25rem .65rem; font-size:.78rem; font-weight:600; }
div.stButton > button { background:#285b43; color:white; border:0; border-radius:10px; }
div.stButton > button:hover { background:#173f32; color:white; border:0; }
hr { border-color: #e7e0cf; }
</style>
""", unsafe_allow_html=True)

# ---------- Sample content ----------
ARTWORKS = [
    {"id":"JH-SOH-001","title":"Sohrai-inspired wall art","form":"Sohrai","region":"Hazaribagh","artist":"Demo Artist 1","price":"₹2,500","description":"A sample listing inspired by the natural forms and animal motifs associated with Sohrai painting. Replace this text with artist-verified information."},
    {"id":"JH-PAT-002","title":"Traditional Paitkar painting","form":"Paitkar","region":"East Singhbhum","artist":"Demo Artist 2","price":"₹1,800","description":"A sample listing for a traditional scroll-painting style. Confirm the artist, community, story and technique before publishing."},
    {"id":"JH-JAD-003","title":"Dokra-inspired craft","form":"Dokra metal craft","region":"Bastar-style example excluded; Jharkhand listing pending","artist":"Demo Artist 3","price":"₹3,200","description":"Demonstration entry only. Replace with a verified Jharkhand artisan and locally accurate cultural description."},
    {"id":"JH-WAR-004","title":"Wooden craft study","form":"Wood craft","region":"Khunti","artist":"Demo Artist 4","price":"₹950","description":"A placeholder gallery item. Add details only after receiving permission and accurate information from the maker."},
]
LANG = {
    "English": {
        "home":"Home", "explore":"Explore Art", "register":"Artist Registration",
        "gallery":"Artwork Gallery", "archive":"Heritage Stories", "qr":"Artwork QR",
        "welcome":"Discover the living art and stories of Jharkhand.",
        "intro":"A digital space to celebrate artists, explore traditional art forms and preserve the stories behind every creation.",
        "featured":"Featured artwork", "browse":"Explore the collection",
    },
    "हिन्दी": {
        "home":"मुखपृष्ठ", "explore":"कला देखें", "register":"कलाकार पंजीकरण",
        "gallery":"कलाकृति संग्रह", "archive":"विरासत की कहानियाँ", "qr":"कलाकृति QR",
        "welcome":"झारखंड की जीवंत कला और कहानियों को जानें।",
        "intro":"कलाकारों को सम्मान देने, पारंपरिक कला को जानने और हर रचना की कहानी सहेजने का डिजिटल मंच।",
        "featured":"विशेष कलाकृति", "browse":"संग्रह देखें",
    },
}

if "artists" not in st.session_state:
    st.session_state.artists = []
if "selected_art" not in st.session_state:
    st.session_state.selected_art = None

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("<div style='font-size:2.1rem;font-weight:800;letter-spacing:2px'>🌿 JHAROHAR</div>", unsafe_allow_html=True)
    st.caption("Preserving Roots, Celebrating Art")
    language = st.selectbox("Language / भाषा", ["English", "हिन्दी", "Regional language (coming soon)"])
    t = LANG.get(language, LANG["English"])
    st.markdown("---")
    page = st.radio("NAVIGATION", [
        t["home"], t["explore"], t["gallery"], t["register"], t["archive"], t["qr"]
    ])
    st.markdown("---")
    st.caption("A DICE innovation prototype")
    st.caption("Demo version • Jharkhand focus")

# ---------- Pages ----------
def artwork_card(item):
    st.markdown(f"""
    <div class="card">
      <span class="pill">{item['form']}</span>
      <h3>{item['title']}</h3>
      <div class="muted">📍 {item['region']} · 👩‍🎨 {item['artist']}</div>
      <p>{item['description']}</p>
      <b>{item['price']}</b>
    </div>
    """, unsafe_allow_html=True)

if page == t["home"]:
    st.markdown(f"""
    <div class="hero">
      <div class="eyebrow">Jharkhand's cultural heritage</div>
      <h1>JHAROHAR</h1>
      <p><b>Preserving Roots, Celebrating Art.</b></p>
      <p>{t['welcome']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.write(t["intro"])
    c1,c2,c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card'><h3>🎨 Explore art</h3><p class='muted'>Discover artwork and art forms from across Jharkhand.</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><h3>🧑‍🎨 Artist voices</h3><p class='muted'>Learn about the people and knowledge behind each creation.</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><h3>📖 Living heritage</h3><p class='muted'>Preserve stories, techniques and meanings with care.</p></div>", unsafe_allow_html=True)
    st.markdown("### " + t["featured"])
    cols = st.columns(2)
    for col, item in zip(cols, ARTWORKS[:2]):
        with col:
            artwork_card(item)
    st.info("Prototype note: the listings shown here are sample placeholders, not verified artist listings or cultural descriptions.")

elif page == t["explore"]:
    st.title("Explore Jharkhand's Art")
    st.write("Browse sample categories. We will add artist-verified entries as the project develops.")
    categories = sorted(set(x["form"] for x in ARTWORKS))
    chosen = st.selectbox("Choose an art category", ["All"] + categories)
    for item in ARTWORKS:
        if chosen == "All" or item["form"] == chosen:
            artwork_card(item)
            st.write("")

elif page == t["gallery"]:
    st.title("Artwork Gallery")
    query = st.text_input("Search by artwork, art form, artist or region")
    for item in ARTWORKS:
        haystack = " ".join([item["title"], item["form"], item["artist"], item["region"]]).lower()
        if query.lower() in haystack:
            artwork_card(item)
            st.write("")

elif page == t["register"]:
    st.title("Artist Registration")
    st.write("This prototype collects a local demo registration. A secure online submission system will be added in the next development stage.")
    with st.form("artist_registration", clear_on_submit=True):
        name = st.text_input("Artist's full name *")
        phone = st.text_input("Mobile number *")
        district = st.selectbox("District", ["Select district", "Bokaro", "Chatra", "Deoghar", "Dhanbad", "Dumka", "East Singhbhum", "Garhwa", "Giridih", "Godda", "Gumla", "Hazaribagh", "Jamtara", "Khunti", "Koderma", "Latehar", "Lohardaga", " पाकुड़", "Palamu", "Ramgarh", "Ranchi", "Sahibganj", "Seraikela-Kharsawan", "Simdega", "West Singhbhum"])
        art_form = st.text_input("Art form / craft")
        language_spoken = st.text_input("Preferred language")
        about = st.text_area("Tell us about your art and experience")
        consent = st.checkbox("I agree that the information may be used for this project demonstration.")
        submitted = st.form_submit_button("Submit registration")
    if submitted:
        if not name.strip() or not phone.strip() or district == "Select district" or not consent:
            st.error("Please complete the required fields and give consent.")
        else:
            st.session_state.artists.append({
                "name":name, "phone":phone, "district":district,
                "art_form":art_form, "language":language_spoken,
                "about":about, "submitted":datetime.now().strftime("%d %b %Y, %I:%M %p")
            })
            st.success("Demo registration received in this session.")
            st.warning("This is not yet a secure permanent database. Do not enter real personal details in this school prototype.")
    if st.session_state.artists:
        st.subheader("Registrations in this session")
        for a in st.session_state.artists:
            st.write(f"**{a['name']}** · {a['district']} · {a['art_form']}")

elif page == t["archive"]:
    st.title("Heritage Stories")
    st.write("This section will hold artist-approved stories about art forms, materials, techniques, symbols and community traditions.")
    st.warning("Cultural knowledge should be documented with the artist's/community's permission. Do not assume one meaning applies to every artwork.")
    st.markdown("### What each story can include")
    st.markdown("- Artist's name and preferred public profile\n- Village/region and art form\n- Materials and process, as described by the artist\n- Meaning and story shared by the artist\n- Cultural context and permissions for public display")
    st.markdown("### Regional language support")
    st.write("English and Hindi interface labels are included in this starter. Santhali, Mundari, Ho, Kurukh and other language content can be added with fluent-speaker review.")

elif page == t["qr"]:
    st.title("Artwork QR Code")
    st.write("Generate a QR code for a sample artwork. In the next stage, each code will open a dedicated online artwork page.")
    labels = {f"{x['id']} — {x['title']}":x for x in ARTWORKS}
    selected = st.selectbox("Choose an artwork", list(labels.keys()))
    item = labels[selected]
    qr_payload = f"JHAROHAR|{item['id']}|{item['title']}|{item['form']}|{item['region']}"
    qr_img = qrcode.make(qr_payload)
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    st.image(buffer.getvalue(), width=230, caption=f"QR code for {item['id']}")
    st.download_button("Download QR code (PNG)", data=buffer.getvalue(), file_name=f"{item['id']}.png", mime="image/png")
    st.code(qr_payload)
    st.info("For the live version, QR codes should link to permanent public artwork pages. This starter QR stores a demo identifier and details.")

st.markdown("---")
st.markdown("<div style='text-align:center;color:#65756a;font-size:.85rem'>🌿 JHAROHAR · Preserving Roots, Celebrating Art · DICE Prototype</div>", unsafe_allow_html=True)
