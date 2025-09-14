# ReliefX – Disaster Relief Prioritization Agent

**ReliefX** is an AI-driven system integrated with **IBM watsonx Orchestrate** to identify high-priority disaster relief zones and visualize them via a Streamlit dashboard. It can also trigger alerts (Slack, Email, etc.) based on critical areas.

## 📂 Project Files
- `app.py` → Flask API for ML inference  
- `dashboard.py` → Streamlit interface for visualization  
- `model.pkl` → Trained ML model  
- `requirements.txt` → Python dependencies  

## 🚀 Run Locally
```bash
# Clone repo
git clone <your-repo-url>
cd <repo-directory>

# Create & activate virtual environment
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run API
python app.py

# Run Streamlit dashboard
streamlit run dashboard.py
