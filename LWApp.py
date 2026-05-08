import streamlit as st
import pandas as pd

# CONFIGURAZIONE UI
st.set_page_config(page_title="Last War: GOD TIER Optimizer", layout="wide")

# STYLE CSS AVANZATO
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #161b22; border-radius: 5px 5px 0 0; gap: 1px; padding: 10px; }
    .stat-card { background: #1c2128; border: 1px solid #30363d; padding: 20px; border-radius: 10px; margin-bottom: 10px; }
    .database-header { color: #f0883e; border-bottom: 2px solid #f0883e; padding-bottom: 5px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE DI GIOCO INTEGRATO (CON I TUOI DATI) ---
def get_game_database():
    return {
        "Armi Esclusive (UR)": {
            "Kimberly (Cannone Gatling)": "Lv.30: Aumento Danno Abilità +30%. Lv.40: Riduzione ricarica. Necessaria per il burst iniziale.",
            "Stetmann (Laser Core)": "Lv.30: Aumento critico cumulativo. Fondamentale per rompere i tank nemici.",
            "Murphy (Scudo Energia)": "Lv.20+: Aumento drastico della Riduzione Danno (fondamentale per le tue T11)."
        },
        "Equipaggiamento Rosso (Mythic)": {
            "Arma": "Priorità 1: Attacco e Perforazione Difesa.",
            "Corazza": "Priorità 2: PS e Riduzione Danno Finale (essenziale per uscire dallo stato 'Glass Cannon').",
            "Radar": "Riduzione Probabilità Critico (il tuo punto debole attuale: 7.60%).",
            "Stivali": "Aumento Velocità e Difesa."
        },
        "Meccanica T11": {
            "Soppressione Tier": "Le T11 infliggono il 10-15% di danno extra contro le T10 e subiscono il 10% in meno.",
            "Unità X": "L'unico ramo rimasto per te. Sblocca bonus PS che superano il cap del 40% delle tecnologie base."
        }
    }

# --- LOGICA DASHBOARD ---
st.title("🎖️ Last War Tactical Engine: T11 God Tier")

tab1, tab2, tab3, tab4 = st.tabs(["📊 Analisi Player", "🛸 Drone & Chip", "🛡️ Database Enciclopedico", "⚔️ Simulatore T11"])

with tab1:
    st.header("Analisi Status Tecnologico: MAXED")
    st.success("✅ Tecnologie Base (Eroi): 100% | ✅ Forze Speciali: 100% | ✅ Maestria Carro: 100%")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Attacco Totale (Carro)", "85.50%", "+20% Cosmetici")
    with col2:
        st.metric("PS Totali (Carro)", "80.00%", "Cap Tecnologico")
    with col3:
        st.metric("Riduzione Danno", "10.75%", "Margine Critico")

with tab2:
    st.header("🛸 Stato Drone Lv. 180")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("**Efficienza Componenti (Lv. 9)**")
        comps = {"Radar Precisione": 92, "Processore": 87, "Sensore": 86, "Motore": 25, "Radar": 16, "Chip Memoria": 13}
        for k, v in comps.items():
            st.write(f"{k}: {v}%")
            st.progress(v/100)
    with col_b:
        st.info("💡 **Analisi di Sopravvivenza**")
        st.write(f"Con un **Chip Memoria al 13%**, la tua riduzione critici da Drone è solo del **2.60%**.")
        st.error("⚠️ Il gap tra Attacco (+15.5%) e PS (+13%) nel drone crea l'effetto 'Glass Cannon'.")

with tab3:
    db = get_game_database()
    st.header("📚 Enciclopedia Last War")
    
    for categoria, info in db.items():
        st.markdown(f"<h3 class='database-header'>{categoria}</h3>", unsafe_allow_html=True)
        if isinstance(info, dict):
            for sub, testo in info.items():
                st.write(f"**{sub}**: {testo}")
        else:
            st.write(info)

with tab4:
    st.header("⚔️ Simulatore Scontro T11 vs T11")
    st.write("In uno scontro tra pari livello tecnologico, la vittoria è determinata dalla **Riduzione Danno Finale**.")
    st.markdown("""
        1. **Calcolo Danno Kimberly**: Il tuo +53.31% satura le difese T10.
        2. **Necessità PS**: Con l'80% di PS, sei vulnerabile ai burst critici (Danno Critico nemico stimato > 200%).
        3. **Soluzione**: Investire in **Unità X** (Unità Tank) per sbloccare i nodi di 'Riduzione Danno' che Forze Speciali non ha più.
    """)
