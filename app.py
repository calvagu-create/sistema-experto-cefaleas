import streamlit as st
from datetime import datetime

# Configuración de la aplicación
st.set_page_config(
    page_title="Consultorio: Fiebre y Dolor de Cabeza", 
    page_icon="🩺", 
    layout="wide"
)

st.title("🩺 Consultorio Virtual: Fiebre y Dolor de Cabeza")
st.write("Seleccione los síntomas específicos de su afección para generar el análisis y la boleta con las recomendaciones.")
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

    st.subheader("🤒 1. Evaluación de la Fiebre")
    temperatura = st.slider("Temperatura corporal registrada (°C):", min_value=35.5, max_value=40.5, value=38.4, step=0.1)
    
    st.write("**Manifestaciones de la fiebre:**")
    f_escalofrios = st.checkbox("Escalofríos intensos y sudoración nocturna")
    f_ardor_ojos = st.checkbox("Sensación de calor facial y ardor en los ojos")
    f_cansancio = st.checkbox("Sensación de 'cuerpo cortado' y fatiga severa")

    st.subheader("🧠 2. Características del Dolor de Cabeza")
    tipo_dolor = st.radio("¿Cómo y dónde siente el dolor?", [
        "Dolor profundo detrás de los ojos (Retroocular)",
        "Pesadez y opresión en la frente / senos paranasales",
        "Dolor pulsátil (latidos) en sienes o un solo lado",
        "Sensación de banda / casco apretado en toda la cabeza"
    ])
    intensidad = st.slider("Intensidad del dolor (1 al 10):", 1, 10, 7)

    st.subheader("🌿 3. Síntomas Acompañantes")
    s_mialgias = st.checkbox("Dolores fuertes en músculos y articulaciones")
    s_respiratorio = st.checkbox("Tos, congestión nasal o dolor al tragar")

    btn_analizar = st.button("📄 Generar Boleta Médica", type="primary", use_container_width=True)

with col_boleta:
    st.subheader("🧾 Boleta de Atención Médica")
    
    if btn_analizar:
        fecha_emision = datetime.now().strftime("%d/%m/%Y %H:%M")
        tiene_fiebre = temperatura >= 38.0

        # Motor de decisiones simplificado
        if tipo_dolor == "Dolor profundo detrás de los ojos (Retroocular)" or (tiene_fiebre and s_mialgias and f_ardor_ojos):
            dx = "1. Síndrome Febril Viral / Sospecha de Dengue"
            analisis = "Presenta fiebre elevada acompañada de dolor retroocular y mialgias intensas. Requiere hidratación activa y reposo en cama."
            cuidados = [
                "**Infusión 'Triple Alivio':** Preparar un té caliente de kión (jengibre) machacado, hojas de toronjil o manzanilla, jugo de 1 limón y 1 cucharada de miel. Tomarlo antes de dormir para bajar la fiebre y calmar el dolor articular.",
                "**Compresas de agua tibia:** Aplicar paños húmedos a temperatura ambiente en la frente y axilas para regular la temperatura.",
                "**Hidratación abundante:** Beber de 2.5 a 3 litros de agua de coco, suero casero o caldos sin grasa al día.",
                "**Reposo absoluto:** Guardar reposo en cama de 3 a 5 días."
            ]

        else:
            dx = "2. Resfriado Febril / Infección Respiratoria Aguda"
            analisis = "Cuadro febril con molestia frontal/sinusal o síntomas respiratorios. Responde bien al tratamiento térmico e infusiones."
            cuidados = [
                "**Vaporización de Eucalipto y Menta:** Inhalar el vapor de 1 litro de agua hirviendo con hojas de eucalipto o menta durante 10 minutos para descongestionar y aliviar la presión de la cabeza.",
                "**Té de Limón con Miel:** Tomar infusión caliente de limón con miel 3 veces al día.",
                "**Descanso y Abrigo:** Dormir de 8 a 10 horas seguidas manteniendo el cuerpo y los pies bien abrigados.",
                "**Nutrición rica en Vitamina C:** Consumir caldos calientes y frutas cítricas."
            ]

        # Contenedor nativo de Streamlit
        container_boleta = st.container(border=True)
        with container_boleta:
            st.markdown("### 🏥 CONSULTORIO MÉDICO VIRTUAL")
            st.markdown("**BOLETA DE ATENCIÓN Y RECOMENDACIONES**")
            st.caption(f"Fecha de emisión: {fecha_emision}")
            st.divider()

            st.write(f"**PACIENTE:** {nombre_paciente.upper()}")
            st.write(f"**EDAD / GÉNERO:** {edad} años | {genero}")
            st.write(f"**TEMPERATURA:** {temperatura} °C")
            st.write(f"**INTENSIDAD DEL DOLOR:** {intensidad} / 10")
            st.divider()

            st.markdown("#### 📌 Diagnóstico Presuntivo")
            st.success(f"**{dx}**")
            st.info(f"_{analisis}_")
            st.divider()

            st.markdown("#### 🍵 Recomendaciones")
            for c in cuidados:
                st.markdown(f"- {c}")

            st.divider()
            st.caption("____________________________________________________")
            st.caption("**Firma y Sello del Médico Especialista**")
            st.caption("Consulta Virtual de Cabecera")

    else:
        st.info("👈 Seleccione los síntomas en el panel izquierdo y presione el botón **'Generar Boleta Médica'**.")
