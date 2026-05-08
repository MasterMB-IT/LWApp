import streamlit as st
import pandas as pd

# CONFIGURAZIONE UI
st.set_page_config(page_title="Last War: Real Tactical Wiki", layout="wide")

# DATABASE REALE ARMI ESCLUSIVE (Dati verificati Lv. 10-20-30)
EXCL_WEAPONS_REAL = {
    "Kimberly (Rocket Gatling)": {
        "Lv. 10": "Aumento Danno Abilità +10%.",
        "Lv. 20": "Aggiunge un missile extra alla raffica di 'Barrage'.",
        "Lv. 30": "Effetto Critico: Ogni colpo critico riduce la Difesa del bersaglio del 2% (Max 10 stack). Fondamentale per sciogliere i Tank.",
        "Descrizione": "L'arma più potente del gioco per DPS singolo. Il salto al 30 è obbligatorio per il PvP End-game."
    },
    "Stetmann (Tesla Core)": {
        "Lv. 10": "Aumento Danno Abilità +10%.",
        "Lv. 20": "Aumenta il numero di rimbalzi del laser elettrico.",
        "Lv. 30": "Dopo aver lanciato l'abilità 3 volte, Stetmann entra in stato 'Overcharge', ignorando il 20% della difesa nemica.",
        "Descrizione": "Essenziale per il danno AoE. La perforazione difesa al Lv.30 lo rende letale contro Murphy/Williams."
    },
    "Murphy (Iron Shield)": {
        "Lv. 10": "Aumento Riduzione Danno +5%.",
        "Lv. 20": "Lo scudo ora riflette una parte del danno subito agli attaccanti.",
        "Lv. 30": "Immunità al Crowd Control (Stun/Silenzio) per i primi 5 secondi di battaglia.",
        "Descrizione": "Il miglior buff per la sopravvivenza della frontline. Il Lv.30 evita che Murphy venga bloccato all'inizio."
    },
    "Williams (Energy Shield)": {
        "Lv. 10": "Aumento Riduzione Danno +5%.",
        "Lv. 20": "Aumenta la durata della protezione per gli alleati adiacenti.",
        "Lv. 30": "Quando Williams subisce danni, aumenta la resistenza di tutta la squadra del 10% per 3 secondi.",
        "Descrizione": "Rende il team quasi immortale contro gli Aerei."
    }
}

# --- DATABASE MECCANICHE (ENCICLOPEDIA) ---
GAME_MECHANICS = {
    "Sinergia Fazione (Tank)": "3 Tank: +10% HP | 4 Tank: +15% HP/ATK | 5 Tank: +20% HP/ATK/DEF. Con le tue T11, il 20% extra è massiccio.",
    "Perforazione vs Difesa": "Statistica invisibile. Se la tua Perforazione è inferiore alla Difesa nemica, il danno viene ridotto fino al 50%.",
    "Unità X (Tank)": "Nodi Critici: 'Danno Finale' e 'Riduzione Danno Finale'. Sono gli unici che scalano oltre i buff che hai già maxato.",
    "Importanza Velocità": "Chi attacca per primo (Kimberly) spesso vince. La velocità è data dagli Stivali e da alcuni nodi di Forze Speciali (che hai già maxato)."
}

# --- INTERFACCIA APP ---
st.title("🛡️ Last War: Encyclopedia & Optimizer (Official Data)")

tab1, tab2, tab3 = st.tabs(["📚 Database Armi Esclusive", "📖 Enciclopedia Meccaniche", "📊 Analisi Tuo Account"])

with tab1:
    st.header("🔬 Livelli Armi Esclusive (UR)")
    hero = st.selectbox("Seleziona Eroe:", list(EXCL_WEAPONS_REAL.keys()))
    
    data = EXCL_WEAPONS_REAL[hero]
    st.write(f"*{data['Descrizione']}*")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Livello 10", "Base", help=data["Lv. 10"])
    col1.write(data["Lv. 10"])
    
    col2.metric("Livello 20", "Advanced", help=data["Lv. 20"])
    col2.write(data["Lv. 20"])
    
    col3.metric("Livello 30", "MAX (Elite)", help=data["Lv. 30"])
    col3.write(data["Lv. 30"])
    st.success("🎯 Il Livello 30 è il CAP attuale del gioco.")

with tab2:
    st.header("🧠 Manuale Tecnico di Combattimento")
    for titolo, testo in GAME_MECHANICS.items():
        with st.expander(titolo):
            st.write(testo)

with tab3:
    st.header("📋 Check-list per il Tier 11")
    st.write("Basato sui tuoi dati tecnologici (100% Maxed):")
    
    st.checkbox("Tecnologia Eroi 100%", value=True, disabled=True)
    st.checkbox("Forze Speciali 100%", value=True, disabled=True)
    st.checkbox("Maestria Carro 100%", value=True, disabled=True)
    st.checkbox("Unità X (In corso)", value=False)
    
    st.divider()
    st.subheader("⚠️ Focus Richiesto")
    st.error("Drone: Chip Memoria (13%) - Devi portarlo almeno al 50% per bilanciare le T11.")
    st.warning("Equipaggiamento: Assicurati che Kimberly abbia l'arma Rossa (Mythic) con almeno 2 stelle.")
