# ReliefX – Disaster Relief Prioritization Agent

ReliefX is an AI-driven system integrated with **IBM watsonx Orchestrate** to:
- Analyze disaster datasets (CSV/GeoJSON).
- Identify high-priority relief zones.
- Trigger alerts and notifications (Slack, Email, etc.).
- Provide a Streamlit dashboard for visualization.

## 📂 Project Structure
- `flask_webhook/` → Flask API for running ML inference.
- `streamlit_dashboard/` → User interface for uploading and visualizing results.
- `models/` → Trained ML models.
- `requirements.txt` → Python dependencies.

## 🚀 How to Run
1. Create a virtual environment and install requirements:
   ```bash
   pip install -r requirements.txt
