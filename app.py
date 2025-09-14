import streamlit as st
import requests

st.title("🌍 ReliefX Dashboard")
st.write("Upload data and run inference through the ReliefX API")

incident_id = st.text_input("Incident ID", "INC001")
numbers = st.text_area("Enter data values (comma-separated)", "20,50,80,100")

if st.button("Run Inference"):
    try:
        data = [float(x.strip()) for x in numbers.split(",")]
        payload = {"incident_id": incident_id, "data": data}
        resp = requests.post("http://127.0.0.1:8080/api/reliefx/infer", json=payload)

        if resp.status_code == 200:
            result = resp.json()
            st.success(f"Severity: {result['severity']:.2f}")
            st.json(result)
        else:
            st.error(f"Error: {resp.text}")
    except Exception as e:
        st.error(f"Failed to run inference: {e}")
