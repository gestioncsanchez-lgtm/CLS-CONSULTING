import streamlit as st

# Configuración general de la página
st.set_page_config(
    page_title="CLS Consulting | Gestión, Calidad y Logística",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS personalizados para un diseño corporativo moderno
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
        color: #1e293b;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.25rem;
        color: #93c5fd;
        font-weight: 500;
    }
    .section-title {
        color: #0f172a;
        font-size: 1.75rem;
        font-weight: 700;
        border-bottom: 3px solid #2563eb;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.04);
        height: 100%;
    }
    .card-title {
        color: #1e40af;
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    .highlight-box {
        background-color: #eff6ff;
        border-left: 5px solid #2563eb;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    .footer-banner {
        background-color: #0f172a;
        color: #f8fafc;
        text-align: center;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# --- ENCABEZADO PRINCIPAL (HERO) ---
st.markdown("""
<div class="hero-box">
    <div class="hero-title">Consultoría en Gestión Empresarial, Calidad y Logística</div>
    <div class="hero-subtitle">Transformamos conocimientos en resultados, impulsando la excelencia organizacional.</div>
</div>
""", unsafe_allow_html=True)

# --- PRESENTACIÓN Y MISIÓN ---
col_intro1, col_intro2 = st.columns([1.2, 1], gap="large")

with col_intro1:
    st.markdown('<div class="section-title">Quiénes Somos</div>', unsafe_allow_html=True)
    st.write("""
    Bienvenidos a nuestra consultoría especializada en **gestión empresarial, calidad, logística y mejora continua**, 
    liderada por el **Dr. Ing. César Luis Sánchez**, Doctor en Administración, Ingeniero Electricista y especialista 
    en gestión estratégica, con más de **30 años de trayectoria profesional** en organizaciones nacionales e internacionales.
    """)
    st.write("""
    Trabajamos con **niveles directivos, mandos gerenciales, mandos medios y equipos operativos**, promoviendo el 
    desarrollo de competencias que permitan transformar conocimientos en acciones concretas y resultados medibles.
    """)

with col_intro2:
    st.markdown('<div class="section-title">Nuestra Misión</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-box">
        <p style="font-size: 1.05rem; margin: 0; color: #1e3a8a;">
            <strong>Fortalecer la competitividad, productividad y sostenibilidad de las organizaciones</strong>, 
            mediante soluciones integrales de consultoría, asesoramiento y capacitación, adaptadas a las necesidades 
            de cada empresa.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- ÁREAS DE ESPECIALIZACIÓN ---
st.markdown('<div class="section-title">Nuestras Áreas de Especialización</div>', unsafe_allow_html=True)

row1_col1, row1_col2, row1_col3 = st.columns(3, gap="medium")

with row1_col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📈 Gestión Empresarial y Estratégica</div>
        <p>Planificación, diagnóstico organizacional, indicadores de desempeño (KPI, OKR y KRI) y toma de decisiones.</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">⚙️ Gestión de Calidad y Mejora Continua</div>
        <p>Optimización de procesos, sistemas de gestión, auditorías internas, reducción de costos de no calidad y excelencia operacional.</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">🚚 Logística y Operaciones</div>
        <p>Gestión de inventarios, almacenamiento, distribución, productividad y optimización de recursos.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Espaciado vertical

row2_col1, row2_col2 = st.columns(2, gap="medium")

with row2_col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🤝 Liderazgo y Desarrollo de Equipos</div>
        <p>Fortalecimiento de competencias directivas, comunicación organizacional, gestión del talento y cultura de mejora continua.</p>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🤖 Innovación e Inteligencia Artificial</div>
        <p>Incorporación de herramientas digitales e IA aplicada al análisis de datos, automatización de procesos y mejora de decisiones empresariales.</p>
    </div>
    """, unsafe_allow_html=True)

# --- METODOLOGÍA Y COMPROMISO ---
st.markdown("---")
col_met, col_comp = st.columns(2, gap="large")

with col_met:
    st.markdown('<div class="section-title">Nuestra Metodología</div>', unsafe_allow_html=True)
    st.write("""
    Combinamos experiencia profesional, fundamentos científicos y herramientas tecnológicas innovadoras, mediante 
    capacitaciones dinámicas, talleres prácticos, diagnósticos organizacionales y proyectos de mejora adaptados a cada realidad empresarial.
    """)
    st.info("Nuestro enfoque prioriza la identificación de oportunidades, la participación de las personas y la implementación de soluciones viables, orientadas a generar valor sostenible.")

with col_comp:
    st.markdown('<div class="section-title">Nuestro Compromiso</div>', unsafe_allow_html=True)
    st.write("""
    Creemos que las organizaciones alcanzan mejores resultados cuando desarrollan personas, optimizan procesos y 
    construyen una cultura de aprendizaje permanente.
    """)
    st.success("Acompañamos a las empresas en su transformación, convirtiendo desafíos en oportunidades de crecimiento, innovación y competitividad.")

# --- FORMULARIO DE CONTACTO INTERACTIVO ---
st.markdown('<div class="section-title">Solicitar Asesoramiento o Capacitación</div>', unsafe_allow_html=True)
with st.form("contacto_form"):
    c1, c2 = st.columns(2)
    nombre = c1.text_input("Nombre y Apellido / Empresa")
    email = c2.text_input("Correo Electrónico")
    area = st.selectbox("Área de interés", [
        "Gestión empresarial y estratégica",
        "Gestión de calidad y mejora continua",
        "Logística y operaciones",
        "Liderazgo y desarrollo de equipos",
        "Innovación e inteligencia artificial"
    ])
    mensaje = st.text_area("Cuéntenos brevemente sobre su necesidad o proyecto")
    enviado = st.form_submit_button("Enviar Consulta")
    
    if enviado:
        if nombre and email:
            st.success(f"¡Gracias {nombre}! Su consulta sobre '{area}' ha sido registrada. Nos pondremos en contacto a la brevedad.")
        else:
            st.warning("Por favor, complete al menos su nombre y correo electrónico.")

# --- PIE DE PÁGINA ---
st.markdown("""
<div class="footer-banner">
    <h3 style="margin:0; color:#ffffff;">Consultoría, conocimiento e innovación al servicio de la excelencia empresarial.</h3>
    <p style="margin-top:0.5rem; color:#94a3b8; font-size:0.9rem;">CLS Consulting — Liderado por Dr. Ing. César Luis Sánchez</p>
</div>
""", unsafe_allow_html=True)
