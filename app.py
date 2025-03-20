import streamlit as st
import subprocess

def generate_blog(topic, audience):
    prompt = f"Write a structured, refined, and SEO-friendly blog post on '{topic}' tailored for {audience}."
    result = subprocess.run([
        "ollama", "run", "deepseek-r1:1.5b", prompt
    ], capture_output=True, text=True)
    return result.stdout.strip()

st.title("AI-Powered Blog & Article Writer")

st.write("Enter a topic and select your target audience to generate a structured, SEO-friendly blog post.")

topic = st.text_input("Enter Blog Topic:")
audience = st.selectbox("Select Target Audience:", ["Common People", "AI/ML Engineers", "Data Scientists"])

generate_button = st.button("Generate Blog Post")

if generate_button and topic:
    st.markdown(f"# **{topic}**")
    st.write("\n")
    blog_content = generate_blog(topic, audience)
    st.markdown(blog_content)
