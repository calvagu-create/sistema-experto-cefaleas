import streamlit as st
from datetime import datetime

# Configuración de la clínica virtual
st.set_page_config(
    page_title="Consulta Médica Virtual - Infectología", 
    page_icon="🩺", 
    layout="wide"
)

# Estilo CSS para dar formato de Boleta / Receta Médica
st.markdown("""
<style>
    .boleta-container {
        border: 2px solid #2e6f40;
        background-color: #f9fbf9;
        padding: 25px;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        color: #1a1a1a;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .boleta-header {
        text-align: center;
        border-bottom: 2px dashed #2e6f40;
        padding-bottom: 10px;
        margin-bottom: 15px;
    }
    .boleta-seccion {
        margin-top: 15px;
        border-bottom: 1px dashed #ccc;
        padding-bottom: 10px;
    }
    .boleta-titulo {
        font-weight: bold;
        color: #1b4d2e;
        text-transform: uppercase;
    }
    .urgencia-critica {
        border: 2px solid #b30000;
        background-color: #fff2f2;
    }
</style>
""", unsafe_allow_html=True)

st.title("🩺 Centro Médico Virtual: Consulta Infectológica")
st.caption("Atención del Médico Especialista en Infectología y Medicina Tropical")
st.markdown("---")

col_form, col_receta = st.columns([1, 1.2], gap="large")

with col_form:
    st.header("📝 Ficha Clinica del Paciente")
    
    # Datos Filiatorios
    with st.expander("👤 1. Datos Personales y Signos Vitales", expanded=True):
        nombre = st.text_input("Nombre completo del paciente:", value="Juan Pérez")
        edad = st.number_input("Edad:", min_value=1, max_value=110, value=30)
        genero = st.selectbox("Género:", ["Masculino", "Femenino", "Otro"])
        temperatura = st.slider("Temperatura corporal (°C):", min_value=35.0, max_value=41.0, value=38.4, step=0.1)
        pas = st.number_input("Presión Arterial Sistólica (mmHg):", min_value=50, max_value=200, value=110)

    # Evaluación de Alarma
    with st.expander("🚨 2. ¿Presenta alguno de estos signos graves?", expanded=True):
        rigidez_nuca = st.checkbox("Dificultad para doblar el cuello hacia el pecho")
        alteracion_conciencia = st.checkbox("Confusión, desorientación o somnolencia marcada")
        petequias = st.checkbox("Manchas o puntos morados/rojos en la piel")
        dificultad_respirar = st.checkbox("Dificultad severa para respirar")

    # Sintomatología Principal
    with st.expander("🤒 3. Detalle de los Síntomas", expanded=True):
        intensidad_dolor = st.select_slider("Intensidad del dolor de cabeza (1-10):", options=list(range(1, 11)), value=7)
        tipo_dolor = st.selectbox("Localización principal del dolor:", [
            "Retroocular (Detrás de los ojos)",
            "Pulsátil (Latidos en un lado o toda la cabeza)",
            "Opresivo (Sensación de casco/banda que aprieta)",
            "Sin dolor de cabeza significativo"
        ])
        
        c1, c2 = st.columns(2)
        with c1:
            dolor_muscular = st.checkbox("Dolor muscular / articular intenso")
            nauseas = st.checkbox("Náuseas o vómitos")
        with c2:
            sintomas_respiratorios = st.checkbox("Tos, dolor de garganta o congestión")
            fotofobia = st.checkbox("Molestia intensa a la luz")

# Lógica Médica de Diagnóstico
def diagnostico_doctor():
    tiene_fiebre = temperatura >= 38.0
    hipotension = pas < 90

    # Diagnóstico 1: Urgencia Neurológica o Infectológica Grave
    if rigidez_nuca or alteracion_conciencia or petequias or dificultad_respirar or hipotension:
        return {
            "diagnostico_medico": "MENINGITIS ACUDA / SEPSIS / NEUROINFECCIÓN GRAVE",
            "tipo_gravedad": "CRÍTICA - ATENCIÓN EN EMERGENCIAS",
            "analisis": "El paciente presenta signos de irritación meníngea o falla hemodinámica sistémica. Se requiere descartar infección bacteriana o viral del SNC.",
            "trata_farmaco": "NO ADMINISTRAR MEDICACIÓN ORAL EN CASA. Requiere antibióticos/antivirales endovenosos intrahospitalarios.",
            "conducta": "Derivación inmediata en ambulancia a guardia de emergencias. Punción lumbar y analítica de sangre urgente.",
            "es_critico": True
        }

    # Diagnóstico 2: Dengue u Arbovirosis
    if tiene_fiebre and tipo_dolor == "Retroocular (Detrás de los ojos)" and dolor_muscular:
        return {
            "diagnostico_medico": "SÍNDROME FEBRIL COMPATIBLE CON DENGUE (ARBOVIROSIS)",
            "tipo_gravedad": "PRIORITARIO - REQUERE MONITOREO",
            "analisis": "Presenta el cuadro clínico clásico de arbovirosis: Fiebre, mialgias intensas y dolor retroocular característico.",
            "trata_farmaco": "• Paracetamol 500mg - 1 tableta c/6 horas si hay fiebre o dolor (Máx 3g/día).\n• 🚫 CONTRAINDICADO: Ibuprofeno, Aspirina, Naproxeno (Riesgo de hemorragia).",
            "conducta": "• Hidratación oral estricta: 2.5 a 3 Litros de suero oral/agua al día.\n• Reposo absoluto en cama.\n• Solicitar Hemograma completo (Plaquetas) y prueba NS1.",
            "es_critico": False
        }

    # Diagnóstico 3: Cuadro Respiratorio Gripal Febril
    if tiene_fiebre and sintomas_respiratorios:
        return {
            "diagnostico_medico": "INFECCIÓN AGUDA DE VÍAS RESPIRATORIAS / SÍNDROME GRIPAL",
            "tipo_gravedad": "MODERADO - MANEJO AMBULATORIO",
            "analisis": "Proceso infeccioso de vías aéreas superiores con respuesta febril activa.",
            "trata_farmaco": "• Paracetamol 500mg cada 8 horas según temperatura.\n• Lavados nasales con solución salina.",
            "conducta": "• Reposo en domicilio por 48-72 horas con aislamiento preventivo.\n• Abundante ingesta de líquidos tibios.\n• Usar mascarilla si convive con otras personas.",
            "es_critico": False
        }

    # Diagnóstico 4: Migraña o Cefalea Primaria
    if not tiene_fiebre and (tipo_dolor == "Pulsátil (Latidos en un lado o toda la cabeza)" or fotofobia) and intensidad_dolor >= 6:
        return {
            "diagnostico_medico": "MIGRAÑA AGUDA / CEFALEA PRIMARIA",
            "tipo_gravedad": "AMBULATORIO",
            "analisis": "Episodio de cefalea vascular pulsátil de intensidad moderada-alta con fotosensibilidad, sin signo infeccioso febril.",
            "trata_farmaco": "• Analgésicos/Antimigrañosos indicados por su médico tratante.\n• Evitar automedicarse en exceso.",
            "conducta": "• Reposo en habitación a oscuras y en silencio.\n• Colocar compresa fría en la frente.",
            "es_critico": False
        }

    # Diagnóstico 5: Fiebre Inespecífica
    if tiene_fiebre:
        return {
            "diagnostico_medico": "SÍNDROME FEBRIL EN ESTUDIO",
            "tipo_gravedad": "OBSERVACIÓN",
            "analisis": "Elevación de la temperatura corporal sin foco infeccioso evidente en el interrogatorio inicial.",
            "trata_farmaco": "• Paracetamol 500mg si la temperatura supera los 38.0°C.",
            "conducta": "• Controlar y anotar la temperatura cada 4 horas.\n• Mantenerse bien hidratado.\n• Consultar a un médico presencial si la fiebre no cede en 48 horas.",
            "es_critico": False
        }

    # Diagnóstico 6: Sin hallazgos
    return {
        "diagnostico_medico": "EVALUACIÓN SIN HALLAZGOS PATOLÓGICOS AGUDOS",
        "tipo_gravedad": "NORMAL",
        "analisis": "No se identifican criterios de síndrome febril agudo ni cefaleas de riesgo en este momento.",
        "trata_farmaco": "• Sin indicación farmacológica por el momento.",
        "conducta": "• Mantener buena hidratación y hábitos saludables.\n• Si los síntomas cambian, consulte nuevamente.",
        "es_critico": False
    }

# Generación de la Boleta / Receta Médica
with col_receta:
    st.header("📋 Boleta de Atención y Receta Médica")
    
    med = diagnostico_doctor()
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

    clase_boleta = "boleta-container urgencia-critica" if med["es_critico"] else "boleta-container"

    # HTML de la Boleta / Ficha
    st.markdown(f"""
    <div class="{clase_boleta}">
        <div class="boleta-header">
            <h3>🏥 CENTRO MÉDICO DE INFECTOLOGÍA</h3>
            <p><strong>FICHA DE ATENCIÓN Y RECETA MÉDICA</strong></p>
            <p>Fecha de emisión: {fecha_actual}</p>
        </div>
        
        <div>
            <p><strong>PACIENTE:</strong> {nombre.upper()}</p>
            <p><strong>EDAD / GÉNERO:</strong> {edad} años | {genero}</p>
            <p><strong>SIGNOS VITALES:</strong> Temp: {temperatura}°C | PA: {pas} mmHg</p>
        </div>
        
        <div class="boleta-seccion">
            <p class="boleta-titulo">📌 EVALUACIÓN Y DIAGNÓSTICO MÉDICO:</p>
            <p><strong>{med['diagnostico_medico']}</strong></p>
            <p><em>Nivel de Atención: {med['tipo_gravedad']}</em></p>
            <p><strong>Análisis Clínico:</strong> {med['analisis']}</p>
        </div>
        
        <div class="boleta-seccion">
            <p class="boleta-titulo">💊 PRESCRIPCIÓN / TRATAMIENTO RECOMENDADO:</p>
            <p>{med['trata_farmaco'].replace('\n', '<br>')}</p>
        </div>
        
        <div class="boleta-seccion">
            <p class="boleta-titulo">📝 INDICACIONES Y CONDUCTA A SEGUIR:</p>
            <p>{med['conducta'].replace('\n', '<br>')}</p>
        </div>
        
        <br>
        <div style="text-align: center; margin-top: 20px;">
            <p>_____________________________________</p>
            <p><strong>Dra. / Dr. Especialista en Infectología</strong></p>
            <p><small>Colegio Médico / Firma Digital de Consulta Virtual</small></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Aviso legal: Esta boleta médica virtual es una simulación orientativa generada para fines académicos. No sustituye una consulta médica o receta emitida en un establecimiento de salud presencial.")
