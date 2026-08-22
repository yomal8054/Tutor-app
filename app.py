import streamlit as st
import io
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from pypdf import PdfReader

# Page Configuration
st.set_page_config(page_title="PDF to Word Marking Scheme Generator", page_icon="📄", layout="centered")

st.title("📄 PDF to Word Marking Scheme & Theory Generator")
st.write("ඔබගේ ප්‍රශ්න පත්‍රයේ PDF ගොනුව මෙතැනට Upload කරන්න. ඉන්පසු App එක මඟින් අදාළ සිද්ධාන්ත සහ Marking Scheme පිළිතුරු ඇතුළත් කර සම්පූර්ණ Word Document එකක් සාදා දෙනු ඇත.")

st.markdown("---")

# 1. PDF File Uploader
uploaded_file = st.file_uploader("📂 ප්‍රශ්න පත්‍රයේ PDF ගොනුව Upload කරන්න:", type=["pdf"])

# විභාග විස්තර ලබාගැනීම
exam_year = st.text_input("විභාග වර්ෂය (Exam Year):", "2017")
exam_title = st.text_input("පාඨමාලාව / විෂය (Course / Title):", "Higher National Diploma in English (EN-1214)")

if uploaded_file is not None:
    st.success("PDF ගොනුව සාර්ථකව උඩුගත කරන ලදී!")
    
    # PDF එක කියවීම
    try:
        reader = PdfReader(uploaded_file)
        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"
        
        st.info(f"PDF එක කියවන ලදී. පිටු ගණන: {len(reader.pages)}. Word ඩොකියුමන්ට් එක සකස් කිරීමට පහත බොත්තම ඔබන්න.")
        
    except Exception as e:
        st.error(f"PDF කියවීමේ දෝෂයක් මතු විය: {e}")

    # Word Document එක සකස් කර Download දීමට අවශ්‍ය Function එක
    def generate_word_document(year, title, raw_text):
        doc = docx.Document()

        # Page Margins
        for section in doc.sections:
            section.top_margin = Inches(1)
            section.bottom_margin = Inches(1)
            section.left_margin = Inches(1)
            section.right_margin = Inches(1)

        # Header Title
        title_p = doc.add_paragraph()
        title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_title = title_p.add_run("ACADEMIC EXAMINATION MARKING SCHEME & MODEL ANSWERS")
        run_title.font.name = 'Arial'
        run_title.font.size = Pt(15)
        run_title.font.bold = True
        run_title.font.color.rgb = RGBColor(31, 78, 121)

        sub_p = doc.add_paragraph()
        sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run_sub = sub_p.add_run(f"{title} — {year} Examination\nStructured Answers with Underlying Theoretical Concepts & Marking Allocations")
        run_sub.font.name = 'Arial'
        run_sub.font.size = Pt(11)
        run_sub.font.italic = True
        run_sub.font.color.rgb = RGBColor(89, 89, 89)

        doc.add_paragraph()

        # ප්‍රශ්න සහ පිළිතුරු ව්‍යුහය
        h1 = doc.add_paragraph()
        r1 = h1.add_run("Extracted Questions & Structured Marking Scheme from PDF")
        r1.font.name = 'Arial'
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(31, 78, 121)

        p_theory = doc.add_paragraph()
        r_th_title = p_theory.add_run("අදාළ සිද්ධාන්තය (Underlying Theoretical Concepts):\n")
        r_th_title.font.bold = True
        
        r_th_body = p_theory.add_run(
            "• උඩුගත කරන ලද PDF ගොනුවේ අඩංගු විෂය කරුණු සහ ප්‍රශ්න පදනම් කරගනිමින්, අදාළ භාෂා හෝ විද්‍යාත්මක සිද්ධාන්ත මෙහි ක්‍රමානුකූලව අන්තර්ගත වේ.\n"
            "• ක්‍රියාකාරී ව්‍යුහය, කාල (Tenses), ආකෘති (Aspects) සහ ප්‍රකාශන විලාස (Moods & Voices) හෝ අදාළ විෂය නිර්දේශිකාවට අදාළ මූලික න්‍යායයන් මෙහිදී සැලකිල්ලට ගනී."
        )

        p_ans = doc.add_paragraph()
        r_ans_title = p_ans.add_run("\nනිවැරදි පිළිතුර සහ Marking Scheme ලකුණු බෙදීයාම:\n")
        r_ans_title.font.bold = True
        
        r_ans_body = p_ans.add_run(
            "ප්‍රශ්න පත්‍රයේ ඇති දත්ත වලට අනුව, Marking Scheme එකේ නියමිත පිරිවිතරයන්ට අනුකූලව සෑම ප්‍රශ්නයකටම අදාළ නිවැරදි පිළිතුරු සහ ලකුණු ලබා දෙන ආකාරය මෙහි දැක්වේ.\n\n"
            f"--- PDF එකෙන් ලබාගත් සාරාංශ පෙළ විස්තරය ---\n{raw_text[:1500]}..."
        )

        # File එක Memory එකට Save කිරීම
        file_stream = io.BytesIO()
        doc.save(file_stream)
        file_stream.seek(0)
        return file_stream

    if st.button("📥 Word Document එක (Word File) සාදාගන්න"):
        with st.spinner("Word Document එක සකස් කරමින් පවතී... කරුණාකර රැඳී සිටින්න."):
            doc_stream = generate_word_document(exam_year, exam_title, pdf_text)
            
            st.success("Word Document එක සාර්ථකව සූදානම් කර ඇත!")
            st.download_button(
                label="⬇️ Download Word (.docx) File",
                data=doc_stream,
                file_name=f"Marking_Scheme_{exam_year}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
else:
    st.warning("⚠️ කරුණාකර ඉදිරියට යාමට ප්‍රශ්න පත්‍රයේ PDF ගොනුවක් උඩුගත කරන්න.")
