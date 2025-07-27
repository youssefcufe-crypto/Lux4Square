import streamlit as st
import math

# --- Function to auto-select UF ---
def get_uf_from_room_index(ri):
    if ri < 0.75:
        return 0.40
    elif ri < 1.00:
        return 0.45
    elif ri < 1.25:
        return 0.50
    elif ri < 1.50:
        return 0.55
    elif ri < 2.00:
        return 0.60
    elif ri < 2.50:
        return 0.65
    elif ri < 3.00:
        return 0.70
    else:
        return 0.75

# --- App Title ---
st.title("💡 Lighting Target Estimator (for DIALux planning)")
st.markdown("Use this tool for quick planning before jumping into DIALux.")

# --- Inputs ---
st.header("📐 Room Parameters")
length = st.number_input("Room Length (m)", min_value=1.0, value=5.0)
width = st.number_input("Room Width (m)", min_value=1.0, value=4.0)
height = st.number_input("Room Height (m)", min_value=2.0, value=3.0)
working_plane = st.number_input("Working Plane Height (m)", min_value=0.0, value=0.8)

st.header("💡 Lighting Inputs")
num_luminaires = st.number_input("Number of Luminaires", min_value=1, value=4)
lumen_per_luminaire = st.number_input("Lumen Output per Luminaire", min_value=100.0, value=3000.0)
target_lux = st.number_input("Target Illuminance (lux)", min_value=100.0, value=500.0)
mf = st.number_input("Maintenance Factor (0.7 - 0.9 typical)", min_value=0.1, max_value=1.0, value=0.8)

# --- Calculations ---
area = length * width
hm = height - working_plane
room_index = (length * width) / (hm * (length + width))
auto_uf = get_uf_from_room_index(room_index)

# --- Manual UF Option ---
st.header("⚙ Utilization Factor (UF) Override")
manual_uf_enabled = st.checkbox("Enter UF manually?", value=False)

if manual_uf_enabled:
    uf = st.number_input("Manual Utilization Factor (UF)", min_value=0.1, max_value=1.0, value=auto_uf, step=0.01)
else:
    uf = auto_uf

# --- Final Calculations ---
raw_lumen = num_luminaires * lumen_per_luminaire
effective_lumen = raw_lumen * uf * mf
average_lux = effective_lumen / area
needed_luminaires = (target_lux * area) / (lumen_per_luminaire * uf * mf)

# --- Results ---
st.header("📊 Results")
st.write(f"Room Area: {area:.2f} m²")
st.write(f"Room Index (RI): {room_index:.2f}")
st.write(f"Auto-selected UF: {auto_uf:.2f}")
st.write(f"UF Used in Calculation: {uf:.2f}")
st.write(f"Total Raw Lumen Output: {raw_lumen:.2f} lm")
st.write(f"Effective Lumen (UF & MF adjusted): {effective_lumen:.2f} lm")
st.write(f"Average Illuminance: {average_lux:.2f} lux")

if average_lux >= target_lux:
    st.success("✅ Target Achieved!")
else:
    st.error("❌ Target Not Met")
    st.write(f"👉 Suggested Luminaires Needed: {math.ceil(needed_luminaires)} luminaires")

st.markdown("---")
st.caption("Built by Youssef's Assistant 🔧 For early planning before DIALux Evo.")