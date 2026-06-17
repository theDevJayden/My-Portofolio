import streamlit as st

st.set_page_config(page_title="Certificates", page_icon="📜")

st.title("ICOBAR")
col1, col2 = st.columns([1, 2])
with col1:
    try:
        st.image("assets/ICOBAR.jpeg", width="stretch")
    except Exception as e:
        st.info("💡 Picture failed to load")

with col2:
    st.markdown("### Smart Motorcycle Tire Monitoring System")
    st.markdown("#### **Research & Hardware Prototype**")
    st.caption("Status: Accepted in ICOBAR Conference (2025)")

    st.write("")

    st.markdown(
        """
        Designed and engineered a non-invasive IoT prototype aimed at enhancing road safety and sustainable urban mobility by monitoring motorcycle tire deflation in real time.

        **Key Architecture & Contributions:**
        * **Non-Invasive Hardware Design:** Integrated an ESP32 microcontroller with high-precision ultrasonic sensors to track tire-to-ground clearance anomalies, allowing installation without modifying existing vehicle components.
        * **Real-Time Telemetry & Alerting:** Programmed a live buzzer module for immediate operator warnings alongside an automated Telegram Bot API integration for remote, instant puncture notifications.
        * **Academic Publication:** Synthesized methodology and technical benchmarks into a peer-reviewed paper accepted for presentation at the ICOBAR 2025 conference.
        """
    )