import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Consulta Médica - Triaje Infectológico", page_icon="🩺", layout="wide")

# Estilo visual de la boleta estilo Ticket Médico
st.markdown("""
<style>
    .ticket-medico {
        border: 2px dashed #1b4d2e;
        background-color: #fcfdfe;
        padding: 25px;
        border-radius: 8px;
        font-family: 'Courier New', Courier, monospace;
        color: #111;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        max-width: 600px;
        margin: auto;
    }
    .ticket-header {
        text-align: center;
        border-bottom: 2px dashed #1b4d2e;
        padding-bottom: 12px;
        margin-bottom: 15px;
    }
    .ticket-seccion {
        margin-top: 15px;
        border-bottom: 1px dashed #ccc;
        padding-bottom: 10px;
    }
    .ticket-titulo {
        font-weight: bold;
        color: #1b4d2e;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

st.title("🩺 Consulta Médica Virtual - Infectología")
st.write("Complete sus síntomas para que el especialista analice su caso y genere su boleta de atención.")
st.markdown("---")

col_input, col_output = st.columns([1, 1], gap="large")

with col_input:
    st.subheader("📋 Ingreso de Datos y Síntomas")
    
    nombre = st.text_input("Nombre y Apellidos del Paciente:", value="Juan Pérez")
    c1, c2 = st.columns(2)
    with c1:
        edad = st.number_input("Edad:", min_value=1, max_value=110, value=30)
    with c2:
        genero = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
        
    temperatura = st.slider("Temperatura corporal (°C):", min_value=35.0, max_value=41.0, value=38.4, step=0.1)
    
    st.write("**Banderas Rojas / Alarma:**")
    rigidez_nuca = st.checkbox("Rigidez de nuca / Dificultad para doblar el cuello")
    alteracion_conciencia = st.checkbox("Confusión o somnolencia marcada")
    petequias = st.checkbox("Manchas o puntos rojos/morados en la piel")
    
    st.write("**Detalle del Dolor y Síntomas:**")
    tipo_dolor = st.selectbox("Tipo de dolor de cabeza:", [
        "Retroocular (Detrás de los ojos)",
        "Pulsátil (Latidos en un lado o toda la cabeza)",
        "Opresivo o difuso",
        "Sin dolor significativo"
    ])
    dolor_muscular = st.checkbox("Dolores musculares/articulares intensos")
    sintomas_respiratorios = st.checkbox("Tos o dolor de garganta")
    
    # BOTÓN PARA GENERAR LA BOLETA
    btn_generar = st.button("📄 Emitir Boleta de Consulta Médica", use_container_width=True, type="primary")

with col_output:
    st.subheader("🧾 Comprobante / Receta Médica")
    
    if btn_generar:
        # Lógica del Motor de Inferencia
        tiene_fiebre = temperatura >= 38.0
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        if rigidez_nuca or alteracion_conciencia or petequias:
            dx = "SOSPECHA DE MENINGITIS / SEPSIS ACUDA"
            prioridad = "CRÍTICA - EMERGENCIA HOSPITALARIA"
            rx = "NO ADMINISTRAR MEDICACIÓN VÍA ORAL EN CASA."
            plan = "Acudir inmediatamente al centro hospitalario más cercano para evaluación urgente por infectología."
        elif tiene_fiebre and tipo_dolor == "Retroocular (Detrás de los ojos)" and dolor_muscular:
            dx = "SÍNDROME FEBRIL COMPATIBLE CON DENGUE (ARBOVIROSIS)"
            prioridad = "ALTA - CONTROL MÉDICO Y LABORATORIO"
            rx = "Paracetamol 500mg (1 tab c/6 horas si hay fiebre).\n🚫 CONTRAINDICADO: Ibuprofeno, Aspirina o Naproxeno."
            plan = "1. Hidratación oral abundante (2.5L de suero oral/agua).\n2. Realizar Hemograma (Plaquetas) y prueba NS1.\n3. Reposo absoluto en cama."
        elif tiene_fiebre and sintomas_respiratorios:
            dx = "INFECCIÓN RESPIRATORIA AGUDA / SÍNDROME GRIPAL"
            prioridad = "MODERADA - ATENCIÓN AMBULATORIA"
            rx = "Paracetamol 500mg cada 8 horas en caso de molestia."
            plan = "1. Isolation preventivo en hogar.\n2. Ingesta abundante de líquidos tibios.\n3. Monitoreo por 48 horas."
        else:
            dx = "SÍNDROME FEBRIL EN ESTUDIO"
            prioridad = "OBSERVACIÓN"
            rx = "Paracetamol 500mg si la temperatura excede los 38.0°C."
            plan = "1. Control de temperatura cada 4 horas.\n2. Mantener hidratación adecuada."

        # RENDERIZADO DE LA BOLETA TIPO TICKET
        st.markdown(f"""
        <div class="ticket-medico">
            <div class="ticket-header">
                <h3>🏥 CLÍNICA VIRTUAL DE INFECTOLOGÍA</h3>
                <p><strong>COMPROBANTE DE ATENCIÓN Y RECETA MÉDICA</strong></p>
                <p><small>Fecha de Emisión: {fecha_actual}</small></p>
            </div>
            
            <div>
                <p><strong>PACIENTE:</strong> {nombre.upper()}</p>
                <p><strong>EDAD / GÉNERO:</strong> {edad} años | {genero}</p>
                <p><strong>TEMP. REGISTRADA:</strong> {temperatura} °C</p>
            </div>
            
            <div class="ticket-seccion">
                <p class="ticket-titulo">📌 DIAGNÓSTICO DEL DOCTOR:</p>
                <p><strong>{dx}</strong></p>
                <p><em>Triaje: {prioridad}</em></p>
            </div>
            
            <div class="ticket-seccion">
                <p class="ticket-titulo">💊 PRESCRIPCIÓN MÉDICA:</p>
                <p>{rx.replace('\n', '<br>')}</p>
            </div>
            
            <div class="ticket-seccion">
                <p class="ticket-titulo">📝 RECOMENDACIONES Y CONDUCTA:</p>
                <p>{plan.replace('\n', '<br>')}</p>
            </div>
            
            <br>
            <div style="text-align: center;">
                <p>___________________________________</p>
                <p><strong>Firma y Sello del Especialista</strong></p>
                <p><small>Infectología y Medicina Tropical</small></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("👈 Ingrese los síntomas del paciente y presione el botón **'Emitir Boleta de Consulta Médica'** para generar el reporte.")
