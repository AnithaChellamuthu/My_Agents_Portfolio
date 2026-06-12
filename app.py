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

# CUSTOM CSS

# =====================================================

st.markdown("""

<style>

.block-container{
    padding-top:2rem;
    max-width:1200px;
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

.timeline{
    border-left:4px solid #2563eb;
    padding-left:20px;
    margin-left:10px;
}

.project-card{
    padding:20px;
    border-radius:20px;
    background:#111827;
    border:1px solid #374151;
}

.section-title{
    margin-top:25px;
}

</style>

""", unsafe_allow_html=True)

# =====================================================

# HERO SECTION

# =====================================================

col1, col2 = st.columns([1,3])

with col1:

```
profile_path = Path("assets/profile.jpg")

if profile_path.exists():
    image = Image.open(profile_path)
    st.image(image, width=250)
```

with col2:

```
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
```

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

```
resume_path = Path("assets/resume.pdf")

if resume_path.exists():

    with open(resume_path, "rb") as pdf:

        st.download_button(
            label="📄 Download Resume",
            data=pdf,
            file_name="Anitha_Devi_C_Resume.pdf",
            mime="application/pdf"
        )
```

st.divider()

# =====================================================

# ABOUT

# =====================================================

st.header("👩‍💻 About Me")

st.write("""
I am passionate about building real-world Generative AI applications that solve practical problems.

My interests include:

* Retrieval-Augmented Generation (RAG)
* Agentic AI
* Multi-Agent Systems
* Workflow Orchestration
* AI Assistants
* LLM Powered Applications

I enjoy creating intelligent systems that can reason, retrieve information, collaborate, and continuously improve through user interaction.
""")

st.divider()

# =====================================================

# SKILLS

# =====================================================

st.header("🛠 Technical Skills")

skills = [
"Python",
"LangChain",
"LangGraph",
"AutoGen",
"OpenAI",
"FastAPI",
"Supabase",
"RAG",
"Vector Databases",
"Prompt Engineering",
"Multi-Agent Systems",
"Git",
"GitHub"
]

for skill in skills:
st.markdown(
f"<span class='skill-badge'>{skill}</span>",
unsafe_allow_html=True
)

st.divider()

# =====================================================

# AI JOURNEY

# =====================================================

st.header("🚀 AI Learning Journey")

st.markdown("""

<div class="timeline">

<h4>📚 Multimodal RAG Systems</h4>

Built retrieval systems capable of processing both text and images from websites and generating context-aware answers.

<br>

<h4>✈️ Agentic Workflows with LangGraph</h4>

Designed intelligent travel planning agents that gather information, reason over constraints, and iteratively improve travel itineraries.

<br>

<h4>🤝 Multi-Agent Systems using AutoGen</h4>

Built collaborative AI agents capable of explaining concepts, generating quizzes, and validating answers from educational PDFs.

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================

# HIGHLIGHTS

# =====================================================

st.header("📊 Portfolio Highlights")

m1, m2, m3, m4 = st.columns(4)

m1.metric("Projects", "3")
m2.metric("Core Focus", "GenAI")
m3.metric("Specialization", "Agentic AI")
m4.metric("Frameworks", "5+")

st.divider()

# =====================================================

# PROJECTS

# =====================================================

st.header("🚀 Featured Projects")

# -----------------------------------------------------

# PROJECT 1

# -----------------------------------------------------

with st.container(border=True):

```
st.subheader("📚 Multimodal RAG Assistant")

col1, col2 = st.columns([2,1])

with col1:

    st.write("""
```

**Overview**

A Retrieval-Augmented Generation system capable of understanding both text and image content from websites.

**Key Features**

* Web URL ingestion
* Text extraction
* Image extraction
* OpenAI Embeddings
* Supabase Vector Storage
* Image-aware retrieval
* Contextual answers with visuals
  """)

  with col2:

  ```
    screenshot = Path("assets/rag.png")

    if screenshot.exists():
        st.image(str(screenshot))
  ```

  video = Path("assets/rag_demo.mp4")

  if video.exists():
  st.video(str(video))

# -----------------------------------------------------

# PROJECT 2

# -----------------------------------------------------

with st.container(border=True):

```
st.subheader("✈️ Travel Planner Agent")

col1, col2 = st.columns([2,1])

with col1:

    st.write("""
```

**Overview**

An Agentic AI travel planner built using LangGraph.

**Capabilities**

* Collects travel preferences
* Budget planning
* Hotel recommendations
* Weather analysis
* Experience recommendations
* Itinerary generation
* User feedback driven optimization
  """)

  with col2:

  ```
    screenshot = Path("assets/travel.png")

    if screenshot.exists():
        st.image(str(screenshot))
  ```

  video = Path("assets/travel_demo.mp4")

  if video.exists():
  st.video(str(video))

# -----------------------------------------------------

# PROJECT 3

# -----------------------------------------------------

with st.container(border=True):

```
st.subheader("🎓 Study Buddy (AutoGen Swarm Team)")

col1, col2 = st.columns([2,1])

with col1:

    st.write("""
```

**Overview**

A multi-agent educational assistant that helps users learn directly from PDF documents.

**Workflow**

* PDF ingestion
* Concept explanation
* Quiz generation
* Answer validation
* Learning reinforcement

**Agents**

* Retriever Agent
* Explainer Agent
* Quiz Generator Agent
* Validator Agent
  """)

  with col2:

  ```
    screenshot = Path("assets/studybuddy.png")

    if screenshot.exists():
        st.image(str(screenshot))
  ```

  video = Path("assets/study_demo.mp4")

  if video.exists():
  st.video(str(video))

st.divider()

# =====================================================

# CURRENTLY EXPLORING

# =====================================================

st.header("📖 Currently Exploring")

st.markdown("""

* Model Context Protocol (MCP)
* Advanced Agentic AI Architectures
* Multi-Agent Collaboration Patterns
* AI Evaluation Frameworks
* Production AI Deployment
  """)

st.divider()

# =====================================================

# CONTACT

# =====================================================

st.header("📬 Contact")

col1, col2 = st.columns(2)

with col1:
st.info("📧 [anithachelamuthu@gmail.com](mailto:anithachelamuthu@gmail.com)")

with col2:
st.info("🌍 Chennai, India")

st.success("Thank you for visiting my portfolio 🚀")
