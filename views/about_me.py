import streamlit as st
from PIL import Image

# with open("assets/style.css") as f:
#     st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

#####################
st.markdown('''
## Education 🎓
''')

txt('**Bachelor of Informatics Engineering**, *State University of Malang*, Malang',
'Aug 2022 – Present')
st.markdown('''
- GPA: `3.84` out of `4.00`
''')

txt('**Bangkit Academy 2024**, Indonesia',
'Sep – Dec 2024')
st.markdown('''
- Machine Learning Cohort
- Participated in a multidisciplinary learning program organized by Google, GoTo, and Traveloka, with a primary focus on developing Machine Learning competencies.
- Completed various renowned courses from DeepLearning.AI and Dicoding Indonesia, including "Supervised Machine Learning," "Advanced Learning Algorithms," and "Natural Language Processing," along with other courses on data analysis and AI model development.
- Developed an innovative capstone project involving a machine learning model for text summarization and an interactive chatbot, utilizing fine-tuning transfer learning techniques, successfully deployed on Google Cloud using Flask and Docker.
- Enhanced soft skills such as professional communication, time management, and problem-solving to support career readiness in the technology industry.
''')

#####################
st.markdown('''
## Achievements 🏆
''')

txt('**- Silver Medalist**, *Indonesia Inventors Day 2024*', 'Aug 2024')
st.markdown('''
Issued by the Indonesian Invention and Innovation Promotion Association (INNOPA). Awarded for the invention "PESI: Personalized Website for the Prevention and Management of Depression".
''')

txt('**- First Place**, *HACKATHON SDGs UM 2024*', 'Jun 2024')
st.markdown('''
Issued by State University of Malang. Recognized for the project: "Digital Innovation in Prevention and Handling of Depression through the CESI Website".
''')

txt('**- First Place**, *Festival Mahasiswa Elektro dan Informatika*', 'Mar 2024')
st.markdown('''
Issued by State University of Malang. Digital Innovation in Education (Digital Learning Innovation Subcategory).
''')

txt('**- Second Place**, *Festival Mahasiswa Elektro dan Informatika*', 'Mar 2024')
st.markdown('''
Issued by State University of Malang. Satria Data Competition (Statistical Essay Subcategory).
''')

txt('**- Second Place**, *Festival Mahasiswa Elektro dan Informatika*', 'Mar 2023')
st.markdown('''
Issued by State University of Malang. Scientific Writing Competition.
''')

st.subheader("My Tools 🛠️")
txt2('Development Tools', '`Visual Studio Code`, `Android Studio`, `SQLyog`, `Laragon`, `Composer`')
txt2('Containerization & Deployment', '`Docker`')
txt2('Other Tools', '`Postman`, `Git`, `Figma`, `Notion`')