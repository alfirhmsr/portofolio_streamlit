import streamlit as st

st.title("📖 Tentang Saya")

st.write(
    """
    Halo! Nama saya **Alfi**, saya peserta bootcamp DataScience batch 29 diBimbing.
    """
)

# Fun Facts List
fun_facts = [
    "💻 Saya suka minuman dingin☕",
    "🎮 Gamer di waktu senggang 🎮",
    "📚 Saya suka warna biru",
]

st.subheader("🎉 Fun Facts tentang Saya")
for fact in fun_facts:
    st.write(f"- {fact}")

