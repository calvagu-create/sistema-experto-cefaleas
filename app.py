import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Consultorio Virtual: Fiebre y Cefalea", 
    page_icon="🩺", 
    layout="wide"
)

st.title("🩺 Consultorio Médico Virtual de Cabecera")
st.write("Herramienta de análisis clínico rápido para afecciones febriles y dolor de cabeza.")
st.markdown("---")

col_entradas, col_boleta = st.columns([1, 1.1], gap="large")

with col_entradas:
    st.subheader("📋 Datos del Paciente")
    nombre_paciente = st.text_input("Nombre completo del paciente:", value="Juan Pérez")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        edad = st.number_input("Edad (años):", min_value=1, max_value=110, value=28)
    with col_e2:
        genero = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
        
    temperatura = st.slider("Temperatura corporal (°C):", min_value=35.5, max_value=40.5, value=38.4, step=0.1)

    st.subheader("🧠 Síntomas del Dolor de Cabeza (Cefalea)")
    tipo_dolor = st.radio("Seleccione las características del dolor de cabeza:", [
        "Dolor profundo detrás de los ojos (Retroocular)",
        "Dolor de pesadez y presión en la frente o senos paranasales",
        "Sin dolor de cabeza significativo"
    ])
    intensidad = st.slider("Intensidad del dolor de cabeza (1 al 10):", 1, 10, 6)

    st.subheader("🤒 Síntomas Acompañantes de la Fiebre")
    s_mialgias = st.checkbox("Dolores fuertes en músculos y articulaciones ('cuerpo cortado / rompehuesos')")
    s_respiratorio = st.checkbox("Tos, estornudos, dolor de garganta o congestión nasal")
    s_escalofrios = st.checkbox("Escalofríos, sudoración y cansancio severo")
    s_ojos_rojos = st.checkbox("Enrojecimiento en los ojos o molestia suave a la luz")

    btn_analizar = st.button("📄 Generar Boleta de Diagnóstico y Tratamiento", type="primary", use_container_width=True)

with col_boleta:
    st.subheader("🧾 Boleta de Atención Médica Virtual")
    
    if btn_analizar:
        fecha_emision = datetime.now().strftime("%d/%m/%Y %H:%M")
        tiene_fiebre = temperatura >= 38.0

        # Reglas de decisión limitadas únicamente a 2 enfermedades
        if tiene_fiebre and (tipo_dolor == "Dolor profundo detrás de los ojos (Retroocular)" or s_mialgias):
            dx = "1. Dengue / Síndrome Febril Tropico-Viral"
            analisis = "Cuadro febril caracterizado por dolor de cabeza concentrado detrás de los ojos y malestar muscular/articular. Requiere hidratación intensiva y descanso estricto."
            cuidados = [
                "**Brebaje 'Triple Alivio':** Preparar una infusión caliente con kión (jengibre) machacado, hojas de toronjil o manzanilla, el jugo de 1 limón fresco y 1 cucharada de miel. Beberlo bien caliente antes de acostarse para reducir el dolor corporal y promover la sudoración natural.",
                "**Compresas tibias para la fiebre:** Colocar paños limpios húmedos con agua a temperatura ambiente en la frente, axilas e ingle para regular la temperatura gradualmente.",
                "**Hidratación constante:** Tomar entre 2.5 y 3 litros diarios de agua de coco, suero casero, sopas o caldos de pollo sin grasa.",
                "**Reposo absoluto:** Guardar reposo en cama de 3 a 5 días evitando realizar esfuerzos físicos.",
                "**Alimentación blanda:** Consumir frutas ricas en agua (sandía, melón) y alimentos ligeros fáciles de digerir."
            ]

        else:
            dx = "2. Resfriado Febril / Infección Respiratoria Aguda"
            analisis = "Proceso infeccioso febril acompañado de molestia respiratoria o presión frontal. Es un cuadro viral común que cede con cuidados térmicos y reposo."
            cuidados = [
                "**Vaporización de Eucalipto y Menta:** Hervir 1 litro de agua con hojas de eucalipto o menta, colocar el recipiente en la mesa e inhalar el vapor cubriéndose la cabeza con una toalla durante 10 minutos antes de dormir para descongestionar y calmar la pesadez en la cabeza.",
                "**Té reconfortante de Limón y Miel:** Beber infusión caliente de té con limón y miel 3 veces al día para aliviar la garganta y reponer líquidos.",
                "**Descanso reparador:** Dormir de 8 a 10 horas seguidas manteniendo el pecho y los pies adecuadamente abrigados.",
                "**Nutrición rica en Vitamina C:** Consumir naranjas, mandarinas y caldos calientes nutritivos durante el período de recuperación."
            ]

        # Renderizado limpio utilizando componentes nativos de Streamlit (Sin código HTML expuesto)
        container_boleta = st.container(border=True)
        with container_boleta:
            st.markdown("### 🏥 CONSULTORIO MÉDICO VIRTUAL DE CABECERA")
            st.markdown("**BOLETA DE ATENCIÓN Y RECETA DE CUIDADOS**")
            st.caption(f"Fecha de emisión: {fecha_emision}")
            st.divider()

            st.write(f"**PACIENTE:** {nombre_paciente.upper()}")
            st.write(f"**EDAD / GÉNERO:** {edad} años | {genero}")
            st.write(f"**TEMPERATURA:** {temperatura} °C")
            st.divider()

            st.markdown("#### 📌 Diagnóstico Médico Presuntivo")
            st.success(f"**{dx}**")
            st.info(f"_{analisis}_")
            st.divider()

            st.markdown("#### 🍵 Plan de Remedios Caseros y Recomendaciones")
            for c in cuidados:
                st.markdown(f"- {c}")

            st.divider()
            st.caption("____________________________________________________")
            st.caption("**Firma y Sello del Médico de Cabecera**")
            st.caption("Atención Virtual e Inferencia Clínica")

    else:
        st.info("👈 Seleccione los síntomas en el panel izquierdo y presione el botón **'Generar Boleta de Diagnóstico y Tratamiento'** para emitir su comprobante.")
