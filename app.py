import streamlit as st
from insert_to_supabase import insert_company_details

st.title("Create My Free Trial – Xavier's Chatbot")

domain = st.text_input("Company Domain Name:")
tone = st.selectbox("Tone of Chatbot:", ["Formal", "Informal", "Professional", "Friendly", "Casual", "Custom"])
custom_tone = ""
if tone == "Custom":
    custom_tone = st.text_input("Enter custom tone:")
description = st.text_input("Company Description:")
expectations = st.text_area("Expectations for Chatbot (e.g., Customer support, FAQ answering, etc.)")

if st.button("Create My Free Trial"):
    final_tone = custom_tone if tone == "Custom" else tone
    data = {
        "domain_name": domain,
        "tone": final_tone,
        "company_description": description,
        "chatbot_expectations": expectations
    }
    res = insert_company_details(data)
    if res.data:
        st.success("✅ Company details stored successfully!")
        # Optionally redirect user
        st.markdown("[Go to Trial Chatbot Page](https://your-trial-page.com)")
    else:
        st.error("❌ Something went wrong.")
