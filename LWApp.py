import streamlit as st
import pandas as pd

# Configurazione Pagina
st.set_page_config(page_title="Last War Strategist Pro", layout="wide")

st.title("🛡️ Last War: Survival - Optimizer v1.0")
st.sidebar.header("Pannello Aggiornamento Dati")

# --- DATABASE INIZIALE (I tuoi dati) ---
if 'data' not in st.session_state:
    st.session_state.data = {
        "decorazioni": {"danno_critico": 15.25, "danno_abilita": 7.06, "riduzione_danni": 5.75},
        "skin_bonus": {"attacco_perc": 130.0, "difesa_perc": 105.0, "ps_perc": 120.0},
        "flat_stats": {"ps": 1524554, "difesa": 23839, "attacco": 24060},
        "eroi": {
            "Kimberly": {"lv": 150, "arma_escl": 30, "tipo": "Tank", "ruolo": "Attacco"},
            "Murphy": {"lv": 150, "arma_escl": 30, "tipo": "Tank", "ruolo": "Difesa"},
            "Marshall": {"lv": 150, "arma_escl": 30, "tipo": "Tank", "ruolo": "Supporto"},
            "Stetman": {"lv": 150, "arma_escl": 20, "tipo": "Tank", "ruolo": "Attacco"},
            "Lucius": {"lv": 150, "arma_escl": 20, "tipo": "Aereo", "ruolo": "Difesa"}
        }
    }

# --- INTERFACCIA DI AGGIORNAMENTO ---
with st.sidebar:
    st.subheader("Aggiorna Statistiche Flat")
    st.session_state.data["flat_stats"]["ps"] = st.number_input("PS Totali Extra", value=st.session_state.data["flat_stats"]["ps"])
    st.session_state.data["flat_stats"]["attacco"] = st.number_input("Attacco Totale Extra", value=st.session_state.data["flat_stats"]["attacco"])
    
    st.subheader("Livello Armi Esclusive")
    for eroe in st.session_state.data["eroi"]:
        st.session_state.data["eroi"][eroe]["arma_escl"] = st.slider(f"{eroe}", 0, 30, st.session_state.data["eroi"][eroe]["arma_escl"])

# --- MOTORE DI CALCOLO ---
def calcola_potenza_schieramento(lista_eroi):
    # Logica semplificata: calcola il bonus sinergia
    tipi = [st.session_state.data["eroi"][e]["tipo"] for e in lista_eroi]
    count_tank = tipi.count("Tank")
    
    bonus_fazione = 0
    if count_tank == 5: bonus_fazione = 0.20 # +20% stats per 5 tank
    elif count_tank == 4: bonus_fazione = 0.15
    
    # Calcolo ipotetico potenza
    potenza_base = (st.session_state.data["flat_stats"]["attacco"] * 
                   (1 + st.session_state.data["skin_bonus"]["attacco_perc"]/100))
    return potenza_base * (1 + bonus_fazione)

# --- VISUALIZZAZIONE ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("⚔️ Schieramento Suggerito")
    selezione = st.multiselect("Seleziona 5 eroi per il campo:", 
                               options=list(st.session_state.data["eroi"].keys()), 
                               default=list(st.session_state.data["eroi"].keys())[:5])
    
    if len(selezione) == 5:
        potenza = calcola_potenza_schieramento(selezione)
        st.success(f"Potenza Stimata Formazione: {potenza:,.0f}")
        
        # Tabella riassuntiva
        df_eroi = pd.DataFrame([st.session_state.data["eroi"][e] for e in selezione], index=selezione)
        st.table(df_eroi)
    else:
        st.warning("Seleziona esattamente 5 eroi per vedere l'analisi.")

with col2:
    st.header("📊 Recap Bonus Attivi")
    st.json(st.session_state.data["decorazioni"])
    st.info(f"Bonus Drone Attacco: +21%")
