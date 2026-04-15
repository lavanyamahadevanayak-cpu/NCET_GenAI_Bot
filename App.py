import streamlit as st
from groq import Groq

st.set_page_config("pragyanAI Content Generator",layout="width")
st.title("pragyanAI -context Generator")
st.image("Screenshot 2025-12-24 082406.png")
client=Groq(api_key=st.secrets["GROQ_API_KEY"])
product = st.text_input("Product")
audience = st.text_input("Audience")
if st.button("Generate Content"):
  prompt = f"Write marketing content for {product} targeting {audience}."
  response = client.chat.chat.completions.create(
  model ="llama-3.3-70b-versatile",
  messages=[{"role": "user", "content": prompt}]
  )
  st.session_stste.text = response.choices[0].message.content
  text =response.choice[0].message.content
  st.write(text)
  if "text" in st.session_state:
      content = st.text_area("Generated Content", st.ession_state.text, height=300)
      st.download_button(
        label="Doumload as TXT",
        data=content,
        file_name="marketing_copy.txt",
        mime="text/plain"
      )
  else:
       st.info("Generate content first")


  
