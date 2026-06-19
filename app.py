import streamlit as st
import pickle
import numpy as np
import pandas as pd


# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="JobPredictor AI",
    page_icon="📄",
    layout="wide"
)



# ----------------------------
# Custom CSS
# ----------------------------

st.markdown(
"""
<style>

.main{
    background-color:#f8f9fa;
}


.title{
    font-size:42px;
    font-weight:700;
    color:#1f4e79;
}


.card{

    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0px 4px 15px rgba(0,0,0,0.1);

}


.result{

    font-size:28px;
    font-weight:bold;

}


</style>

""",
unsafe_allow_html=True
)



# ----------------------------
# Load Model
# ----------------------------

@st.cache_resource
def load_model():


    model = pickle.load(
        open(
            "models/resume_screening_model.pkl",
            "rb"
        )
    )


    columns = pickle.load(
        open(
            "models/columns.pkl",
            "rb"
        )
    )


    return model, columns



model, columns = load_model()



# ----------------------------
# Header
# ----------------------------

st.markdown(
"<div class='title'>📄JobPredictor AI</div>",
unsafe_allow_html=True
)


st.write(
"""
An ML-powered recruitment assistant that predicts whether a candidate
is likely to be shortlisted based on resume features.
"""
)


st.divider()



# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.header(
"Candidate Information"
)



experience = st.sidebar.slider(
"Experience (Years)",
0,
20,
3
)



education = st.sidebar.selectbox(

"Education",

[
"Bachelor",
"Master",
"PhD"
]

)



certifications = st.sidebar.selectbox(

"Certifications",

[
"Yes",
"No"
]

)



job_role = st.sidebar.selectbox(

"Job Role",

[
"Data Scientist",
"Data Analyst",
"Software Engineer",
"ML Engineer",
"Web Developer"
]

)



salary = st.sidebar.number_input(

"Expected Salary ($)",

min_value=10000,

max_value=200000,

value=50000

)



projects = st.sidebar.slider(

"Number of Projects",

0,

20,

3

)



ai_score = st.sidebar.slider(

"AI Resume Score",

0,

100,

70

)



skills = st.sidebar.multiselect(

"Skills",

[
"Python",
"SQL",
"Machine Learning",
"Power BI",
"Excel",
"Java",
"Cloud"
]

)



# ----------------------------
# Prediction
# ----------------------------

if st.button(
"🔍 Screen Resume",
use_container_width=True
):


    input_data = pd.DataFrame(
        np.zeros(
            (1,len(columns))
        ),
        columns=columns
    )



    # numerical values


    if "Experience (Years)" in columns:
        input_data["Experience (Years)"] = experience


    if "Salary Expectation ($)" in columns:
        input_data["Salary Expectation ($)"] = salary


    if "Projects Count" in columns:
        input_data["Projects Count"] = projects


    if "AI Score (0-100)" in columns:
        input_data["AI Score (0-100)"] = ai_score



    # categorical encoding


    values = [

        education,
        certifications,
        job_role

    ]


    for value in values:

        col = value

        if col in input_data.columns:

            input_data[col]=1



    for skill in skills:

        skill_col = "Skills_"+skill

        if skill_col in input_data.columns:

            input_data[skill_col]=1



    prediction = model.predict(
        input_data
    )[0]


    probability = model.predict_proba(
        input_data
    )[0][1]



    st.divider()



    col1,col2 = st.columns(2)



    with col1:


        if prediction==0:

            st.success(
            "✅ Candidate Recommended"
            )

        else:

            st.error(
            "❌ Candidate Not Recommended"
            )



    with col2:


        st.metric(

        "Screening Confidence",

        f"{round(probability*100,2)} %"

        )



st.divider()



# ----------------------------
# About Section
# ----------------------------


st.subheader(
"⚙️ Model Information"
)


c1,c2,c3 = st.columns(3)



c1.info(
"""
Algorithm

Random Forest Classifier
"""
)


c2.info(
"""
Accuracy

~95%
"""
)


c3.info(
"""
Task

Binary Classification
"""
)



st.caption(
"Built using Machine Learning + Streamlit"
)
