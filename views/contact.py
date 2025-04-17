import streamlit as st

def txt(svg, label, link):
  col1, col2 = st.columns([1, 5], gap="small")
  with col1:
    st.markdown(
      f"<div style='display: flex; align-items: center; justify-content: center; height: 50px;'>"
      f"<img src='{svg}' alt='{label}' style='width: 30px; height: 30px;'></div>",
      unsafe_allow_html=True
    )
  with col2:
    st.markdown(
      f"<div style='display: flex; align-items: center; height: 50px;'>"
      f"<a href='{link}' style='text-decoration: none; color: #0366d6;' target='_blank'>"
      f"<h4 style='margin: 0;'>{label}</h4></a></div>",
      unsafe_allow_html=True
    )

st.title("📞 My Contact")

txt('https://cdn-icons-png.flaticon.com/512/174/174857.png', 'LinkedIn', 'https://www.linkedin.com/in/yusuf-agriafan/')
txt('https://cdn-icons-png.flaticon.com/512/25/25231.png', 'GitHub', 'https://github.com/YusufAgriafan')
txt('https://cdn-icons-png.flaticon.com/512/732/732200.png', 'Email', 'mailto:yusuf.agriafan29@gmail.com')

st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)

st.markdown(
  "<div style='text-align: center; margin-top: 20px;'>"
  "<p>Feel free to connect with me on any platform!</p>"
  "<a href='https://www.linkedin.com/in/yusuf-agriafan/' target='_blank' "
  "style='background-color: #0366d6; color: white; padding: 10px 20px; text-decoration: none; "
  "border-radius: 5px;'>Connect Now</a>"
  "</div>",
  unsafe_allow_html=True
)