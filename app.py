import streamlit as st

# Configuración inicial del entorno
st.set_page_config(
    page_title="SE Infectología: Fiebre y Cefalea", 
    page_icon="🩺", 
    layout="wide"
)

# Encabezado con la delimitación de la especialidad
st.title("🩺 Sistema Experto de Triaje e Infecciones Agudas")
st.markdown("**Especialidad Delimitada:** Infectología y Medicina Tropical")
st.caption("Evaluación clínica rápida de Síndrome Febril Agudo y Cefaleas Infecciosas mediante motor de inferencia.")
st.markdown("---")

col_entradas, col_salidas = st.columns([1, 1], gap="large")

with col_entradas:
    st.header("📋 Entrada de Datos y Síntomas Clínicos")
    
    with st.expander("👤 1. Parámetros Generales y Signos Vitales", expanded=True):
        edad = st.number_input("Edad del paciente (años):", min_value=1, max_value=110, value=25)
        temperatura = st.slider("Temperatura corporal (°C):", min_value=35.0, max_value=41.0, value=38.4, step=0.1)
        pas = st.number_input("Presión Arterial Sistólica (mmHg):", min_value=50, max_value=200, value=110)

    with st.expander("🚨 2. Evaluador de Signos de Alarma (Red Flags)", expanded=True):
        rigidez_nuca = st.checkbox("Rigidez de nuca / Dificultad para doblar el cuello hacia el pecho")
        alteracion_conciencia = st.checkbox("Confusión, desorientación o somnolencia extrema")
        petequias = st.checkbox("Puntos o manchas rojas/moradas en la piel (Petequias)")
        dificultad_respirar = st.checkbox("Dificultad respiratoria severa o dolor torácico")

    with st.expander("🧠 3. Caracterización de Cefalea y Síntomas Acompañantes", expanded=True):
        intensidad_dolor = st.select_slider("Intensidad del dolor de cabeza (1 al 10):", options=list(range(1, 11)), value=7)
        ubicacion_dolor = st.selectbox("Localización/Tipo de Dolor:", [
            "Retroocular (Detrás o alrededor de los ojos)",
            "Pulsátil (Latidos en un lado o toda la cabeza)",
            "Opresivo / Difuso generalizado",
            "Sin dolor de cabeza significativo"
        ])
        
        c1, c2 = st.columns(2)
        with c1:
            dolor_muscular = st.checkbox("Dolores musculares o articulares intensos (Mialgias)")
            nauseas = st.checkbox("Náuseas o vómitos recurrentes")
        with c2:
            sintomas_respiratorios = st.checkbox("Tos, dolor de garganta o congestión nasal")
            fotofobia = st.checkbox("Sensibilidad molesta a la luz (Fotofobia)")

# Motor de Inferencia (Base de Reglas IF-THEN)
def motor_inferencia():
    tiene_fiebre = temperatura >= 38.0
    hipotension = pas < 90

    # REGLA 0: Emergencia Infectológica / Meningitis o Sepsis
    if rigidez_nuca or alteracion_conciencia or petequias or dificultad_respirar or hipotension:
        return {
            "diagnostico": "Urgencia Infectológica: Posible Meningitis, Neuroinfección o Sepsis",
            "triaje": "NIVEL CRÍTICO - ATENCIÓN INMEDIATA EN URGENCIAS",
            "justificacion": "Presencia de signos de alarma neurológicos o sistémicos que requieren descarte inmediato de infección grave del sistema nervioso central.",
            "plan": [
                "Traslado inmediato al servicio de emergencias hospitalario.",
                "Evaluación prioritaria para punción lumbar y cultivos.",
                "Evitar la administración de alimentos o medicamentos por vía oral si hay confusión."
            ],
            "alerta": "⚠️ Riesgo de deterioro neurológico o shock infeccioso.",
            "color": "error"
        }

    # REGLA 1: Dengue / Arbovirosis Tropical
    if tiene_fiebre and ubicacion_dolor == "Retroocular (Detrás o alrededor de los ojos)" and dolor_muscular:
        return {
            "diagnostico": "Cuadro Compatible con Dengue u otra Arbovirosis Tropical",
            "triaje": "NIVEL 1 - PRIORIDAD MÉDICA Y LABORATORIO",
            "justificacion": "Tríada infecciosa clásica: Fiebre alta, dolor retroocular y mialgias/artralgias intensas.",
            "plan": [
                "Solicitar Hemograma completo (conteo de plaquetas y hematocrito) y prueba antígeno NS1 / Serología.",
                "Hidratación oral abundante con suero oral (2 a 3 litros al día).",
                "Vigilar la aparición de signos de alarma de Dengue grave (sangrado de encías, dolor abdominal severo)."
            ],
            "alerta": "🚫 CONTRAINDICACIÓN: NO administrar Ibuprofeno, Aspirina ni AINEs por riesgo de hemorragia.",
            "color": "warning"
        }

    # REGLA 2: Infección Respiratoria Aguda Febril
    if tiene_fiebre and sintomas_respiratorios:
        return {
            "diagnostico": "Infección Respiratoria Aguda Febril / Síndrome Gripal",
            "triaje": "NIVEL 2 - CONSULTA AMBULATORIA",
            "justificacion": "Cuadro febril focalizado en vías respiratorias superiores (tos, inflamación de garganta).",
            "plan": [
                "Reposo y aislamiento respiratorio preventivo en el hogar.",
                "Uso de antitérmicos habituales bajo indicación médica (ej. Paracetamol).",
                "Hidratación abundante y uso de mascarilla."
            ],
            "alerta": "Consultar a un médico si la fiebre persiste más de 72 horas o si aparece dificultad respiratoria.",
            "color": "info"
        }

    # REGLA 3: Cefalea Primaria (Migraña / Sin Fiebre)
    if not tiene_fiebre and (ubicacion_dolor == "Pulsátil (Latidos en un lado o toda la cabeza)" or fotofobia) and intensidad_dolor >= 6:
        return {
            "diagnostico": "Cuadro Sugerente de Migraña / Cefalea Primaria",
            "triaje": "NIVEL 2 - ATENCIÓN AMBULATORIA",
            "justificacion": "Cefalea pulsátil e intensa con fotofobia en ausencia de síndrome febril activo.",
            "plan": [
                "Descanso en ambiente oscuro y libre de ruidos.",
                "Uso de analgésicos o triptanes indicados por medicina general/neurología."
            ],
            "alerta": "Acuda a urgencias si el dolor inicia bruscamente como un 'estallido'.",
            "color": "info"
        }

    # REGLA 4: Síndrome Febril Inespecífico
    if tiene_fiebre:
        return {
            "diagnostico": "Síndrome Febril Agudo en Estudio",
            "triaje": "NIVEL 2 - OBSERVACIÓN",
            "justificacion": "Fiebre comprobada sin un foco infeccioso localizable de forma inmediata.",
            "plan": [
                "Llevar control escrito de la temperatura cada 4 horas.",
                "Mantener hidratación constante y consultar a un centro de salud si la fiebre persiste."
            ],
            "alerta": "Consultar si la temperatura supera los 38.5°C.",
            "color": "success"
        }

    # REGLA 5: Evaluación Normal
    return {
        "diagnostico": "Sin Criterios de Afección Aguda Febril o Cefalea Severa",
        "triaje": "NIVEL 3 - CONTROL GENERAL",
        "justificacion": "Los parámetros registrados no sobrepasan los umbrales de las reglas clínicas del sistema.",
        "plan": [
            "Mantener hábitos saludables e hidratación adecuada.",
            "Evitar la automedicación."
        ],
        "alerta": "Si los síntomas varían o empeoran, realice una nueva evaluación.",
        "color": "success"
    }

# Despliegue de Resultados del Diagnóstico
with col_salidas:
    st.header("📊 Dictamen del Sistema Experto")
    
    res = motor_inferencia()
    
    if res["color"] == "error":
        st.error(f"### 🛑 {res['diagnostico']}\n**Triaje:** {res['triaje']}")
    elif res["color"] == "warning":
        st.warning(f"### ⚠️ {res['diagnostico']}\n**Triaje:** {res['triaje']}")
    elif res["color"] == "info":
        st.info(f"### ℹ️ {res['diagnostico']}\n**Triaje:** {res['triaje']}")
    else:
        st.success(f"### ✅ {res['diagnostico']}\n**Triaje:** {res['triaje']}")

    st.markdown("---")
    st.markdown(f"**Fundamentación de la Inferencia:**\n{res['justificacion']}")
    
    st.markdown("---")
    st.subheader("💡 Plan de Acción e Indicaciones")
    for i, paso in enumerate(res["plan"], 1):
        st.markdown(f"**{i}.** {paso}")
        
    st.markdown("---")
    st.write(f"**Indicación de Seguridad:** {res['alerta']}")

st.markdown("---")
st.caption("Nota: Sistema Experto de Soporte a Decisiones Médicas (DSS) para la especialidad de Infectología. No sustituye la evaluación profesional.")
