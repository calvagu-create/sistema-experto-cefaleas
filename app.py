import streamlit as st
from datetime import datetime

# Configuración de la ventana
st.set_page_config(
    page_title="Consulta: Fiebre y Dolor de Cabeza", 
    page_icon="🩺", 
    layout="wide"
)

st.title("🩺 Consultorio Virtual: Fiebre y Dolor de Cabeza")
st.write("Ingrese únicamente los datos de su fiebre y el tipo de dolor de cabeza para generar la boleta de diagnóstico y remedios caseros.")
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

    st.subheader("🤒 1. Fiebre")
    temperatura = st.slider("Temperatura corporal registrada (°C):", min_value=35.5, max_value=40.5, value=38.4, step=0.1)

    st.subheader("🧠 2. Dolor de Cabeza")
    tipo_dolor = st.radio("¿Dónde y cómo siente el dolor de cabeza?", [
        "Dolor profundo detrás de los ojos (Retroocular)",
        "Pesadez y opresión en la frente o senos paranasales"
    ])
    intensidad = st.slider("Intensidad del dolor (1 al 10):", 1, 10, 7)

    # BOTÓN ÚNICO DE EJECUCIÓN
    btn_analizar = st.button("📄 Generar Boleta Médica", type="primary", use_container_width=True)

with col_boleta:
    st.subheader("🧾 Boleta de Atención Médica")
    
    if btn_analizar:
        fecha_emision = datetime.now().strftime("%d/%m/%Y %H:%M")
        tiene_fiebre = temperatura >= 38.0

        # LÓGICA EXCLUSIVA PARA FIEBRE Y DOLOR DE CABEZA
        if tipo_dolor == "Dolor profundo detrás de los ojos (Retroocular)":
            dx = "1. Síndrome Febril Viral / Sospecha de Dengue"
            analisis = "Presenta la combinación característica de fiebre acompañada de dolor de cabeza centrado detrás de los ojos (retroocular). Se requiere reposo e hidratación intensiva."
            cuidados = [
                "**Infusión 'Triple Alivio':** Preparar un té bien caliente con kión (jengibre) machacado, hojas de toronjil o manzanilla, jugo de 1 limón y 1 cucharada de miel. Beberlo antes de dormir para bajar la fiebre y calmar el dolor corporal.",
                "**Compresas de agua tibia:** Colocar paños húmedos a temperatura ambiente en la frente y axilas para regular la temperatura gradualmente.",
                "**Hidratación abundante:** Tomar entre 2.5 y 3 litros de agua de coco, suero casero o caldos de pollo sin grasa al día.",
                "**Reposo absoluto:** Guardar reposo en cama de 3 a 5 días sin realizar esfuerzos físicos.",
                "**Alimentación blanda:** Consumir frutas ricas en agua (sandía, melón) y alimentos de fácil digestión."
            ]

        else:
            dx = "2. Resfriado Febril / Infección Respiratoria Aguda"
            analisis = "Presenta aumento de temperatura corporal acompañado de dolor de cabeza pesado u opresivo en la zona frontal. Cuadro febril común que cede con calor térmico y descanso."
            cuidados = [
                "**Vaporizaciones de Eucalipto y Menta:** Hervir 1 litro de agua con hojas de eucalipto o menta e inhalar el vapor cubriéndose la cabeza con una toalla durante 10 minutos para descongestionar y aliviar la pesadez en la frente.",
                "**Té de Limón con Miel:** Beber infusión caliente de limón con miel 3 veces al día para reconfortar el cuerpo.",
                "**Descanso prolongado:** Dormir de 8 a 10 horas seguidas manteniendo el cuerpo y los pies abrigados.",
                "**Alimentación reconfortante:** Consumir caldos calientes y jugos de frutas cítricas ricos en Vitamina C."
            ]

        # RENDERIZADO NATIVO LIMPIO (SIN CÓDIGO HTML VISIBLE)
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

            st.markdown("#### 🍵 Remedios Caseros y Indicaciones")
            for c in cuidados:
                st.markdown(f"- {c}")

            st.divider()
            st.caption("____________________________________________________")
            st.caption("**Firma y Sello del Médico Especialista**")
            st.caption("Consulta Virtual de Cabecera")

    else:
        st.info("👈 Registre su medición de fiebre y tipo de dolor de cabeza a la izquierda, y presione el botón **'Generar Boleta Médica'**.")
