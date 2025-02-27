import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB92k02wczwkOK3VWuLQZ5JyJWj-uAV6Tk")

def get_travel_recommendations(source, destination):
    """Send travel query to Google Gemini AI API and get recommendations."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    Provide travel options from {source} to {destination}, including:
    - Flight options with estimated costs
    - Train options with estimated costs
    - Bus options with estimated costs
    - Cab options with estimated costs
    """
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else response

st.title("AI-Powered Travel Planner")
st.write("Enter your travel details below:")

source = st.text_input("Source Location:")
destination = st.text_input("Destination Location:")

if st.button("Get Travel Options"):
    if source.strip() and destination.strip():
        with st.spinner("Fetching travel options..."):
            travel_options = get_travel_recommendations(source, destination)
        st.subheader("Travel Recommendations")
        st.write(travel_options)
    else:
        st.warning("Please enter both source and destination!")
