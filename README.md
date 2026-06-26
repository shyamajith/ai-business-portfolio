# AI Business Intelligence & Strategy Portfolio

A sophisticated Streamlit-based decision-support system bridging artificial intelligence with global market dynamics. This portfolio demonstrates data science and machine learning applications for solving complex international business challenges.

## 📋 Modules

### 1. **Due Diligence Studio** (Module 1)
Automated preliminary evaluation of companies, suppliers, and M&A opportunities using NLP heuristics.
- Strategic positioning & business model viability assessment
- Operational & jurisdictional risk evaluation
- Technological readiness & ESG compliance analysis

### 2. **UK Economic Inactivity Forecast** (Module 2)
Dynamic time-series projection modeling the Return on Investment (ROI) of workforce rehabilitation initiatives.
- Macroeconomic variable stress-testing
- 5-year algorithmic forecasting
- Gross GDP impact vs. intervention cost analysis

### 3. **ESG Traceability Ledger** (Module 3)
Enterprise pipeline utilizing Unsupervised Machine Learning (Isolation Forest) to detect supply chain data anomalies and greenwashing.
- Batch data ingestion and validation
- Anomaly detection on ESG metrics
- Supply chain transparency metrics

## 🚀 Deployment

### Local Development
```bash
# Clone the repository
git clone https://github.com/shyamajith/ai-business-portfolio.git
cd ai-business-portfolio

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run 1_Home.py
```

### Streamlit Cloud Deployment
1. Push this repository to GitHub
2. Go to [streamlit.io](https://streamlit.io)
3. Create new app and select this repository
4. Set main file path to `1_Home.py`
5. Deploy!

## 📦 Dependencies

- **streamlit**: Web framework for rapid data app development
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **plotly**: Interactive visualizations
- **scikit-learn**: Machine learning library (Isolation Forest for anomaly detection)

See `requirements.txt` for specific versions.

## 👨‍💼 Architect Profile

**Syamjith A A**  
*B.Tech Artificial Intelligence & Data Science*

**Core Competencies:**
- Corporate Strategy & Risk
- Supply Chain Analytics
- Embedded Finance Infrastructure

## 📝 Project Structure

```
ai-business-portfolio/
├── 1_Home.py                    # Landing page & navigation hub
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── .gitignore                   # Git ignore rules
└── pages/
    ├── 2_Due_Diligence.py      # M&A due diligence module
    ├── 3_Economic_Inactivity.py # UK macro forecasting module
    └── 4_ESG_Ledger.py         # ESG traceability & anomaly detection
```

## 📄 License

This project is part of a professional portfolio. All rights reserved.

## 🔗 Links

- **GitHub Repository**: https://github.com/shyamajith/ai-business-portfolio
- **Live Demo**: Visit the Streamlit Cloud deployment (when deployed)
