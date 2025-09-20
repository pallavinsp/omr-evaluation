# Automated OMR Evaluation System

## Setup
```bash
git clone <your_repo_url>
cd automated-omr-evaluation
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

## Train CNN
```bash
python omr_engine/train_cnn.py
```

## Run Backend
```bash
uvicorn backend.app:app --reload
```

## Run Frontend
```bash
streamlit run frontend/streamlit_app.py
```

Upload an OMR sheet image → get evaluated scores instantly ✅
