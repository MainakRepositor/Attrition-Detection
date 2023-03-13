"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Detection Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Trees and Artificial Neural Networks</b> for the Company Attrition Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    
    V1 = st.slider("Age", int(df["Age"].min()), int(df["Age"].max()))
    with st.expander("View Classes for Business Travel Types"):
        st.write('''0: Rarely Travelling; 1 : Frequently Travelling; 2: Non Travelling''')
    V2 = st.slider("Business Travel", int(df["BusinessTravel"].min()), int(df["BusinessTravel"].max()))
    V3 = st.slider("Daily Rate", int(df["DailyRate"].min()), int(df["DailyRate"].max()))
    with st.expander("View Classes for Department Types"):
        st.write('''1: Research and Development; 2 : Sales; 3: Human Resource''')
    V4 = st.slider("Department", int(df["Department"].min()), int(df["Department"].max()))
    V5 = st.slider("Distance From Home", int(df["DistanceFromHome"].min()), int(df["DistanceFromHome"].max()))
    V6 = st.slider("Education", int(df["Education"].min()), int(df["Education"].max()))
    with st.expander("View Classes for Education Fields"):
        st.write('''1: Life Sciences; 2 : Medical; 3: Human Resources; 4: Marketing; 5: Technical Degree; 6: Others''')
    V7 = st.slider("Education Field", int(df["EducationField"].min()), int(df["EducationField"].max()))
    V8 = st.slider("Years With Current Manager", int(df["YearsWithCurrManager"].min()), int(df["YearsWithCurrManager"].max()))
   
    V9 = st.slider("Environment Satisfaction", int(df["EnvironmentSatisfaction"].min()), int(df["EnvironmentSatisfaction"].max()))
    V10 = st.slider("Gender", int(df["Gender"].min()), int(df["Gender"].max()))
    V11 = st.slider("Hourly Rate", int(df["HourlyRate"].min()), int(df["HourlyRate"].max()))
    V12 = st.slider("Job Involvement", int(df["JobInvolvement"].min()), int(df["JobInvolvement"].max()))
    V13 = st.slider("Job Level", int(df["JobLevel"].min()), int(df["JobLevel"].max()))
    V14 = st.slider("Years In Current Role", int(df["YearsInCurrentRole"].min()), int(df["YearsInCurrentRole"].max()))

    with st.expander("View Classes for Job Role Types"):
        st.write('''1: Sales Executive; 2 : Lab Technician; 3: Research Scientist; 4:Manufacturing Director; 5: Healthcare Representative; 6: Manager; 7: Sales Representative; 8: Research Director''')
    V15 = st.slider("Job Role", int(df["JobRole"].min()), int(df["JobRole"].max()))
    V16 = st.slider("Years Since Last Promotion", int(df["YearsSinceLastPromotion"].min()), int(df["YearsSinceLastPromotion"].max()))
    V17 = st.slider("Job Satisfaction", int(df["JobSatisfaction"].min()), int(df["JobSatisfaction"].max()))
    with st.expander("View Classes for Marital Status Types"):
        st.write('''1: Single; 2 : Married; 3: Divorced''')
    V18 = st.slider("Marital Status", int(df["MaritalStatus"].min()), int(df["MaritalStatus"].max()))
    V19 = st.slider("Monthly Income", int(df["MonthlyIncome"].min()), int(df["MonthlyIncome"].max()))
    V20 = st.slider("Monthly Rate", int(df["MonthlyRate"].min()), int(df["MonthlyRate"].max()))
    V21 = st.slider("Number of Companies Worked In", int(df["NumCompaniesWorked"].min()), int(df["NumCompaniesWorked"].max()))
    V22 = st.slider("Years At Company", int(df["YearsAtCompany"].min()), int(df["YearsAtCompany"].max()))


    V23 = st.slider("Over Time", int(df["OverTime"].min()), int(df["OverTime"].max()))
    V24 = st.slider("Percent Salary Hike", int(df["PercentSalaryHike"].min()), int(df["PercentSalaryHike"].max()))
    V25 = st.slider("Performance Rating", int(df["PerformanceRating"].min()), int(df["PerformanceRating"].max()))
    V26 = st.slider("Relationship Satisfaction", int(df["RelationshipSatisfaction"].min()), int(df["RelationshipSatisfaction"].max()))
    V27 = st.slider("Total Working Years", int(df["TotalWorkingYears"].min()), int(df["TotalWorkingYears"].max()))
    V28 = st.slider("Training Times LastYear", int(df["TrainingTimesLastYear"].min()), int(df["TrainingTimesLastYear"].max()))
    V29 = st.slider("Work Life Balance", int(df["WorkLifeBalance"].min()), int(df["WorkLifeBalance"].max()))
    V30 = st.slider("Number of Employees", int(df["EmployeeNumber"].min()),int(df["EmployeeNumber"].max()))
    



        
        
    
    
    # Create a list to store all the features
    features = [V1,V2,V3,V4,V5,V6,V8,V9,V7,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,V29,V30]

    # Create a button to predict
    if st.button("Detect"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.1
        st.info("Detected Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.error("The Company has high risk of Attrition")
        else:
            st.success("The Company is presently less prone to Attrition")

        # Print teh score of the model 
        st.write("The model used is trusted by analysts and has an accuracy of ", round((score*100)),"%")
