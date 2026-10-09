import streamlit as st

st.set_page_config(page_title="SE Diagnóstico de Cefaleas", page_icon="🩺", layout="centered")

st.title("🩺 Sistema Experto de Triaje: Diagnóstico de Cefaleas")
st.write("Especialidad: **Neurología / Triaje Médico Rápido**")
st.markdown("---")

st.sidebar.header("📋 Datos del Paciente")
edad = st.sidebar.number_input("Edad del paciente", min_value=1, max_value=110, value=30)
genero = st.sidebar.selectbox("Género", ["Femenino", "Masculino", "Otro"])
duracion = st.sidebar.selectbox("Duración habitual del episodio:", [
    "Menos de 3 horas",
    "Entre 4 y 72 horas",
    "Varios días continuos"
])

st.header("🔍 Evaluación de Síntomas y Signos Clínicos")

st.subheader("⚠️ 1. Signos de Alarma (Red Flags)")
col1, col2 = st.columns(2)
with col1:
    furia_inicio = st.checkbox("Inicio explosivo o súbito (Dolor en estallido)")
    fiebre_rigidez = st.checkbox("Fiebre con rigidez de nuca / alteración de conciencia")
with col2:
    deficit_neurologico = st.checkbox("Pérdida de fuerza, visión doble o dificultad para hablar")
    trauma = st.checkbox("Aparición tras traumatismo craneal reciente")

st.subheader("🧠 2. Características e Intensidad del Dolor")
intensidad = st.select_slider("Intensidad del dolor (1-10):", options=list(range(1, 11)), value=5)
ubicacion = st.radio("Ubicación del dolor:", ["Unilateral (Un solo lado)", "Bilateral (Ambos lados / En banda)", "Orbital (Alrededor de un ojo)"])
tipo_dolor = st.radio("Tipo de pulsación/sensación:", ["Pulsátil (Latido)", "Opresivo (Cinta que aprieta)", "Taladrante / Punzante intenso"])

st.subheader("👁️ 3. Síntomas Acompañantes")
col3, col4 = st.columns(2)
with col3:
    nauseas = st.checkbox("Náuseas o vómitos")
    fotofobia = st.checkbox("Miedo o molestia a la luz (Fotofobia) y sonido (Fonofobia)")
with col4:
    lagrimeo_ojo = st.checkbox("Lagrimeo o enrojecimiento del ojo en el lado del dolor")
    aura = st.checkbox("Aura visual (destellos, luces o líneas antes del dolor)")

def motor_inferencia():
    if furia_inicio or fiebre_rigidez or deficit_neurologico or trauma:
        return {
            "diagnostico": "Urgencia Neurológica / Posible Cefalea Secundaria",
            "nivel": "CRÍTICO - ATENCIÓN INMEDIATA",
            "explicacion": "Se identificaron signos de alarma clínicos que requieren descarte inmediato de patología intracraneal o infecciosa.",
            "recomendacion": "Diríjase de inmediato a un centro de urgencias o guardia médica.",
            "color": "error"
        }
    
    if (ubicacion == "Unilateral (Un solo lado)" or aura) and (tipo_dolor == "Pulsátil (Latido)") and (nauseas or fotofobia) and intensidad >= 6:
        tipo = "Migraña con Aura" if aura else "Migraña sin Aura"
        return {
            "diagnostico": f"Cuadro compatible con {tipo}",
            "nivel": "NIVEL 1 - MODERADO A ALTO",
            "explicacion": "Cumple los criterios con dolor unilateral, pulsátil, de moderada a alta intensidad, asociado a síntomas vegetativos/sensoriales.",
            "recomendacion": "Consulta con Neurología o Medicina General para indicación de triptanes o antimigrañosos específicos.",
            "color": "warning"
        }

    if ubicacion == "Orbital (Alrededor de un ojo)" and tipo_dolor == "Taladrante / Punzante intenso" and lagrimeo_ojo and intensidad >= 8:
        return {
            "diagnostico": "Cuadro compatible con Cefalea en Brotes (Trigémino-Autonómica)",
            "nivel": "NIVEL 1 - ALTO (Dolor Severo)",
            "explicacion": "Presenta localización periorbitaria muy severa con síntomas autonómicos craneales unilaterales (lagrimeo/enrojecimiento).",
            "recomendacion": "Evaluación prioritaria por Neurología. El tratamiento agudo suele requerir oxigenoterapia e inyectables específicos.",
            "color": "warning"
        }

    if ubicacion == "Bilateral (Ambos lados / En banda)" and tipo_dolor == "Opresivo (Cinta que aprieta)" and not nauseas and intensidad <= 6:
        return {
            "diagnostico": "Cuadro compatible con Cefalea Tensional",
            "nivel": "NIVEL 2 - LEVE / MODERADO",
            "explicacion": "Dolor de carácter opresivo holocraneal o en banda, de intensidad leve a moderada, sin náuseas ni agravación intensa.",
            "recomendacion": "Manejo inicial con analgésicos comunes, control de estrés, hidratación y corrección postural.",
            "color": "info"
        }

    return {
        "diagnostico": "Cefalea Inespecífica / No Clasificada",
        "nivel": "NIVEL 3 - EVALUACIÓN GENERAL",
        "explicacion": "Los síntomas reportados no cumplen strictly el patrón clásico de una cefalea primaria específica.",
        "recomendacion": "Llevar un diario de dolor de cabeza y consultar con un médico de atención primaria.",
        "color": "success"
    }

st.markdown("---")
if st.button("🚀 Ejecutar Diagnóstico del Sistema Experto", use_container_width=True):
    res = motor_inferencia()
    
    st.subheader("📊 Resultado de la Inferencia")
    
    if res["color"] == "error":
        st.error(f"**Prioridad:** {res['nivel']}")
    elif res["color"] == "warning":
        st.warning(f"**Prioridad:** {res['nivel']}")
    elif res["color"] == "info":
        st.info(f"**Prioridad:** {res['nivel']}")
    else:
        st.success(f"**Prioridad:** {res['nivel']}")
        
    st.markdown(f"**Diagnóstico Sugerido:** {res['diagnostico']}")
    st.markdown(f"**Explicación del Sistema:** {res['explicacion']}")
    st.markdown(f"**Recomendación:** {res['recomendacion']}")

st.caption("Nota: Este sistema experto es una herramienta de soporte de decisiones orientativo y no reemplaza la evaluación clínica profesional.")
