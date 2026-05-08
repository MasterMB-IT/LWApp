import streamlit as st

# Configurazione UI stile "Tactical Mode"
st.set_page_config(page_title="Last War Engine Pro", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .stNumberInput > label { color: #3b82f6; font-weight: bold; }
    .stat-card { border: 1px solid #262730; padding: 20px; border-radius: 10px; background: #161b22; }
    </style>
""", unsafe_allow_html=True)

# --- DATABASE DINAMICO (Pre-compilato con i tuoi screenshot) ---
if 'stats' not in st.session_state:
    st.session_state.stats = {
        "Attacco Carro": {"Tecno": 40.0, "Drone": 15.5, "Onore": 2.5, "VIP": 7.5, "Cosmetici": 20.0},
        "Difesa Carro": {"Tecno": 40.0, "Drone": 13.0, "Onore": 4.0, "VIP": 7.5, "Cosmetici": 8.0},
        "PS Carro": {"Tecno": 40.0, "Drone": 13.0, "Onore": 4.5, "VIP": 7.5, "Cosmetici": 15.0},
        "Danno Eroe": {"Tecno": 35.0, "Drone": 9.75, "Costruzione": 7.06, "Cosmetici": 1.5}
    }

st.title("🛡️ Last War: Tactical Optimizer V2")
st.write("Dati estratti dagli screenshot aggiornati al maggio 2026.")

# --- PANNELLO DI MODIFICA (MODIFICABILE IN APP) ---
with st.expander("📝 MODIFICA VALORI (Aggiorna qui i tuoi dati giornalieri)"):
    cols = st.columns(4)
    for i, (categoria, valori) in enumerate(st.session_state.stats.items()):
        with cols[i]:
            st.subheader(categoria)
            for sub_cat in valori:
                st.session_state.stats[categoria][sub_cat] = st.number_input(
                    f"{sub_cat} (%)", 
                    value=valori[sub_cat], 
                    key=f"{categoria}_{sub_cat}"
                )

# --- MOTORE DI CALCOLO E ANALISI ---
st.divider()
st.header("📊 Analisi Performance Reale")

col_res1, col_res2, col_res3, col_res4 = st.columns(4)

def display_stat(label, data, container):
    totale = sum(data.values())
    container.metric(label, f"{totale:.2f}%")
    # Suggerimento intelligente basato sui tuoi dati
    if totale < 60 and label == "Danno Eroe":
        container.warning("⚠️ Priorità: Alza il Boost Costruzione")
    elif totale > 80:
        container.success("✅ Statistica Eccellente")

display_stat("Attacco Totale", st.session_state.stats["Attacco Carro"], col_res1)
display_stat("Difesa Totale", st.session_state.stats["Difesa Carro"], col_res2)
display_stat("PS Totali", st.session_state.stats["PS Carro"], col_res3)
display_stat("Danno Eroe", st.session_state.stats["Danno Eroe"], col_res4)

# --- SEZIONE MIGLIORIE (IL "CERVELLO" DELL'APP) ---
st.divider()
st.header("💡 Piano d'Azione per Miglioramenti")

tab_drone, tab_tecno, tab_hero = st.tabs(["Focus Drone", "Ricerca Strategica", "Sinergia Team"])

with tab_drone:
    st.info("I tuoi dati mostrano un contributo del Drone del 15.5% sull'attacco. Per livellare con i top player, devi puntare al 20%.")
    st.write("**Azione:** Converti i componenti difesa in componenti attacco se il tuo Marshall sopravvive oltre i 30 secondi.")

with tab_tecno:
    st.success("Il tuo 'Boost Tecnologia' è solido (40%).")
    st.write("**Prossimo Step:** Concentrati sulla branca 'Unità Eroe' per sbloccare il sesto livello di riduzione danno, che al momento hai solo al 10.75%.")

with tab_hero:
    st.warning("Analisi Counter: Con il tuo 85% di attacco Carro, Kimberly è devastante. Ma se incontri un team Aereo (DVA/Schuyler), il tuo vantaggio si riduce del 20% netto.")
