import streamlit as st
st.title("5 Basic Component Streamlit!")

st.subheader("Basic component of streamlit 1: text")

st.markdown('**I am a student of Dibimbing Bootcamp B29**')

st.markdown("<p style='color:pink; font-size:20px;'>[🌸 And this is my assignment! 🌸]</p>", unsafe_allow_html=True)

st.subheader("Basic component of streamlit 2: button")
import random
moods = ["😊 Happy", "🤩 Excited", "😴 Sleepy", "🥳 Party Mode!", "🤔 Thinking", "😎 Cool"]
if st.button("🎲 Acak Mood Hari Ini"):
    st.write(f"🎭 Mood kamu hari ini: **{random.choice(moods)}**")

    
st.subheader("Basic component of streamlit 3: gambar")

st.image("pngegg.png", caption="yuhuu 😊", use_container_width=True)

st.subheader("Basic component of streamlit 4: grafik")

import matplotlib.pyplot as plt
import numpy as np

# 🔹 Data Dummy
categories = ["Makeup", "Pakaian", "Kuota", "Makan"]
values = np.random.randint(5, 15, size=4)  # Angka acak

# 🔹 Membuat Grafik
fig, ax = plt.subplots()
ax.bar(categories, values, color=["red", "yellow", "purple", "green"])  # Warna sesuai buah

# 🔹 Tambahkan Label
ax.set_ylabel("Total (Rp)")
ax.set_title(" Kemana perginya uang saya? ")

# 🔹 Menampilkan Grafik di Streamlit
st.pyplot(fig)

st.subheader("Basic component of streamlit 5: form")

st.subheader("📩 Kirim Pesan untuk Aku!")
name = st.text_input("Nama kamu:")
message = st.text_area("Pesan:")
if st.button("📨 Kirim"):
    st.success(f"Terima kasih, {name}! Aku akan baca pesanmu: \"{message}\" 💌")

    