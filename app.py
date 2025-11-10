import streamlit as st
import base64
from pathlib import Path
import fitz  # PyMuPDF

# Configuration de la page
st.set_page_config(
    page_title="Certificat d'Anglais - NIAKO KEBE",
    page_icon="🎓",
    layout="centered"
)

# Style CSS personnalisé avec badge de progression
st.markdown("""
<style>
    .progress-badge {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-left: 10px;
        font-size: 0.9em;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .level-progress {
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .progress-bar {
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
        height: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .certificate-image {
        border: 2px solid #3498db;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour convertir PDF en images
def pdf_to_images(pdf_path):
    """Convertit un PDF en images pour l'affichage"""
    try:
        pdf_document = fitz.open(pdf_path)
        images = []
        
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Augmente la résolution
            img_data = pix.tobytes("png")
            images.append(img_data)
        
        pdf_document.close()
        return images
    except Exception as e:
        st.error(f"Erreur lors de la conversion du PDF: {e}")
        return None

# Fonction pour le téléchargement
def create_download_link(file_path):
    """Crée un lien de téléchargement pour le PDF"""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode()
    
    download_link = f'''
    <a href="data:application/pdf;base64,{base64_pdf}" 
       download="Certificat_Anglais_NIAKO_KEBE.pdf" 
       style="
           background-color: #3498db; 
           color: white; 
           padding: 12px 24px; 
           text-decoration: none; 
           border-radius: 5px; 
           display: inline-block;
           font-weight: bold;
           margin: 10px 0;
       ">
       📄 Télécharger le Certificat PDF Original
    </a>
    '''
    return download_link

# Interface principale avec progression vers B2
st.markdown("""
<h1 style='text-align: center;'>
    🎓 Certificat d'Anglais - NIAKO KEBE 
    <span class='progress-badge'>📈 En progression vers B2</span>
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# Section de progression
st.subheader("🚀 Ma progression en Anglais")

# Barre de progression visuelle
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class='level-progress'>
        <div style='display: flex; justify-content: space-between;'>
            <span><strong>A2</strong> (Actuel)</span>
            <span><strong>B1</strong> (Intermédiaire)</span>
            <span><strong>B2</strong> (Objectif)</span>
        </div>
        <div class='progress-bar' style='width: 60%;'></div>
        <p style='text-align: center; margin: 0;'>
            <strong>Progression:</strong> A2 → B1 → B2
        </p>
    </div>
    """, unsafe_allow_html=True)

# Objectifs de progression
with st.expander("🎯 Mon parcours de progression vers B2"):
    st.markdown("""
    **📅 Début de la progression:** Octobre 2025
    
    **🎯 Objectif actuel:** Niveau B2 (Intermédiaire supérieur)
    
    **📈 Compétences visées:**
    - 💬 Comprendre des textes complexes
    - 🗣️ Conversation fluide sur des sujets variés
    - ✍️ Rédaction de textes détaillés
    - 🎧 Compréhension de discours complexes
    
    **🔄 Prochaines étapes:**
    - Passage au niveau B1 (Intermédiaire)
    - Atteinte du niveau B2 (Intermédiaire supérieur)
    - Préparation aux certifications internationales
    """)

st.markdown("---")

# Vérifier si le fichier PDF existe et l'afficher
pdf_path = "certificat.pdf"

try:
    # Afficher le PDF comme image
    st.subheader("📜 Certificat Actuel (Niveau A2)")
    st.info("""
    **Certificat actuel:** Niveau A2 Élémentaire  
    **Statut:** En formation active pour atteindre le niveau B2
    """)
    
    # Convertir et afficher le PDF comme image
    images = pdf_to_images(pdf_path)
    
    if images:
        for i, img_data in enumerate(images):
            # st.image(img_data, use_container_width=True, caption=f"Page {i+1} du certificat")
            st.image(img_data, width=700, caption=f"Page {i+1} du certificat")

    else:
        st.error("Impossible de charger le certificat")
    
    # Bouton de téléchargement
    st.markdown("---")
    st.subheader("📥 Téléchargement")
    st.markdown(create_download_link(pdf_path), unsafe_allow_html=True)
    
    # Informations supplémentaires
    with st.expander("ℹ️ Détails du Certificat"):
        st.write("""
        **Détails du certificat:**
        - **Nom:** NIAKO KEBE
        - **Niveau actuel:** 2 (A2 - Élémentaire)
        - **Objectif:** Niveau B2 (Intermédiaire supérieur)
        - **Date de délivrance:** 20 Octobre 2025
        - **Émis par:** Centre de Perfectionnement en Langue Anglaise (CPLA)
        - **Ministère de l'Éducation nationale du Sénégal**
        """)

except FileNotFoundError:
    st.error("""
    ❌ Fichier PDF non trouvé !
    
    **Pour afficher votre certificat:**
    1. Assurez-vous que le fichier PDF est dans le même dossier que cette application
    2. Le fichier doit s'appeler : `certificat.pdf`
    """)
    
    # Option pour uploader le fichier
    uploaded_file = st.file_uploader("Ou uploader votre certificat PDF", type="pdf")
    
    if uploaded_file is not None:
        # Sauvegarder le fichier uploadé
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success("✅ Certificat uploadé avec succès!")
        st.rerun()

# Section de motivation
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(45deg, #667eea, #764ba2); padding: 20px; border-radius: 10px; color: white; text-align: center;'>
    <h3>💪 Engagement et Persévérance</h3>
    <p><em>"Je suis déterminé à atteindre le niveau B2 et à continuer mon apprentissage de l'anglais avec passion et régularité."</em></p>
</div>
""", unsafe_allow_html=True)

# Pied de page
st.markdown("---")
st.caption("🎓 Certificat d'Anglais | NIAKO KEBE | Niveau A2 - En progression vers B2 | Début de formation: Octobre 2025")