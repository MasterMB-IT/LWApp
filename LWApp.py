import streamlit as st
import pandas as pd

# --- CONFIGURAZIONE UI STILE TACTICAL ---
st.set_page_config(
    page_title="Last War Tactical Engine Pro",
    page_icon="🛡️",
    layout="wide"
)

# Design personalizzato per richiamare i colori del gioco
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .stProgress > div > div > div > div { background-color: #58a6ff; }
    h1, h2, h3 { color: #58a6ff; font-family: 'Orbitron', sans-serif; }
    .highlight-box { background-color: #23863633; border-left: 5px solid #238636; padding: 15px; border-radius: 5px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# --- INIZIALIZZAZIONE DATI (Mappatura dai tuoi Screenshot) ---
if 'data' not in st.session_state:
    st.session_state.data = {
        "Atk_Carro": {"Tecno": 40.0, "Drone": 15.5, "Onore": 2.5, "VIP": 7.5, "Cosmetici": 20.0},
        "Dif_Carro": {"Tecno": 40.0, "Drone": 13.0, "Onore": 4.0, "VIP": 7.5, "Cosmetici": 8.0},
        "PS_Carro": {"Tecno": 40.0, "Drone": 13.0, "Onore": 4.5, "VIP": 7.5, "Cosmetici": 15.0},
        "Danno_Eroe": {"Tecno": 35.0, "Drone": 9.75, "Costruzione": 7.06, "Cosmetici": 1.5},
        "Drone_Comp": {
            "Radar Precisione (Atk)": 92,
            "Sensore (Dif)": 86,
            "Processore (PS)": 87,
            "Radar (Atk)": 16,
            "Chip Memoria (Dif)": 13,
            "Motore (PS)": 25
        },
        "Flat_Stats": {"PS": 1524554, "Dif": 23839, "Atk": 24060}
    }

# --- SIDEBAR: PANNELLO DI AGGIORNAMENTO GIORNALIERO ---
with st.sidebar:
    st.title("⚙️ Pannello Comando")
    st.info("Aggiorna qui i tuoi dati man mano che cresci nel gioco.")
    
    tier_truppe = st.selectbox("Tier Truppe Attuale", ["T9", "T10", "T11 (In Progress)", "T11 Unlock"])
    
    with st.expander("📝 Modifica Bonus %"):
        for cat, vals in st.session_state.data.items():
            if isinstance(vals, dict) and "Comp" not in cat:
                st.subheader(cat.replace("_", " "))
                for k in vals:
                    st.session_state.data[cat][k] = st.number_input(f"{k} %", value=vals[k], key=f"{cat}_{k}")

# --- DASHBOARD PRINCIPALE ---
st.title("🛡️ Last War: Tactical Optimizer Pro")
st.markdown("### Configurazione End-Game: Transizione T11")

# --- RIGA 1: STATISTICHE REALI ---
st.header("📊 Analisi Buff Totali")
c1, c2, c3, c4 = st.columns(4)

def get_total(key):
    return sum(st.session_state.data[key].values())

c1.metric("Attacco Carro", f"+{get_total('Atk_Carro'):.2f}%")
c2.metric("Difesa Carro", f"+{get_total('Dif_Carro'):.2f}%")
c3.metric("PS Carro", f"+{get_total('PS_Carro'):.2f}%")
c4.metric("Danno Eroe", f"+{get_total('Danno_Eroe'):.2f}%")

# --- RIGA 2: DRONE & TECNOLOGIA ---
st.divider()
col_left, col_right = st.columns(2)

with col_left:
    st.header("🛸 Drone Tactical Analyzer (Lv. 180)")
    st.write("Stato Componenti Livello 9:")
    for comp, prog in st.session_state.data["Drone_Comp"].items():
        st.write(f"**{comp}** ({prog}%)")
        st.progress(prog / 100)
    
    if st.session_state.data["Drone_Comp"]["Radar (Atk)"] < 20:
        st.warning("⚠️ **Focus Radar**: Il Radar secondario è molto basso (16%). Questo penalizza il tuo DPS totale rispetto al potenziale delle T11.")

with col_right:
    st.header("⚔️ Simulatore Scontro T11")
    st.markdown("""
        Il passaggio alle **T11** attiva la **Soppressione Tier**. 
        Il calcolo del danno finale sarà influenzato dal tuo Bonus Danno Eroe attuale (+53.31%).
    """)
    
    enemy_tier = st.radio("Scegli Tier Nemico per simulazione:", ["T10", "T11"])
    
    # Logica di calcolo semplificata
    soppressione = 0.15 if (tier_truppe == "T11 Unlock" and enemy_tier == "T10") else 0
    power_mult = (get_total("Atk_Carro") / 100) + (get_total("Danno_Eroe") / 100) + soppressione
    
    st.metric("Moltiplicatore Danno Finale Stimato", f"x{1 + power_mult:.2f}")
    
    st.markdown("<div class='highlight-box'>", unsafe_allow_html=True)
    st.write("💡 **Consiglio AI Strategico:**")
    if get_total("PS_Carro") < 85:
        st.write("Le tue T11 saranno dei cannoni di vetro. Priorità: Alza la Ricerca 'Unità Eroe' per portare i PS Carro sopra il 90%.")
    else:
        st.write("Bilanciamento ottimo. Concentrati sull'Arma Esclusiva di Stetmann al 30 per massimizzare il buff T11.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TABELLA DETTAGLIATA ---
with st.expander("🔍 Vedi Tabella Dettagliata Fonti"):
    df = pd.DataFrame(st.session_state.data).T
    st.table(df)

st.divider()
st.caption("Last War Tactical Engine | Sviluppato per Account High-End | Versione Maggio 2026")
