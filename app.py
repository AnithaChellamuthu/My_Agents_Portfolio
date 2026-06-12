# app.py


import streamlit as st
from PIL import Image
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Anitha Devi C | GenAI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
}

.hero-card{
    background: linear-gradient(135deg,#0F172A,#1E293B);
    padding:30px;
    border-radius:20px;
    border:1px solid #334155;
}

.project-card{
    padding:20px;
    border-radius:18px;
    background-color:#111827;
    border:1px solid #374151;
    margin-bottom:20px;
}

.metric-card{
    background:#1E293B;
    padding:15px;
    border-radius:12px;
    text-align:center;
}

.tech-badge{
    display:inline-block;
    padding:8px 12px;
    margin:4px;
    border-radius:20px;
    background:#2563EB;
    color:white;
    font-size:12px;
}

.project-title{
    color:#60A5FA;
}

hr{
    margin-top:2rem;
    margin-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

col1, col2 = st.columns([1, 3])

with col1:

    image_path = Path("assets/profile.jpg")

    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, width=220)
    else:
        st.info("Add assets/profile.jpg")

with col2:

    st.subheader("Generative AI & Agentic AI Developer")

st.markdown("""
Building intelligent AI applications using:

- LangGraph
- AutoGen
- OpenAI
- RAG
- FastAPI
- Supabase
- Multi-Agent Systems
""")
st.write("")

# --------------------------------------------------
# LINKS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("🔗 GitHub", "https://github.com/AnithaChellamuthu")

with col2:
    st.link_button("💼 LinkedIn", "https://www.linkedin.com/in/anitha-chelamuthu-b93757b0/")

with col3:
    st.link_button("📄 Resume", "#")

st.divider()

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.header("👨‍💻 About Me")

st.write("""
I am passionate about building real-world Generative AI applications.

My interests include:

- Retrieval-Augmented Generation (RAG)
- Agentic AI
- Multi-Agent Systems
- Workflow Orchestration
- AI Assistants
- Production-Ready LLM Applications

I enjoy transforming ideas into intelligent systems that can reason,
retrieve knowledge, and collaborate autonomously.
""")

st.divider()

# --------------------------------------------------
# CAREER JOURNEY
# --------------------------------------------------

st.header("🚀 AI Learning Journey")

st.markdown("""
### RAG Systems
⬇️

### Agentic Workflows
⬇️

### Multi-Agent Systems
""")

st.divider()

# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.header("🛠 Technical Skills")

st.subheader("AI Frameworks")
st.progress(90, text="LangGraph")
st.progress(85, text="LangChain")
st.progress(80, text="AutoGen")
st.progress(75, text="CrewAI")
st.progress(70, text="Google ADK")

st.subheader("Generative AI")
st.progress(90, text="RAG")
st.progress(85, text="Prompt Engineering")
st.progress(80, text="Vector Databases")
st.progress(80, text="OpenAI APIs")

st.subheader("Backend")
st.progress(85, text="Python")
st.progress(80, text="FastAPI")
st.progress(75, text="Supabase")

st.divider()

# --------------------------------------------------
# PROJECT METRICS
# --------------------------------------------------

st.header("📊 Portfolio Highlights")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Projects Built", "3")

with m2:
    st.metric("AI Domains", "RAG + Agents")

with m3:
    st.metric("Learning Focus", "Agentic AI")

st.divider()

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.header("🚀 Featured Projects")

# ==================================================
# PROJECT 1
# ==================================================

st.markdown("""
<div class='project-card'>

<h3 class='project-title'>
1️⃣ Multimodal RAG Assistant
</h3>

<p>
A Retrieval-Augmented Generation system capable of understanding
both text and image content from websites.
</p>

<b>Features</b>

<ul>
<li>Web URL ingestion</li>
<li>Text extraction</li>
<li>Image extraction</li>
<li>Supabase vector storage</li>
<li>Image-aware retrieval</li>
<li>Contextual answers with visuals</li>
</ul>

<b>Tech Stack:</b>

Python • LangChain • OpenAI • Supabase • RAG

</div>
""", unsafe_allow_html=True)

if Path("assets/rag_demo.mp4").exists():
    st.video("assets/rag_demo.mp4")

# ==================================================
# PROJECT 2
# ==================================================

st.markdown("""
<div class='project-card'>

<h3 class='project-title'>
2️⃣ Travel Planner Agent
</h3>

<p>
An intelligent travel planning agent built with LangGraph.
</p>

<b>Capabilities</b>

<ul>
<li>Collects travel preferences</li>
<li>Captures budget information</li>
<li>Checks weather conditions</li>
<li>Finds hotel recommendations</li>
<li>Creates detailed itineraries</li>
<li>Improves plans using user feedback</li>
</ul>

<b>Tech Stack:</b>

LangGraph • OpenAI • Python • Agentic Workflows

</div>
""", unsafe_allow_html=True)

if Path("assets/travel_agent_demo.mp4").exists():
    st.video("assets/travel_agent_demo.mp4")

# ==================================================
# PROJECT 3
# ==================================================

st.markdown("""
<div class='project-card'>

<h3 class='project-title'>
3️⃣ Study Buddy (AutoGen Swarm Team)
</h3>

<p>
A multi-agent educational assistant that helps users learn
from uploaded PDF documents.
</p>

<b>Workflow</b>

<ul>
<li>PDF ingestion</li>
<li>Concept explanation</li>
<li>Quiz generation</li>
<li>Answer validation</li>
<li>Learning reinforcement</li>
</ul>

<b>Multi-Agent Architecture</b>

<ul>
<li>Retriever Agent</li>
<li>Explainer Agent</li>
<li>Quiz Generator Agent</li>
<li>Validator Agent</li>
</ul>

<b>Tech Stack:</b>

AutoGen • Swarm Teams • OpenAI • Python

</div>
""", unsafe_allow_html=True)

if Path("assets/study_buddy_demo.mp4").exists():
    st.video("assets/study_buddy_demo.mp4")

st.divider()

# --------------------------------------------------
# TECH STACK
# --------------------------------------------------

st.header("⚡ Technologies")

techs = [
    "Python",
    "LangChain",
    "LangGraph",
    "AutoGen",
    "OpenAI",
    "FastAPI",
    "Supabase",
    "Vector Databases",
    "RAG",
    "Git",
    "GitHub"
]

cols = st.columns(4)

for i, tech in enumerate(techs):
    cols[i % 4].success(tech)

st.divider()

# --------------------------------------------------
# CURRENTLY LEARNING
# --------------------------------------------------

st.header("📚 Currently Exploring")

st.markdown("""
- Advanced Agentic AI Systems
- MCP (Model Context Protocol)
- Multi-Agent Collaboration
- AI Workflow Evaluation
- Production AI Deployment
""")

st.divider()

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

st.header("📬 Let's Connect")

st.write("📧 anithachelamuthu@gmail.com")
st.write("💼 https://www.linkedin.com/in/anitha-chelamuthu-b93757b0/")
st.write("💻 GitHub: https://github.com/AnithaChellamuthu")

st.success("Thanks for visiting my portfolio 🚀")

