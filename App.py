
import streamlit as st

st.set_page_config(
    page_title="Textile GSM Calculator",
    page_icon="🧵",
    layout="centered"
)

st.title("🧵 Textile GSM Calculator")
st.write("Calculate the GSM of fabric using sample weight and area.")

st.subheader("Enter Fabric Details")

weight = st.number_input(
    "Fabric Weight (grams)",
    min_value=0.0,
    value=1.8,
    step=0.1
)

unit = st.selectbox(
    "Select Area Unit",
    ["cm²", "m²"]
)

if unit == "cm²":
    area = st.number_input(
        "Sample Area (cm²)",
        min_value=0.0,
        value=100.0,
        step=1.0
    )
    area_m2 = area / 10000

else:
    area_m2 = st.number_input(
        "Sample Area (m²)",
        min_value=0.0,
        value=0.01,
        step=0.001
    )

if st.button("Calculate GSM"):
    if weight > 0 and area_m2 > 0:

        gsm = weight / area_m2

        st.success("Calculation Completed!")

        st.metric(
            label="Fabric GSM",
            value=f"{gsm:.2f} g/m²"
        )

    else:
        st.error("Please enter valid weight and area.")

st.subheader("GSM Formula")

st.latex(r"GSM = \frac{Weight\ (g)}{Area\ (m^2)}")

st.info(
    "Example: 1.8 g fabric sample with 100 cm² area "
    "has a GSM of 180 g/m²."
)

st.caption("Textile Engineering GSM Calculator")
