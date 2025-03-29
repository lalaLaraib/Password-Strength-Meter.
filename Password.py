#🔐project 03: Passsword Strength Meter Sir Zia Prroject 3

#📌 Objective:
#Build a Passsword Strength Meter in Python that evaluates a user's password based on security rules.
#The program will:

#Analyze passwords based on length, character types, and patterns.
#Analyze a Strength Score (Weak, Moderate, Strong).
#Provide feedback to improve weak passwords.
#Use control flow, type casting, strings, and functions.

#⭐ Requirements:

#1. Password Strength criteris

#A Strong password should:
#✅ Be atleast 9 character long
#✅ contain uppercase & lowercase letters
#✅ Include atleast one digit (0-9)
#✅ Have one special character (!@#$%^&*)

#2. Scoring System:

#Weak (Score: 1-2) -> Short, misdsing key elements
#Moderate (Score: 3-4) -> Good but missing some security features
#Strong (Score: 5) -> Meets all criteria

#3. Feedback System

#If the password is weak, suggest improvement.
#If the password is strong, display a success message.


import re
import streamlit as st

# page styling:
st.set_page_config(page_title="Password Strength Checker Efza laraib",page_icon="🔑", layout="centered")
# custom css:
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}
    .stButton button:hover { backgroung-color: #45a048;}
<style>       
""", unsafe_allow_html=True)

# page title and deccription:
st.title("🔐Password Strength Meter")
st.write("plaese Enter your password below to check its security level.🔍")

# function check password strength:
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >=8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ Password should be **atleast 9 character long**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ pasword should include **both uppercase (A-Z) and lowercase (a-z) letters**.")


    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9) **.")

    # special character:
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")
    
    # display password strength results:
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - consider improving security by adding more feature")
    else:
        st.error("❌ **Week Password** - Follow the suggestion below to strength it. ")
    

    #feedback:
    if feedback:
        with st.expander("🔍**Improve Your Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")


# button working:
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ please enter a password first!") #show warning if password empty
