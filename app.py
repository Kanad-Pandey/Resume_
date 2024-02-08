from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume_new.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kanad Pandey"
PAGE_ICON = ":wave:"
NAME = "Kanad Pandey"
DESCRIPTION = """
Data Science Intern at Acuitas360
"""
EMAIL = "kanadpandey19946@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kanad-pandey-b1264a200/",
    "GitHub": "https://github.com/Kanad-Pandey",
}
PROJECTS = {
    "🏆 Heart Attack analysis and prediction - Prediction using Machine Learning": "https://github.com/Kanad-Pandey/Machine-Learning/blob/main/heart-attack-analysis-and-prediction.ipynb",
    "🏆 Twitter Sentiment Analysis - The project is aimed to categorize tweets as either positive or negative, providing valuable insights into public perception.": "https://github.com/Kanad-Pandey/Machine-Learning/blob/main/twitter%20sentiment%20analysis.ipynb",
    "🏆 Text Analysis Web Application - It delivers sentiment analysis, named entity recognition, and abuse detection from a text prompt.": "https://github.com/Kanad-Pandey/text_analysis_web_application",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    yes=st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",

    )
    if yes:
        st.snow()
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Expert in extracting actionable insights from complex datasets to drive informed decision-making and achieve strategic objectives.
- ✔️ Strong hands on experience and knowledge in Data Science domain
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Tensorflow, Keras), SQL, Front-end
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Seaborn
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Intern | Acuitas360**")
st.write("09/2023 - Present")
st.write(
    """
- ► Currently implementing key features, UI design, and data source integration for efficient account tracking and planning within the application in Powerapps
- ► Generated statistical reports, providing key insights for more than 20 marketing campaigns and initiatives, includ- ing A/B testing, customer retention, brand awareness, and global expansion.
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Teaching Assistant | Coding Ninjas**")
st.write("02/2022 - 04/2022")
st.write(
    """
- ► Helped students with data structures and algorithms in C++ through live call sessions, chat, and mentoring
- ► Addressed over 200 doubts and mentored 60+ students.
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
