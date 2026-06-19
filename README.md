# 📄 JobPredictorAI - AI Powered Job Prediction System

An end-to-end Machine Learning application that predicts candidate suitability for a job role using candidate profile features.

The project combines:
- Data Analysis
- Machine Learning
- Feature Engineering
- Model Deployment
- Streamlit Web Application


## 🚀 Live Demo

🔗 Streamlit App:

https://jobpredictorai-debdut-nandy.streamlit.app/


---

# 📌 Project Overview

JobPredictorAI is an ML-based recruitment assistant that analyzes candidate information and predicts whether a candidate is likely to be shortlisted.

The system uses a trained Machine Learning classification model to evaluate:

- Experience
- Education
- Certifications
- Skills
- Projects
- Salary Expectation
- AI Resume Score
- Job Role


The goal is to assist recruiters in faster and data-driven candidate screening.


---

# ✨ Features

✅ Candidate profile based prediction

✅ AI-powered hiring recommendation

✅ Machine Learning classification model

✅ Fast real-time predictions

✅ Interactive Streamlit interface

✅ Confidence score generation

✅ Clean and user-friendly UI


---

# 🛠️ Tech Stack

## Programming Language

- Python


## Data Processing

- Pandas
- NumPy


## Machine Learning

- Scikit-learn
- Random Forest Classifier


## Visualization

- Matplotlib
- Seaborn
- Power BI


## Deployment

- Streamlit Cloud


---

# 📂 Project Structure


```

JobPredictorAI
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── models
│   │
│   ├── resume_screening_model.pkl
│   └── columns.pkl
│
├── notebook
│   │
│   └── Resume_Screening_Model.ipynb
│
└── dashboard
└── image


````


---

# 📊 Dataset Features


| Feature | Description |
|-|-|
| Experience | Candidate work experience |
| Education | Highest qualification |
| Skills | Technical skill information |
| Certifications | Professional certifications |
| Job Role | Target position |
| Salary Expectation | Expected salary |
| Projects Count | Completed projects |
| AI Score | Resume ranking score |
| Recruiter Decision | Target variable |


---
# Dashboard Image

<img src="image/Screenshot 2026-06-18 191028.png" width="700">

---

# 🔍 Machine Learning Workflow


## 1. Data Cleaning

Performed:

- Missing value handling
- Duplicate removal
- Feature selection
- Data consistency checks


---

## 2. Exploratory Data Analysis

Analyzed:

- Hiring distribution
- Experience impact
- AI Score relationship
- Education influence
- Salary patterns
- Skill trends


---

## 3. Feature Engineering

Applied:

- Label Encoding
- One Hot Encoding
- Feature transformation


---

## 4. Model Training


Algorithm Used:

### Random Forest Classifier


Why Random Forest?

- Handles categorical and numerical data
- Provides feature importance
- Good generalization
- Suitable for recruitment prediction


---

# 📈 Model Performance


Model:

Random Forest Classifier


Accuracy:

~95%


Evaluation Metrics:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix


---

# 🖥️ Streamlit Application


The deployed application allows users to enter candidate details:


Input:

- Experience
- Education
- Certifications
- Job Role
- Skills
- Projects
- Salary Expectation
- AI Score


Output:

- Hiring Prediction
- Prediction Confidence


---

# 📷 Application Preview
<img src="image/Screenshot 2026-06-19 095753.png" width="700">


---

# ▶️ Run Locally


Clone repository:

```bash
git clone https://github.com/Deb124-source/JobPredictorAI.git
````

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

* Resume PDF parser
* NLP based resume matching
* Job description similarity scoring
* Transformer based embeddings
* Candidate ranking system
* ATS compatibility score

---

# 👨‍💻 Author

**Debdut Nandy**

---

⭐ If you found this project useful, consider giving it a star!

```

This README structure is similar to strong ML deployment repositories where they clearly separate **dataset → preprocessing → model → deployment → usage**. :contentReference[oaicite:1]{index=1}
```
