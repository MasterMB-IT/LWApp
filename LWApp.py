import streamlit as st
import pandas as pd

# --- CONFIGURAZIONE AVANZATA ---
st.set_page_config(page_title="Last War Tactical AI", layout="wide")

def apply_custom_css():
    st.markdown("""
        <style>
        .main { background-color: #0e1117; color: white; }
        .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; }
        </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# --- DATABASE EROI (Aggiornato 2026) ---
HERO_DB = {
    "Kimberly": {"tipo": "Tank", "ruolo": "DPS", "tier": "UR"},
    "Murphy": {"tipo": "Tank", "ruolo": "Tank", "tier": "UR"},
    "Marshall": {"tipo": "Tank", "ruolo": "Support", "tier": "UR"},
    "Stetman": {"tipo": "Tank", "ruolo": "DPS", "tier": "UR"},
    "Williams": {"tipo": "Tank", "ruolo": "Tank", "tier": "UR"},
    "Lucius": {"tipo": "Aereo", "ruolo": "Tank", "tier": "UR"},
    "DVA": {"tipo": "Aereo", "ruolo": "DPS", "tier": "UR"},
    "Schuyler": {"tipo": "Aereo", "ruolo": "Crowd Control", "tier": "UR"}
}

# --- SIDEBAR: INPUT DATI ---
with st.sidebar:
    st.title("⚙️ Parametri Globali")
    
    tab1, tab2 = st.tabs(["Dati Base", "Ricerca & Drone"])
    
    with tab1:
        st.subheader("Bonus Skin & Decor")
        atk_pct = st.number_input("Attacco % Totale", value=130.0)
        hp_flat = st.number_input("PS Flat Totali", value=1524554)
        
    with tab2:
        st.subheader("Ricerca Militare")
        sf_level = st.slider("Special Forces (%)", 0, 100, 45)
        drone_parts_priority = st.selectbox("Focus Drone", ["Attacco (Destra)", "Difesa (Sinistra)"])

# --- MOTORE TATTICO (Logica di Counter) ---
def analyze_lineup(selected_heroes, enemy_type):
    # Calcolo Sinergia (es. 5 Tank = 20% bonus)
    types = [HERO_DB[h]["tipo"] for h in selected_heroes]
    tank_count = types.count("Tank")
    
    # Logica di Counter
    # Tank batte Missile (+20%), ma perde da Aereo (-20%)
    counter_multiplier = 1.0
    if tank_count >= 4:
        if enemy_type == "Aereo": counter_multiplier = 0.8
        elif enemy_type == "Missile": counter_multiplier = 1.2
        
    return tank_count, counter_multiplier

# --- INTERFACCIA PRINCIPALE ---
st.title("🛡️ Last War Tactical Optimizer")

col_main, col_stats = st.columns([3, 1])

with col_main:
    st.subheader("⚔️ Simulatore Scontro")
    enemy_team = st.radio("Tipo Team Nemico:", ["Tank", "Aereo", "Missile"], horizontal=True)
    
    my_team = st.multiselect("Il tuo schieramento (Max 5):", 
                             options=list(HERO_DB.keys()), 
                             default=["Kimberly", "Murphy", "Marshall", "Stetman", "Williams"])
    
    if len(my_team) == 5:
        tanks, multiplier = analyze_lineup(my_team, enemy_team)
        
        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Bonus Fazione", f"+{tanks*4}%" if tanks >=3 else "0%")
        c2.metric("Efficacia vs Nemico", f"{multiplier*100}%", delta=f"{int((multiplier-1)*100)}%")
        
        if multiplier < 1.0:
            st.error(f"⚠️ Attenzione: Il tuo team Tank è debole contro {enemy_team}. Valuta di inserire Lucius o DVA.")
        else:
            st.success("✅ Matchup Favorevole o Neutro.")
    
    st.subheader("📈 Roadmap Miglioramenti (Consigli AI)")
    st.info("""
    - **Priorità 1:** Porta l'arma di **Stetman al Livello 30**. Al momento è l'anello debole del tuo DPS backline.
    - **Priorità 2:** Concentra i 'Drone Component Choice Chests' sui componenti di **Destra** (Missile/Fuel Cell). Il tuo attacco % è buono, ma manca il moltiplicatore del drone.
    """)

with col_stats:
    st.subheader("📊 Tuoi Totali")
    st.write(f"**PS Extra:** {hp_flat:,}")
    st.write(f"**Attacco %:** {atk_pct}%")
    st.progress(sf_level / 100, text=f"Ricerca SF: {sf_level}%")
