import streamlit as st
import pandas as pd

# CONFIGURAZIONE UI
st.set_page_config(page_title="Last War: Professional Tactical Wiki", layout="wide")

# DATABASE DETTAGLIATO ARMI ESCLUSIVE & ABILITÀ
EXCL_WEAPONS_DB = {
    "Kimberly (Rocket Gatling)": {
        "Lv. 10": "Aumenta il Danno Abilità del 10%.",
        "Lv. 20": "Aggiunge un razzo extra alla raffica principale.",
        "Lv. 30": "Effetto Critico: Ogni colpo critico riduce la difesa del bersaglio del 2% (cumulabile).",
        "Lv. 40": "Danno Finale +15% e aumento velocità di ricarica energia."
    },
    "Stetmann (Tesla Core)": {
        "Lv. 10": "Aumenta la probabilità di attivazione del 'Tesla Bounce' del 5%.",
        "Lv. 20": "Il raggio rimbalza su un bersaglio aggiuntivo.",
        "Lv. 30": "Stato 'Overdrive': Dopo 3 attivazioni, il prossimo colpo ignora il 20% della Difesa nemica.",
        "Lv. 40": "Aumento Danno Critico del 25% per tutta la durata dello scontro."
    },
    "Murphy (Iron Shield)": {
        "Lv. 10": "Aumenta la riduzione danno fisica del 5%.",
        "Lv. 20": "Quando lo scudo è attivo, Murphy riflette il 10% del danno subito.",
        "Lv. 30": "Immunità al Crowd Control (stordimento) per i primi 5 secondi di battaglia.",
        "Lv. 40": "Condivisione Danni: Murphy assorbe il 15% del danno diretto inflitto alla backline."
    },
    "Marshall (Tactical Radio)": {
        "Lv. 10": "Aumenta la durata del buff Attacco del 15%.",
        "Lv. 20": "Il buff ora aumenta anche la Velocità d'Attacco del 10%.",
        "Lv. 30": "Frequenza Critica: Gli alleati sotto l'effetto del buff hanno +10% Tasso Critico.",
        "Lv. 40": "Ricarica Rapida: Riduce il tempo di ricarica delle abilità di tutta la squadra."
    }
}

# --- INTERFACCIA APP ---
st.title("🛡️ Last War: Encyclopedia & Tactical Optimizer")

tabs = st.tabs(["📚 Database Armi Esclusive", "⚔️ Analisi T11 & Unità X", "⚙️ Il Tuo Setup"])

with tabs[0]:
    st.header("🔬 Breakpoint Armi Esclusive (UR)")
    st.info("Visualizza i potenziamenti per ogni soglia di livello per decidere dove investire i tuoi frammenti.")
    
    selected_hero = st.selectbox("Seleziona Eroe per dettagli arma:", list(EXCL_WEAPONS_DB.keys()))
    
    # Visualizzazione a schede per i breakpoint
    cols = st.columns(4)
    data_hero = EXCL_WEAPONS_DB[selected_hero]
    
    for i, (lv, desc) in enumerate(data_hero.items()):
        with cols[i]:
            st.markdown(f"### {lv}")
            st.write(desc)
            if "30" in lv: st.success("🎯 Breakpoint Fondamentale")

with tabs[1]:
    st.header("🎖️ Meccaniche Avanzate: Verso le T11")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dati Unità X (Tank)")
        st.write("""
        Essendo al 100% di Special Forces, Unità X è la tua unica via.
        - **Nodo 1-5**: Aumento HP Flat (Fondamentale per superare il tuo 80%).
        - **Nodo 6-10**: Riduzione Danno Finale (L'unica statistica che contrasta le T11 nemiche).
        - **Sblocco T11**: Richiede il completamento del ramo centrale.
        """)
        
    with col2:
        st.subheader("Meccanica di Perforazione")
        st.write("""
        A livello T11, la Difesa nemica è altissima. 
        - **Kimberly** ha bisogno di equipaggiamento con **Perforazione Difesa**.
        - Se la tua perforazione è < 15%, il tuo +85% Attacco verrà mitigato del 40% dai tank nemici (Murphy/Williams).
        """)

with tabs[2]:
    st.header("📊 Recap Bonus Attuali (Dai tuoi dati)")
    # Visualizzazione compatta dei tuoi dati estratti
    st.table(pd.DataFrame({
        "Statistica": ["Attacco Carro", "PS Carro", "Danno Eroe", "Riduzione Danno", "Critico (Drone)"],
        "Valore": ["85.50%", "80.00%", "53.31%", "10.75%", "2.50%"],
        "Status": ["ECCELLENTE", "MAX TECNO", "SOLIDO", "CRITICO", "DEBOLE"]
    }))
