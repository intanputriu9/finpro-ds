"""
Contact Me Tab - Profil pengembang dan informasi kontak
"""
import streamlit as st


def render():
    """Render tab Contact Me"""
    st.title("Contact Information")
    st.markdown("---")
    
    # Author Section
    st.markdown("## Penulis")
    
    st.markdown("""
    **[Intan putri Utami]**  
    *Data Science Enthusiast*
      
    [Jakarta, Indonesia]
    """)
    
    st.markdown("---")
    
    # Contact Details
    st.markdown("## Detail Kontak")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Alamat Email**  
        intanputriu9@gmail.com
        
        **Telepon**  
        +62 815-1707-2839
        
        **Lokasi**  
        Jakarta, Indonesia
        """)
    
    with col2:
        st.markdown("""
        **LinkedIn**  
        [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
        
        **GitHub**  
        [github.com/intanputriu9](https://github.com/intanputriu9)
        
        **Instagram**  
        [@intn.ptr](https://instagram.com/intn.ptr)
        """)
    
    st.markdown("---")
    
    
    
    st.markdown("---")
    
    # Research Interests
    st.markdown("## Minat Penelitian")
    
    st.markdown("""
    - Machine Learning & Artificial Intelligence
    - Sistem Deteksi Fraud
    - Data Mining & Pattern Recognition
    - Financial Technology (FinTech)
    """)
    
    st.markdown("---")
    
    # About This Project
    st.markdown("## Tentang Proyek Ini")
    
    st.markdown("""
    **Credit Card Fraud Detection System** ini dikembangkan sebagai bagian dari 
    [nama mata kuliah / skripsi / proyek penelitian] untuk mendemonstrasikan 
    penerapan teknik machine learning dalam keamanan finansial.
    
    **Tujuan:**
    1. Mengimplementasikan classifier Random Forest untuk deteksi fraud
    2. Menangani dataset tidak seimbang menggunakan teknik SMOTE
    3. Mengembangkan dashboard web interaktif menggunakan Streamlit
    4. Menyediakan kemampuan analisis transaksi real-time
    
    **Teknologi & Tools:**
    - **Bahasa Pemrograman:** Python
    - **Library ML:** Scikit-learn, Imbalanced-learn
    - **Web Framework:** Streamlit
    - **Visualisasi:** Matplotlib
    - **Pemrosesan Data:** Pandas, NumPy
    """)
    
    st.markdown("---")
    
  
    
    
