import streamlit as st

col_photo, col_about = st.columns([1, 3], gap="medium")

def txt3(a, b):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

with col_photo:
    st.image("assets/foto1.png")

with col_about:
    st.title("Yusuf Agung Rizky Afandi")

    st.markdown("""
        > 🧑‍💻 A passionate Informatics Engineering student specializing in Data Science and Full Stack Development. 
            Turning technology into meaningful solutions for real-world impact.
    """)

    st.info("""
            Hello! I'm Yusuf Agung Rizky Afandi, an Informatics Engineering student in the Bachelor of Informatics Engineering program 
            at the State University of Malang. I'm deeply interested in data science and full stack web development. Actively involved in 
            tech communities, competitions, and projects, I'm continuously sharpening both my technical and leadership skills 
            through hands-on experiences and structured 
            training programs.
            """)

col_exp, col_skills = st.columns(2, gap="medium")

with col_exp:
    st.header("Experience ✈️")
    st.write("""
- **Fullstack Developer Intern – IT Division**  
  *PT Bintang Multi Teknologi Media, Malang* — *Jan 2025 – Present*  
    - Led the development of the JoySailing ticketing project using Laravel as a fullstack developer.  
    - Assisted in refactoring and redesigning legacy CodeIgniter 3 codebase using Bootstrap.  
    - Contributed to frontend development using Next.js, React, Tailwind CSS, and TypeScript for a psychology web project.  

---

- **Software Engineering Intern – Hospital Information Systems Division**  
  *Aminah Islamic Hospital Blitar, Blitar* — *Jun 2024 – Aug 2024*  
    - Developed a hospital queue management system using Laravel to handle patient registration and appointment scheduling.  
    - Created a hospital Android application using Flutter to improve patient service accessibility.  
    - Supported the setup and maintenance of the hospital’s network infrastructure, including cabling and network optimization.
    """)


with col_skills:
    st.header("Skills ⚙️")

    txt3('Programming Languages', '`Python`, `SQL`, `HTML`, `CSS`, `JavaScript`, `TypeScript`, `C#`, `PHP`, `Kotlin`, `Dart`')
    txt3('Frameworks & Tools', '`Laravel`, `Flutter`, `React`, `Next.js`, `Vue`, `CodeIgniter`, `RestAPI`, `Bootstrap`, `Tailwind`')
    txt3('Machine Learning & AI', '`TensorFlow`, `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `flask`')
    txt3('Cloud & DevOps', '`Google Cloud`, `Docker`')
    txt3('Public Speaking', '`Public Speaking`, `Presentation`, `Communication Skills`')
    txt3('Project Management', '`Task Management`, `Project Management`')
    txt3('Research & Problem Solving', '`Research Skills`, `Critical Thinking`, `Problem Solving`, `Scientific Writing`')
    txt3('Organizational', '`Organizational Leadership`, `Strategic Planning`, `Partnership Development`')
    txt3('IT & Electronics', '`Soft Skills`, `Hard Skills`, `IT`')


