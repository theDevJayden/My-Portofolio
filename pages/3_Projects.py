import streamlit as st

st.set_page_config(page_title="Projects", page_icon="📂")
st.title("PneuScan AI Portal")

st.markdown("### Intelligent Pneumonia Diagnostic System")
st.markdown("#### **Deep Learning & Unsupervised Clustering Pipeline**")
st.caption("Timeline: 2026 • Core Tech: Python, TensorFlow, Scikit-Learn")

st.write("")

st.markdown(
    """
    Developed an advanced medical imaging pipeline designed to automate the screening and deeper categorical analysis of pneumonia from digital chest X-rays.

    **Key Architecture & Contributions:**
    * **Supervised Feature Extraction:** Leveraged a fine-tuned **MobileNetV2** Convolutional Neural Network (CNN) framework under a supervised learning paradigm to accurately execute binary classification (Normal vs. Pneumonia).
    * **Unsupervised Subtype Segmentation:** Integrated **K-Means Clustering** on extracted deep-feature representations to classify and group latent structural variations within positive cases, aiding in the differentiation of pneumonia types.
    * **Optimized for Deployment:** Selected MobileNetV2 specifically for its highly efficient, lightweight architecture, ensuring the model remains computationally viable for real-world clinical edge-devices or lightweight web applications.
    
    **Links:**
    * GitHub : https://github.com/theDevJayden/AI-pneumonia-detector
    * Website : https://ai-pneumonia-detector-thedevjayden.streamlit.app/

    """
)

st.write("---")
st.title("Live Air Quality AI based Dashboard")

st.markdown("### Real-time Environmental Intelligence & AQI Monitoring")
st.markdown("#### **Hybrid IoT Architecture & ML-Driven Anomaly Detection**")
st.caption("Tech Stack: Arduino Mega, ESP32, ThingSpeak, Scikit-Learn")

st.write("")

st.markdown(
    """
    Developed an end-to-end environmental monitoring system designed to provide high-granularity Air Quality Index (AQI) data through a robust edge-to-cloud pipeline.

    **Key Architecture & Contributions:**
    * **Hybrid Hardware Integration:** Engineered a dual-microcontroller system utilizing an **Arduino Mega** for high-pin-count sensor polling and an **ESP32** as a dedicated wireless gateway for cloud transmission.
    * **Multi-Modal Sensing:** Integrated an array of **MQ-series gas sensors** and high-precision **PM2.5 optical sensors** to monitor a wide spectrum of atmospheric pollutants, including CO2, smoke, and fine particulate matter.
    * **Cloud Orchestration:** Streamlined data persistence via the **ThingSpeak API**, enabling live telemetry storage and real-time retrieval for remote web-based visualization.
    * **Intelligent Anomaly Detection:** Implemented an **Isolation Forest** machine learning model to automatically identify and flag environmental irregularities or sensor drift within the live data stream, ensuring higher data integrity.

    **Links:**
    * GitHub : https://github.com/theDevJayden/kualitas-udara-dashboard
    * Website : https://kualitas-udara-dashboard-eudtahka6ajlqffz3t5adm.streamlit.app/ 
    """
)