import streamlit as st

st.set_page_config(page_title="Jayden's Portofolio", page_icon="👋", layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("assets/profile.jpeg", width="stretch")
    except Exception as e:
        st.info("💡 Picture failed to load")

with col2:
    st.title("About Me")

    st.write(
        "Hello, I'm Jayden Samuel Kurniawan, a Computer Science undergraduate from Bina Nusantara University. "
        "What drives me is the ability to work in teams to bridge physical hardware, cloud software, and "
        "interactive interfaces to solve problems like data reliability in Indonesia."
    )

    st.write("---") 


    st.subheader("My Specializations")

    st.markdown(
        """
    * **Machine Learning:** Analyzing complex datasets and building predictive models using tools like Google Colab.
    * **IoT & Systems Architecture:** Connecting microcontrollers, sensors, and cloud systems to user-facing dashboards using Arduino IDE.
    * **Software & Design:** Building mobile and web solutions with Android Studio, integrated with interactive prototypes in Figma.
    """
    )

    st.write("---")

    st.subheader("Toolkits & Workflow")
    st.write(
        "I actively leverage advanced AI tools like Gemini to accelerate my documentation, optimize my workflows, "
        "and enhance the engineering process behind my project building."
    ) 

st.write("---")
st.title("My Socials")
st.markdown(
    """
* **LinkedIn:** [Jayden Samuel Kurniawan](https://www.linkedin.com/in/jayden-samuel-kurniawan-a525b3323?utm_source=share_via&utm_content=profile&utm_medium=member_android).
* **GitHub:** [theDevJayden](https://github.com/theDevJayden).
"""
)