import streamlit as st
from pathlib import Path
from PIL import Image

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Anitha Devi C | GenAI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# GLOBAL CUSTOM CSS (All styles consolidated here)
# =====================================================

st.markdown("""
<style>

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

.hero{
    background: linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:35px;
    border-radius:20px;
    color:white;
    box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.skill-badge{
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:8px 14px;
    border-radius:20px;
    margin:4px;
    font-size:14px;
    font-weight:500;
}

/* Timeline Layout Fixes */
.timeline{
    border-left: 4px solid #2563eb;
    padding-left: 20px;
    margin-left: 10px;
    margin-top: 15px;
}

.timeline-item {
    margin-bottom: 35px;
    position: relative;
}

.tech-badge {
    background-color: #f0f2f6;
    color: #31333F;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: bold;
    margin-right: 6px;
    display: inline-block;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

col1, col2 = st.columns([1, 3])

with col1:
    profile_path = Path("assets/profile.jpg")

    if profile_path.exists():
        image = Image.open(profile_path)
        st.image(image, width=250)
    else:
        st.info("Add profile.jpg inside assets folder")

with col2:
    st.markdown("""
    <div class="hero">

    <h1>🤖 Anitha Devi C</h1>

    <h3>Generative AI & Agentic AI Developer</h3>

    <p style="font-size:18px;">
    Building intelligent AI applications using
    LangGraph, AutoGen, OpenAI, RAG,
    FastAPI, Supabase and Multi-Agent Systems.
    </p>

    <p>
    Passionate about Agentic AI, Multi-Agent Systems,
    Retrieval-Augmented Generation (RAG),
    and Production-Ready AI Applications.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# LINKS
# =====================================================

c1, c2, c3 = st.columns(3)

with c1:
    st.link_button(
        "🔗 GitHub",
        "https://github.com/AnithaChellamuthu"
    )

with c2:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/anitha-chelamuthu-b93757b0/"
    )

with c3:
    resume_path = Path("assets/resume.pdf")

    if resume_path.exists():
        with open(resume_path, "rb") as pdf:
            st.download_button(
                label="📄 Download Resume",
                data=pdf,
                file_name="Anitha_Devi_C_Resume.pdf",
                mime="application/pdf"
            )

st.divider()

# =====================================================
# ABOUT
# =====================================================

st.header("👩‍💻 About Me")

st.write("""
I am passionate about building real-world Generative AI applications that solve practical problems.

My interests include:

- Retrieval-Augmented Generation (RAG)
- Agentic AI
- Multi-Agent Systems
- Workflow Orchestration
- AI Assistants
- LLM Powered Applications

I enjoy creating intelligent systems that can reason, retrieve information, collaborate, and continuously improve through user interaction.
""")

st.divider()

# =====================================================
# SKILLS
# =====================================================

st.header("🛠 Technical Skills")

skills = [
    "Autonomous Agents",
    "Python",
    "LangChain",
    "LangGraph",
    "AutoGen",
    "OpenAI",
    "FastAPI",
    "Supabase",
    "Pinecone",
    "FAISS",
    "Embeddings",
    "RAG",
    "Prompt Engineering",
    "Multi-Agent Systems",
    "Git",
    "GitHub",
    "Java",
    "REST API's",
    "SQL"
]

# 1. Join all skill badges into a single string
badge_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in skills])

# 2. Wrap them in a flexbox container for horizontal alignment and automatic wrapping
st.markdown(
    f"""
    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
        {badge_html}
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# AI JOURNEY
# =====================================================

st.header("🚀 AI Learning Journey")

st.markdown("""
<div class="timeline">

    <!-- MILESTONE 1 -->
    <div class="timeline-item">
        <h4>📚 Multimodal RAG Systems</h4>
        <p>Engineered an advanced retrieval pipeline that ingests live website URLs to extract, chunk, and index both text and visual elements. By mapping image metadata directly to semantic text chunks, the system enables an LLM to deliver context-grounded answers paired with real-time supporting visuals.</p>
        <p>💡 <b>Key Accomplishments:</b></p>
        <ul>
            <li>Automated parsing and intelligent chunking of rich web content.</li>
            <li>Eliminated hallucinations by forcing strict grounding on retrieved data.</li>
        </ul>
        <div>
            <span class="tech-badge">Supabase (pgvector)</span>
            <span class="tech-badge">LangChain</span>
            <span class="tech-badge">OpenAI GPT-4o</span>
            <span class="tech-badge">BeautifulSoup</span>
        </div>
    </div>

    <!-- MILESTONE 2 -->
    <div class="timeline-item">
        <h4>✈️ Agentic Workflows with LangGraph</h4>
        <p>Designed and deployed autonomous, stateful travel planning agents using graph-based architectures. The system coordinates cyclical workflows where agents dynamically gather real-time data, reason over complex budget and scheduling constraints, and iteratively refine highly customized itineraries.</p>
        <p>💡 <b>Key Accomplishments:</b></p>
        <ul>
            <li>Implemented state management to track and update user constraints dynamically.</li>
            <li>Created feedback loops for continuous self-correction and route optimization.</li>
        </ul>
        <div>
            <span class="tech-badge">LangGraph</span>
            <span class="tech-badge">Stateful Agents</span>
            <span class="tech-badge">Tool Calling</span>
            <span class="tech-badge">Python</span>
        </div>
    </div>

    <!-- MILESTONE 3 -->
    <div class="timeline-item">
        <h4>🤝 Multi-Agent Systems using AutoGen</h4>
        <p>Developed an AI-powered "Study Buddy" that transforms static PDF textbooks into conversational learning tools. Built on a swarm framework, the project coordinates specialized agents to handle core tutoring, active recall evaluation, and human-in-the-loop validation.</p>
        <p>💡 <b>Key Accomplishments:</b></p>
        <ul>
            <li><b>Tutor & MCQ Agents:</b> Cooperate to explain concepts and instantly generate custom quizzes.</li>
            <li><b>User Proxy Agent:</b> Orchestrates seamless task handoffs and direct human feedback.</li>
        </ul>
        <div>
            <span class="tech-badge">AutoGen Swarm</span>
            <span class="tech-badge">FAISS Vectorstore</span>
            <span class="tech-badge">Strict RAG Context</span>
        </div>
    </div>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# HIGHLIGHTS
# =====================================================

st.header("📊 Portfolio Highlights")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("Projects", "3")

with m2:
    st.metric("Core Focus", "GenAI")

with m3:
    st.metric("Specialization", "Agentic AI")

with m4:
    st.metric("Frameworks", "5+")

st.divider()
