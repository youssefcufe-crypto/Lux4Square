# 💡 Lux4Square – Light Estimator Web App

*Live App:* [https://lux4square.streamlit.app/](https://lux4square.streamlit.app/)

## 📝 Overview

*Lux4Square* is a simple and practical Streamlit web application that helps estimate the required number of luminaires (lighting fixtures) in a rectangular room. It is designed to provide quick, educational-level estimates based on standard lighting formulas.

> ⚠ This tool is for *educational and preliminary design purposes only. It does **not replace professional lighting software* like DIALux Evo, nor is it suitable for complex or irregular spaces.

---

## ✅ Features

- User inputs include:
  - Room dimensions (length and width in meters)
  - Desired illuminance level (lux)
  - Utilization Factor (UF)
  - Maintenance Factor (MF)
  - Lumen output per luminaire
- Outputs the estimated number of luminaires required for the space.
- Accessible, fast, and runs entirely in the browser using Streamlit.

---

## 📌 Usage Notes

- The app assumes a rectangular room with *uniform light distribution*.
- You must provide appropriate *UF and MF values*, typically found in manufacturer datasheets or calculated via software like DIALux.
- Ceiling height, room surface reflectance, and fixture beam angle are *not* considered.
- It is meant to assist in *making faster decisions* or testing lighting ideas before committing to full simulation tools.

---

## 🧪 Technologies Used

- Python
- Streamlit

---

## 🔧 Running Locally

```bash
git clone https://github.com/your-username/Lux4Square.git
cd Lux4Square
pip install -r requirements.txt
streamlit run Lux4Square.py
