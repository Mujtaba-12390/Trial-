import streamlit as st
from datetime import time
import pytz
import sqlite3
from datetime import datetime



# Set page configuration to wide mode
st.set_page_config(layout="wide")

# Add the logo to the sidebar
st.sidebar.image(
    "https://static.wixstatic.com/media/6c10b1_8f6d01566b5f4b40bd33fcb9a2b16585~mv2.png/v1/crop/x_0,y_37,w_640,h_161/fill/w_223,h_49,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/image002.png",
    use_column_width=True
)

# Set up the sidebar for navigation
st.sidebar.title("Candidate Information Form")
page = st.sidebar.selectbox("Select Page", ["1st Interview", "2nd Interview", "Hiring Details", "Employee Details"])



# Database connection
db_path = 'Data_Sample_old.db'


conn = sqlite3.connect(db_path)
c = conn.cursor()

# 1st Interview Form
if page == "1st Interview":
    st.header("1st Interview")

    with st.form(key='first_interview_form'):
        full_name = st.text_input("Full Name", placeholder="Muhammad Kamran Waseem")
        # Create columns for better layout
        col1, col2 = st.columns([1, 1])

        with col1:
            # Column 1: Personal Information and Work Details
            contact1 = st.text_input("Contact #1", placeholder= "03151234567")
            email1 = st.text_input("Email #1", placeholder="kamran.muhammad@yahoo.com")
            country = st.selectbox("Country", ["Pakistan", "India", "United States", "Canada"], key="country")
            city = st.text_input("City", placeholder="Karachi")
            calling_date = st.date_input("Calling Date")
            source =st.selectbox("Source", ["Indeed", "LinkedIn", "Monster", "Dice", "Taldel", "traxccel"], key="source_1")
            expected_salary = st.number_input("Expected Salary", min_value=0)
            notice_period = st.text_input("Notice Period", placeholder="Immediately")
            current_employment_status = st.selectbox("Current Employment Status", ["Fresh", "Employed", "Unemployed"], key="current_employment_status")
            work_arrangement = st.selectbox("Work Arrangement", ["On-site", "Remote", "Hybrid"], key="work_arrangement_1")
            skills = ['Python', 'Power BI', 'Azure', 'SQL', 'JavaScript']  # Example skills
            skill_experience = {}
            

        with col2:
            # Column 2: Candidate Status, Recruitment Source, Relocation Assistance, Reason, and Notes
            contact2 = st.text_input("Contact #2", placeholder="03462345678")
            email2 = st.text_input("Email #2", placeholder="kamran@gmail.com")  # Fixed typo in the variable name
            state = st.text_input("State", placeholder="Sindh")
            address = st.text_input("Address", placeholder="House-1, Gulshan e Maymar, XYZ, Karachi")
            col3, col4 = st.columns([1, 1])
            with col3:
                time_selected = st.time_input("Calling Time", value=time(12, 0))
            with col4:
                timezone = st.selectbox("Timezone", ["CST", "PST", "EST"])
                
            interview_mode = st.selectbox("Interview Mode", ["In-Person", "Virtual"], key="interview_mode_1")   
            current_salary = st.number_input("Current Salary", min_value=0)
            availability_for_2nd_interview = st.date_input("Candidate Availability For 2nd Interview")
            relocation_assistance = st.selectbox("Relocation Assistance", ["Yes", "No"], key="relocation_assistance_1")
            role_related_experience = st.text_input("Role Related Experience")

        
        col5, col6, col7, col8, col9 = st.columns([1, 1, 1, 1, 1])
        with col5:
            skill_experience['Python'] = st.number_input(f"Years of Experience in Python", min_value=0, key=f"Python_experience")

        with col6:
            skill_experience['Power BI'] = st.number_input(f"Years of Experience in Power BI", min_value=0, key=f"Power_BI_experience")

        with col7:
            skill_experience['MySQL'] = st.number_input(f"Years of Experience in MySQL", min_value=0, key=f"MySQL_experience")

        with col8:
            skill_experience['DataBricks'] = st.number_input(f"Years of Experience in DataBricks", min_value=0, key=f"DataBricks_experience")

        with col9:
            skill_experience['Azure'] = st.number_input(f"Years of Experience in Azure", min_value=0, key=f"Azure_experience")


        reason = st.text_area("Reason for Leaving")
        notes = st.text_area("Recruiter Notes")

        # Convert selected time to the chosen timezone
        if timezone == "CST":
            timezone_info = pytz.timezone('America/Chicago')
        elif timezone == "PST":
            timezone_info = pytz.timezone('America/Los_Angeles')
        else:
            timezone_info = pytz.utc  # Default to UTC if no valid timezone is selected

        # Current time with selected timezone
        now = datetime.now(timezone_info)
        local_time = timezone_info.localize(datetime.combine(now.date(), time_selected))


        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Insert the form data into the SQLite database
            c.execute(''' INSERT INTO form_1 (
                full_name, contact_1, contact_2, email_1, email_2, country, state, city, address,
                calling_date, calling_time, timezone, source, interview_mode, expected_salary,
                current_salary, notice_period, candidate_availability_for_2nd_interview,
                current_employment_status, relocation_assistance, work_arrangement, role_related_experience,
                years_of_experience_in_python, years_of_experience_in_power_bi, years_of_experience_in_mysql,
                years_of_experience_in_databricks, years_of_experience_in_azure, reason_for_leaving, recruiter_notes
            )
            VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
''', (full_name, contact1, contact2, email1, email2, country, state, city, address,
      calling_date, time_selected.strftime("%H:%M:%S"), timezone, source, interview_mode, expected_salary,
      current_salary, notice_period, availability_for_2nd_interview, current_employment_status, relocation_assistance,
      work_arrangement, role_related_experience, skill_experience['Python'], skill_experience['Power BI'],
      skill_experience['MySQL'], skill_experience['DataBricks'], skill_experience['Azure'], reason, notes))
        
            conn.commit()

            st.success("Form submitted successfully!")

# Close the database connection
conn.close()

# 2nd Interview Form
if page == "2nd Interview":
    st.header("2nd Interview")

    with st.form(key='second_interview_form'):
        full_name = st.text_input("Full Name")
        # Create columns for better layout
        col1, col2 = st.columns([1, 1])

        with col1:
            # Column 1: Personal Information and Interview Details
            contact1 = st.text_input("Contact #1")
            email1 = st.text_input("Email #1")
            country = st.selectbox("Country", ["Pakistan", "India", "United States", "Canada"], key="country")
            city = st.text_input("City")
            calling_date = st.date_input("Calling Date")
            source =st.selectbox("Source", ["Indeed", "LinkedIn", "Monster", "Dice", "Taldel", "traxccel"], key="source_1")
            interview_date = st.date_input("2nd Interview Date")
            hiring_manager_id = st.text_input("Hiring Manager ID")
            interview_duration = st.number_input("Interview Duration (minutes)", min_value=0)
            interview_location = st.text_input("Interview Location")
            technically_sound  = st.selectbox(
                "Technical Score", 
                list(range(1, 11)),  # List of numbers from 1 to 10
                index=0  # Default to 1
            )
            
            technical_assessment_score = st.number_input("Technical Assessment Score", min_value=0)
            ##cultural_fit = st.text_input("Cultural Fit")
            leadership_potential_years = st.selectbox(
                "Leadership Potential (Years of Experience)",
                list(range(1, 21)),  # List of years from 1 to 20
                index=0  # Default to 1 year
            )
            recommend = st.selectbox("Recommend", ["Yes", "No"], key="recommend_2")
            interview_panel = st.text_area("Interview Panel")
            ##decision_date = st.date_input("Decision Date")
            interview_feedback = st.text_area("Interview Feedback")
            overall_technical_rating = st.slider("Overall Technical Rating", min_value=1, max_value=10, value=1)

        with col2:
            # Column 2: Additional Candidate Status and Attributes
            contact2 = st.text_input("Contact #2")
            email2 = st.text_input("Email #2")  # Fixed typo in the variable name
            state = st.text_input("State")
            address = st.text_input("Address")

            col3, col4 = st.columns([1, 1])
            with col3:
                time_selected = st.time_input("Calling Time", value=time(12, 0))
            with col4:
                timezone = st.selectbox("Timezone", ["CST", "PST"])

            job_id = st.text_input("Job ID")
            candidate_id = st.text_input("Candidate ID")
            interviewer_id = st.text_input("Interviewer ID")
            interview_mode = st.selectbox("Interview Mode", ["In-Person", "Virtual"], key="interview_mode_2")
            personality = st.selectbox(
                "Overall Personality", 
                ["Extroverted", "Introverted", "Ambivert", "Assertive", "Reserved", "Creative", "Analytical", "Proactive"],
                key="personality"
            )
            communication_skills_score = st.selectbox(
                "Communication Skills Score", 
                list(range(1, 11)),  # List of numbers from 1 to 10
                index=0  # Default to 1
            )
            problem_solving_skills = st.selectbox(
                "Problem-Solving Skills", 
                list(range(1, 11)),  # List of numbers from 1 to 10
                index=0  # Default to 1
            )
            team_collaboration_years = st.selectbox(
                "Team Collaboration (Years of Experience)",
                list(range(1, 21)),  # List of years from 1 to 20
                index=0  # Default to 1 year
            )
            current_employment_status = st.selectbox("Current Employment Status", ["Fresh", "Employed", "Unemployed"], key="current_employment_status")
            
            ##team_collaboration = st.text_input("Team Collaboration")
            ##adaptability = st.text_input("Adaptability")
            follow_up_actions = st.text_area("Follow-up Actions")
            
            

            # Convert selected time to the chosen timezone
        if timezone == "CST":
            timezone_info = pytz.timezone('America/Chicago')
        elif timezone == "PST":
            timezone_info = pytz.timezone('America/Los_Angeles')
        else:
            timezone_info = pytz.utc  # Default to UTC if no valid timezone is selected

        # Current time with selected timezone
        now = datetime.now(timezone_info)
        local_time = timezone_info.localize(datetime.combine(now.date(), time_selected))


        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.write("Form submitted successfully!")
            st.write("Full Name:", full_name)
            st.write(f"Contact #1: {contact1}")
            st.write(f"Contact #2: {contact2}")
            st.write(f"Email #1: {email1}")
            st.write(f"Email #2: {email2}")
            st.write("Calling Date:", calling_date)
            st.write("Job ID:", job_id)
            st.write("Candidate ID:", candidate_id)
            st.write("Interview Date:", interview_date)
            st.write("Interviewer ID:", interviewer_id)
            st.write("Interview Mode:", interview_mode)
            st.write("Interview Duration:", interview_duration)
            st.write("Interview Location:", interview_location)
            st.write("Interview Panel:", interview_panel)
            st.write("Technical Assessment Score:", technical_assessment_score)
            st.write("Problem-Solving Skills:", problem_solving_skills)
            st.write("Cultural Fit:", cultural_fit)
            st.write("Team Collaboration (Years of Experience):", team_collaboration)
            st.write("Leadership Potential (Years of Experience):", leadership_potential)
            st.write("Adaptability:", adaptability)
            st.write("Follow-up Actions:", follow_up_actions)
            #st.write("Decision Date:", decision_date)
            st.write("Hiring Manager ID:", hiring_manager_id)
            st.write("Interview Feedback:", interview_feedback)
            st.write("Overall Technical Rating:", final_interview_score)
            st.write("Technical Score:", technically_sound)
            st.write("Overall Personality:", personality)
            st.write("Communication Skills Score:", communication_skills)
            st.write("Recommend:", recommend)
            st.write("Current Employment Status:", current_employment_status)

# Hiring Details Form
elif page == "Hiring Details":
    st.header("Hiring Details")
    
    with st.form(key='hiring_details_form'):
        full_name = st.text_input("Full Name")
        # Create columns for better layout
        col1, col2 = st.columns([1, 1])

        with col1:
            # Column 1: Job and Candidate Information
            contact_no = st.text_input("Contact No")
            calling_date = st.date_input("Calling Date")
            job_id = st.text_input("Job ID")
            final_interview_date = st.date_input("Final Interview Date")
            offer_acceptance_date = st.date_input("Offer Acceptance Date")
            salary_offered = st.number_input("Salary Offered", min_value=0)
            department = st.text_input("Department")
            contract_type = st.selectbox("Contract Type", ["Permanent", "Temporary", "Contract"], key="contract_type")
            candidate_status = st.selectbox("Candidate Status", ["Hired", "Rejected", "Withdrawn"], key="candidate_status_hiring")
            background_check_status = st.selectbox("Background Check Status", ["Pending", "Completed", "Failed"], key="background_check_status")
            hiring_notes = st.text_area("Hiring Notes")
            
        with col2:
            # Column 2: Contract and Status Information
            email = st.text_input("Email")
            source = st.selectbox("Source", ["Indeed", "LinkedIn"], key="source_hiring")
            hiring_manager_id = st.text_input("Hiring Manager ID")
            offer_status = st.selectbox("Offer Status", ["Extended", "Accepted", "Declined"], key="offer_status")
            offer_date = st.date_input("Offer Date")
            start_date = st.date_input("Start Date")
            position_title = st.text_input("Position Title")
            work_arrangement = st.selectbox("Work Arrangement", ["Remote", "Hybrid", "On-site"], key="work_arrangement_hiring")
            references_check_status = st.selectbox("References Check Status", ["Pending", "Completed"], key="references_check_status")
            benefits_offered = st.text_area("Benefits Offered")

        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.write("Form submitted successfully!")
            st.write("Full Name:", full_name)
            st.write("Contact No:", contact_no)
            st.write("Email:", email)
            st.write("Calling Date:", calling_date)
            st.write("Job ID:", job_id)
            st.write("Hiring Manager ID:", hiring_manager_id)
            st.write("Final Interview Date:", final_interview_date)
            st.write("Offer Date:", offer_date)
            st.write("Offer Acceptance Date:", offer_acceptance_date)
            st.write("Start Date:", start_date)
            st.write("Position Title:", position_title)
            st.write("Department:", department)
            st.write("Salary Offered:", salary_offered)
            st.write("Contract Type:", contract_type)
            st.write("Candidate Status:", candidate_status)
            st.write("Background Check Status:", background_check_status)
            st.write("Hiring Notes:", hiring_notes)

# Employee Details Form
elif page == "Employee Details":
    st.header("Employee Details")

    with st.form(key='employee_details_form'):
        employee_id = st.text_input("Employee ID")
        employee_photo = st.file_uploader("Employee Photo", type=["jpg", "jpeg", "png"])
        # Create columns for better layout
        col1, col2 = st.columns([1, 1])

        with col1:
            # Column 1: Personal Information
            first_name = st.text_input("First Name")
            phone_number = st.text_input("Phone Number")
            date_of_birth = st.date_input("Date of Birth")
            nationality = st.text_input("Nationality")
            address_cnic = st.text_input("Address (as per CNIC)")
            emergency_contact_name = st.text_input("Emergency Contact Name")
            job_title = st.text_input("Job Title")
            department = st.text_input("Department")
            work_arrangement = st.selectbox("Work Arrangement", ["On-site", "Remote", "Hybrid"], key="work_arrangement_employee")
            salary = st.number_input("Salary", min_value=0)
            leave_balance = st.number_input("Leave Balance", min_value=0)
            employee_benefits = st.text_area("Employee Benefits")
            skills_certifications = st.text_area("Skills and Certifications")
            employee_status = st.selectbox("Employee Status", ["Active", "Inactive", "On Leave"], key="employee_status")
            reason_for_termination = st.text_area("Reason for Termination")
            employee_notes = st.text_area("Employee Notes")

        with col2:
            # Column 2: Emergency Contact and Additional Information
            last_name = st.text_input("Last Name")
            email_address = st.text_input("Email Address")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
            address = st.text_input("Address")
            emergency_contact_phone = st.text_input("Emergency Contact Phone")
            hire_date = st.date_input("Hire Date")
            employment_type = st.selectbox("Employment Type", ["Full-time", "Part-time", "Contract"], key="employment_type")
            manager_id = st.text_input("Manager ID")
            office_location = st.text_input("Office Location")
            years_of_service = st.number_input("Years of Service", min_value=0)
            last_promotion_date = st.date_input("Last Promotion Date")
            performance_reviews = st.text_area("Performance Reviews")
            training_records = st.text_area("Training Records")
            date_of_termination = st.date_input("Date of Termination")

        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.write("Form submitted successfully!")
            st.write("Employee ID:", employee_id)
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            st.write("Date of Birth:", date_of_birth)
            st.write("Gender:", gender)
            st.write("Nationality:", nationality)
            st.write("Address (as per CNIC):", address_cnic)
            st.write("Address:", address)
            st.write("Phone Number:", phone_number)
            st.write("Email Address:", email_address)
            st.write("Employee Status:", employee_status)
            st.write("Hire Date:", hire_date)
            st.write("Job Title:", job_title)
            st.write("Department:", department)
            st.write("Manager ID:", manager_id)
            st.write("Employment Type:", employment_type)
            st.write("Salary:", salary)
            st.write("Work Arrangement:", work_arrangement)
            st.write("Office Location:", office_location)
            st.write("Employee Benefits:", employee_benefits)
            st.write("Emergency Contact Name:", emergency_contact_name)
            st.write("Emergency Contact Phone:", emergency_contact_phone)
            if employee_photo is not None:
                st.image(employee_photo, caption="Employee Photo", use_column_width=True)
            st.write("Date of Termination:", date_of_termination)
            st.write("Reason for Termination:", reason_for_termination)
            st.write("Years of Service:", years_of_service)
            st.write("Last Promotion Date:", last_promotion_date)
            st.write("Performance Reviews:", performance_reviews)
            st.write("Skills and Certifications:", skills_certifications)
            st.write("Training Records:", training_records)
            st.write("Leave Balance:", leave_balance)
            st.write("Employee Notes:", employee_notes)
