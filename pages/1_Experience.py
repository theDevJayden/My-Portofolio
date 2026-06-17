import streamlit as st

st.set_page_config(page_title="Experience", page_icon="💼")
st.title("Work Experience")

col1, col2 = st.columns([1, 2])

with col1:
    try:
        st.image("assets/viodi.jpeg", width="stretch")
    except Exception as e:
        st.info("💡 Picture failed to load")

with col2:
    st.markdown("### Accounting Assistant (Internship)")
    st.markdown("#### **Viodi Cosmetics**")
    st.caption("Timeline: 2024 - 2025 • Duration: 4 Months")
    
    st.write("")
    
    st.markdown(
        """
    Managed financial transactions and compliance operations for corporate accounts. 

    **Key Responsibilities & Contributions:**
    * **Financial Documentation:** Streamlined corporate transactional records by accurately creating and organizing invoices.
    * **Taxation Compliance:** Supported the finance team in calculating and verifying monthly company taxation data.
    """
    )

st.write("---")
st.title("Campus Experience")

col3, col4 = st.columns([1, 2])

with col3:
    images = ["assets/FL.jpg", "assets/FL2.jpg", "assets/FL3.jpg"]  

    if "image_index" not in st.session_state:
        st.session_state.image_index = 0

    try:
        st.image(images[st.session_state.image_index], use_container_width=True)
    except Exception as e:
        st.info("💡 Picture failed to load")


    nav_col1, nav_col2 = st.columns([1, 1])

    with nav_col1:
        if st.button("⬅️ Prev", use_container_width=True):
            if st.session_state.image_index > 0:
                st.session_state.image_index -= 1
                st.rerun()

    with nav_col2:
        if st.button("Next ➡️", use_container_width=True):
            if st.session_state.image_index < len(images) - 1:
                st.session_state.image_index += 1
                st.rerun()

with col4:
    st.markdown("### Freshmen Leader")
    st.markdown("#### **Bina Nusantara University**")
    st.caption("Timeline: 2025 • Duration: 1 month")
    
    st.write("") 
    
    st.markdown(
        """
    Guide and lead new students during their orientation program.

    **Key Responsibilities & Contributions:**
    * Teach new students about Bina Nusantara rules, guidelines, and policy. 
    * Consult and guide new students personally, learning their troubles and adaptation problems, while finding a solution. 
    """
    ) 


st.write("---")
st.title("Organizational Experience")

col5, col6 = st.columns([1, 2])

with col5:
    try:
        st.image("assets/JK.jpeg", width="stretch")
    except Exception as e:
        st.info("💡 Picture failed to load")

with col6:
    st.markdown("### Toddler Ministry Co-Leader")
    st.markdown("#### **Joel Kids Ministry**")
    st.caption("Timeline: 2025 - Present")

    st.write("")

    st.markdown(
        """
        Directing weekly operations to facilitate impactful ministry programs.

        **Key Responsibilities & Contributions:**
        * Involved in planning rundowns, special services, and curricular materials for the toddler ministry.
        * Directing weekly operations to facilitate impactful ministry programs
        """
    )