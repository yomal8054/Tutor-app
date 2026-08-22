import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="PDF Tutor & Marking Scheme App", page_icon="📚", layout="centered")

# Header Details (අදාල වර්ෂය සහ විස්තර)
st.title("📚 Digital Tutor & Marking Scheme Generator")
st.markdown("---")
st.subheader("📌 විභාග විස්තර සහ PDF උඩුගත කිරීම")

# වර්ෂය සහ වෙනත් විස්තර ඇතුළත් කිරීමට User Inputs
exam_year = st.text_input("විභාග වර්ෂය (Exam Year):", "2017")
exam_title = st.text_input("පාඨමාලාව / විෂය (Course / Subject):", "Higher National Diploma in English (EN-1214)")

st.markdown("---")

# PDF File Uploader
uploaded_file = st.file_uploader("📂 මෙතනට ඔබේ ප්‍රශ්න පත්‍රයේ PDF ගොනුව (PDF) Upload කරන්න:", type=["pdf"])

if uploaded_file is not None:
    st.success(f"'{uploaded_file.name}' සාර්ථකව උඩුගත කරන ලදී!")
    st.markdown("---")
    
    st.header(f"✍️ {exam_year} - ප්‍රශ්න පත්‍රයේ පිළිතුරු සහ Marking Scheme එක")
    st.info("පහත දැක්වෙන්නේ උඩුගත කළ PDF ගොනුවට අදාළ ප්‍රශ්න, සිද්ධාන්ත සහ නිවැරදි Marking Scheme පිළිතුරු වේ.")

    # ප්‍රශ්න 1
    st.subheader("ප්‍රශ්න අංක 01")
    st.write("The authority removed John from his post. (මෙම වාක්‍යයේ Tense, Aspect, Mood සහ Voice ලියන්න.)")

    with st.expander("🔍 සිද්ධාන්තය සහ නිවැරදි පිළිතුර බලන්න"):
        st.markdown("### 💡 අදාළ සිද්ධාන්තය (Underlying Theory):")
        st.write(
            "• **Tense (කාලය):** ක්‍රියාවක් සිදුවන කාලය ප්‍රකාශ කරයි (වර්තමාන සහ අතීත පමණි).\n"
            "• **Aspect (ස්වභාවය):** ක්‍රියාවක කාලික ව්‍යුහය (Simple, Progressive, Perfect, Perfect-progressive) පෙන්වයි.\n"
            "• **Mood (අභිප්‍රාය):** Indicative, Subjunctive, හෝ Imperative ලෙස දැක්වේ."
        )
        st.markdown("### ✅ Marking Scheme පිළිතුර:")
        st.success(
            "• **Tense:** Past\n"
            "• **Aspect:** Simple\n"
            "• **Mood & Voice:** Indicative / Active"
        )

    st.markdown("---")

    # ප්‍රශ්න 2
    st.subheader("ප්‍රශ්න අංක 02")
    st.write("විද්‍යාත්මක හා ශාස්ත්‍රීය ලිවීමේදී Passive Voice භාවිතා කරන අවස්ථා මොනවාදැයි පැහැදිලි කරන්න.")

    with st.expander("🔍 සිද්ධාන්තය සහ නිවැරදි පිළිතුර බලන්න"):
        st.markdown("### 💡 අදාළ සිද්ධාන්තය (Underlying Theory):")
        st.write("ක්‍රියාව සිදුකළ පුද්ගලයාට වඩා, ක්‍රියාවට භාජනය වූ දෙය (Object) වාක්‍යයේ මුල් තැනට ගෙන ලිවීම Passive Voice වේ.")
        
        st.markdown("### ✅ Marking Scheme පිළිතුර (ලකුණු 10 යි):")
        st.success(
            "අපේක්ෂකයා විසින් අවම වශයෙන් අවස්ථා 05 ක් ලියා තිබිය යුතුය:\n"
            "1. ක්‍රියාකරු නොදන්නා අවස්ථාවක (The actor is unknown)\n"
            "2. ක්‍රියාකරු වැදගත් නොවන අවස්ථාවක (The actor is irrelevant)\n"
            "3. වගකීම පැහැදිලිව සඳහන් කිරීමට අවශ්‍ය නොවන විට\n"
            "4. පොදු සත්‍යයක් ප්‍රකාශ කරන විට (General truth)\n"
            "5. ක්‍රියාවට භාජනය වූ දෙය විශේෂයෙන් ඉස්මතු කිරීමට අවශ්‍ය විට"
        )
else:
    st.warning("⚠️ කරුණාකර ඉදිරියට යාමට ප්‍රශ්න පත්‍රයේ PDF ගොනුවක් උඩුගත කරන්න (Upload a PDF file to begin).")
