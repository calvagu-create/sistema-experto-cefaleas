import streamlit as st
from datetime import datetime

# Configuración de la aplicación
st.set_page_config(
    page_title="Consulta Médica de Cabecera", 
    page_icon="🩺", 
    layout="wide"
)

# Estilo visual de Boleta Médica Impresa Realista
st.markdown("""
<style>
    .boleta-medica {
        background-color: #ffffff;
        border: 2px solid #2c3e50;
        border-radius: 10px;
        padding: 30px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        max-width: 750px;
        margin: auto;
    }
    .boleta-encabezado {
        text-align: center;
        border-bottom: 2px solid #2c3e50;
        padding-bottom: 15px;
        margin-bottom: 20px;
    }
    .boleta-titulo-seccion {
        font-weight: bold;
        background-color: #ecf0f1;
        padding: 6px 10px;
        border-left: 5px solid #2980b9;
        margin-top: 15px;
        margin-bottom: 10px;
        text-transform: uppercase;
        font-size: 14px;
    }
    .boleta-contenido {
        line-height: 1.6;
        font-size: 15px;
    }
    .boleta-firma {
        text-align: center;
        margin-top: 30px;
        border-top: 1px solid #ccc;
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🩺 Consultorio Médico Virtual de Cabecera")
st.write("Seleccione sus síntomas para analizar su cuadro de **fiebre y dolor de cabeza**, y obtener su boleta con indicaciones de descanso y cuidados en casa.")
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
        
    temperatura = st.slider("Medición de Temperatura corporal (°C):", min_value=35.5, max_value=40.5, value=38.2, step=0.1)

    st.subheader("🧠 Características del Dolor de Cabeza")
    tipo_dolor = st.radio("¿Cómo siente el dolor de cabeza?", [
        "Pulsátil (Latidos constantes en las sienes o un lado)",
        "Pesadez y opresión (Como un casco apretado alrededor de la cabeza)",
        "Dolor profundo detrás de los ojos",
        "Sin dolor de cabeza significativo"
    ])
    
    intensidad_dolor = st.select_slider("Intensidad del dolor (1 al 10):", options=list(range(1, 11)), value=6)

    st.subheader("🤒 Síntomas Acompañantes")
    st.write("Marque las molestias que está sintiendo actualmente:")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        s_fotofobia = st.checkbox("Molestia intensa a la luz o al ruido")
        s_mialgias = st.checkbox("Dolor en los músculos y articulaciones")
        s_nauseas = st.checkbox("Sensación de náuseas o mareos")
    with col_s2:
        s_respiratorio = st.checkbox("Congestión nasal, tos o dolor de garganta")
        s_escalofrios = st.checkbox("Escalofríos y sudoración nocturna")
        s_cansancio = st.checkbox("Fatiga extrema o pesadez en el cuerpo")

    # BOTÓN DE EJECUCIÓN
    btn_analizar = st.button("📄 Generar Boleta de Diagnóstico y Cuidados", type="primary", use_container_width=True)

with col_boleta:
    st.subheader("🧾 Boleta de Atención Médica Virtual")
    
    if btn_analizar:
        fecha_emision = datetime.now().strftime("%d/%m/%Y %H:%M")
        tiene_fiebre = temperatura >= 38.0

        # LÓGICA DE DIAGNÓSTICO Y RECOMENDACIONES CASERAS
        # Caso 1: Cuadro Migrañoso / Cefalea por Estrés y Tensión (Sin fiebre alta)
        if not tiene_fiebre and (tipo_dolor == "Pulsátil (Latidos constantes en las sienes o un lado)" or s_fotofobia) and intensidad_dolor >= 5:
            diagnostico = "Cuadro de Migraña Aguda o Cefalea Tensional"
            analisis = "El dolor de tipo pulsátil con fotosensibilidad sin presencia de síntoma febril indica un episodio de cefalea primaria por fatiga, sobrecarga visual o estrés."
            cuidados = [
                "**Descanso absoluto:** Reposar de 8 a 10 horas continuas en una habitación totalmente oscura y sin ruidos.",
                "**Compresas frías:** Colocar un paño limpio húmedo con agua fría en la frente y las sienes durante 15 minutos.",
                "**Infusión relajante:** Tomar un té caliente de manzanilla, tilo o toronjil para relajar la tensión muscular.",
                "**Desconexión:** Evitar por completo pantallas de televisión, celular o computadoras durante las próximas 12 horas.",
                "**Masaje:** Realizar masajes suaves y circulares en el cuello, hombros y sienes usando las yemas de los dedos."
            ]

        # Caso 2: Cuadro Viral con Fiebre y Dolor Retroocular (Estilo Dengue / Gripe Fuerte)
        elif tiene_fiebre and (tipo_dolor == "Dolor profundo detrás de los ojos" or s_mialgias):
            diagnostico = "Síndrome Febril Viral / Proceso Infeccioso Cutáneo o Tropico-Viral"
            analisis = "Presenta la combinación clásica de temperatura elevada acompañada de dolor muscular generalizado y dolor retroocular, característico de infecciones virales."
            cuidados = [
                "**Reposo en cama:** Guardar reposo absoluto en cama por al menos 3 a 5 días para permitir que el sistema inmune actúe.",
                "**Hidratación intensa:** Tomar de 2.5 a 3 litros de líquidos al día (agua de coco, sueros orales caseros, sopas ligeras y té de kión/jengibre con limón).",
                "**Control de la temperatura:** Aplicar paños con agua a temperatura ambiente (no helada) en las axilas y frente. Tomar duchas de agua tibia.",
                "**Alimentación ligera:** Consumir caldos de gallina o pollo sin grasa, papas sancochadas y frutas ricas en agua (patilla/sandía, melón).",
                "**Evitar esfuerzos:** No realizar actividad física ni levantar objetos pesados durante una semana."
            ]

        # Caso 3: Cuadro Respiratorio Febril (Gripe / Resfriado)
        elif tiene_fiebre and s_respiratorio:
            diagnostico = "Infección Respiratoria Aguda / Resfriado Febril"
            analisis = "La fiebre combinada con malestar en garganta o vías respiratorias indica un proceso viral en las vías aéreas superiores."
            cuidados = [
                "**Infusiones calientes:** Tomar té caliente de eucalipto, menta o limón con miel 3 veces al día para aliviar la garganta y descongestionar.",
                "**Vaporizaciones:** Hacer inhalaciones de vapor de agua con hojas de eucalipto durante 10 minutos antes de dormir.",
                "**Descanso:** Dormir un mínimo de 9 horas por noche y tomar siestas de 30 minutos por la tarde.",
                "**Abrigarse correctamente:** Mantener el pecho y los pies abrigados, evitando corrientes de aire frío.",
                "**Alimentación rica en Vitamina C:** Consumir naranjas, mandarinas y caldos calientes nutritivos."
            ]

        # Caso 4: Fiebre Aguda Inespecífica por Agotamiento o Insolación
        elif tiene_fiebre:
            diagnostico = "Síndrome Febril Agudo en Observación"
            analisis = "Se evidencia aumento de la temperatura corporal con malestar general sin localización específica inmediata."
            cuidados = [
                "**Monitoreo:** Medir y anotar la temperatura cada 4 horas.",
                "**Hidratación abundante:** Tomar abundantes infusiones tibias y agua natural a temperatura ambiente.",
                "**Reposo:** Guardar reposo en casa por las próximas 48 horas.",
                "**Baño de agua tibia:** Tomar un baño con agua tibia si la temperatura supera los 38.5°C para refrescar el cuerpo de forma gradual."
            ]

        # Caso 5: Evaluación Normal
        else:
            diagnostico = "Estado General Estable / Sin Criterios de Infección Aguda"
            analisis = "Los valores y síntomas ingresados se encuentran dentro de los rangos normales o de cansancio leve."
            cuidados = [
                "**Hábitos de sueño:** Dormir de 7 a 8 horas diarias para mantener defensas altas.",
                "**Buena hidratación:** Tomar al menos 2 litros de agua durante el día.",
                "**Alimentación balanceada:** Incluir verduras frescas, frutas y proteínas magras en la dieta diaria."
            ]

        # RENDERIZADO DE LA BOLETA MÉDICA
        st.markdown(f"""
        <div class="boleta-medica">
            <div class="boleta-encabezado">
                <h2 style="margin:0; color:#2c3e50;">📋 BOLETA DE ATENCIÓN Y CUIDADOS MÉDICOS</h2>
                <p style="margin:5px 0 0 0; font-size:14px; color:#7f8c8d;">Consultorio Virtual de Cabecera | Infectología y Medicina General</p>
                <p style="margin:2px 0 0 0; font-size:12px; color:#95a5a6;">Fecha y Hora: {fecha_emision}</p>
            </div>
            
            <div class="boleta-contenido">
                <p><strong>PACIENTE:</strong> {nombre_paciente.upper()}</p>
                <p><strong>EDAD / GÉNERO:</strong> {edad} años | {genero}</p>
                <p><strong>TEMPERATURA REGISTRADA:</strong> {temperatura} °C</p>
                
                <div class="boleta-titulo-seccion">📌 Diagnóstico del Médico especialista</div>
                <p><strong>{diagnostico}</strong></p>
                <p><em>{analisis}</em></p>
                
                <div class="boleta-titulo-seccion">🍵 Plan de Tratamiento y Recomendaciones Caseras</div>
        """, unsafe_allow_html=True)

        for c in cuidados:
            st.markdown(f"- {c}")

        st.markdown("""
                <div class="boleta-firma">
                    <br>
                    <p>____________________________________________</p>
                    <p><strong>Firma y Sello del Médico Especialista</strong></p>
                    <p><small>Atención Médica Virtual y Diagnóstico Familiar</small></p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("👈 Complete los síntomas del paciente en el panel de la izquierda y presione **'Generar Boleta de Diagnóstico y Cuidados'** para visualizar su informe médico.")
