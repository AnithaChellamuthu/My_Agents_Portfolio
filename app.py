import streamlit as st

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Anith C | GenAI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.profile-name {
    font-size: 3rem;
    font-weight: bold;
}

.profile-title {
    font-size: 1.4rem;
    color: #4F8BF9;
}

.section-header {
    font-size: 2rem;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 15px;
}

.project-card {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

.skill-box {
    background-color: #f3f4f6;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------

col1, col2 = st.columns([1,3])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=180
    )

with col2:
    st.markdown(
        '<div class="profile-name">Anith C</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="profile-title">Generative AI Engineer | Python Developer | RAG & Agentic AI Enthusiast</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        Passionate about building intelligent AI systems using
        LLMs, RAG architectures, LangChain, LangGraph,
        Vector Databases and AI Agents.
        """
    )

    st.markdown("""
📍 Chennai, India

📧 your.email@example.com

🔗 [LinkedIn](https://linkedin.com)

💻 [GitHub](https://github.com)
""")

st.divider()

# -------------------------
# ABOUT
# -------------------------

st.markdown(
    '<div class="section-header">About Me</div>',
    unsafe_allow_html=True
)

st.write("""
I am a Generative AI developer specializing in designing and building
AI-powered applications using OpenAI models, LangChain, LangGraph,
RAG pipelines, vector databases, and agentic workflows.

My goal is to create intelligent systems that combine retrieval,
reasoning, memory, and multimodal capabilities to solve real-world problems.
""")

# -------------------------
# SKILLS
# -------------------------

st.markdown(
    '<div class="section-header">Technical Skills</div>',
    unsafe_allow_html=True
)

skills = [
    "Python",
    "OpenAI",
    "LangChain",
    "LangGraph",
    "RAG",
    "Supabase",
    "PostgreSQL",
    "Vector Databases",
    "Streamlit",
    "FastAPI",
    "Git",
    "Prompt Engineering"
]

cols = st.columns(4)

for i, skill in enumerate(skills):
    cols[i % 4].markdown(
        f'<div class="skill-box">{skill}</div>',
        unsafe_allow_html=True
    )

# -------------------------
# PROJECTS
# -------------------------

st.markdown(
    '<div class="section-header">Featured Projects</div>',
    unsafe_allow_html=True
)

projects = [

    {
        "title": "Multimodal RAG Assistant",
        "desc": """
        Built a Retrieval-Augmented Generation system that extracts text
        and images from web pages, stores embeddings in Supabase,
        and retrieves contextual answers along with relevant images.
        """,
        "tech": "Python | OpenAI | LangChain | Supabase | Streamlit"
    },

    {
        "title": "AI Quiz Generator Agent",
        "desc": """
        Developed an AI Agent using LangGraph capable of generating MCQs
        with custom guardrails and structured workflows.
        """,
        "tech": "LangGraph | OpenAI | Python"
    },

    {
        "title": "Agentic Knowledge Assistant",
        "desc": """
        Created a multi-step AI assistant capable of planning,
        memory management, retrieval and tool usage.
        """,
        "tech": "LangGraph | LangChain | OpenAI"
    },

    {
        "title": "Web Content Intelligence Pipeline",
        "desc": """
        Built a pipeline that crawls websites, extracts content,
        generates embeddings and enables semantic search.
        """,
        "tech": "Python | BeautifulSoup | Supabase"
    }
]

for project in projects:

    st.markdown(
        f"""
        <div class="project-card">
            <h3>{project['title']}</h3>
            <p>{project['desc']}</p>
            <b>Tech Stack:</b> {project['tech']}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# CURRENT LEARNING
# -------------------------

st.markdown(
    '<div class="section-header">Currently Learning</div>',
    unsafe_allow_html=True
)

st.write("""
- Advanced LangGraph Workflows
- Multi-Agent Systems
- MCP Architecture
- AI Evaluation Frameworks
- Production-grade GenAI Deployment
""")

# -------------------------
# RESUME
# -------------------------

st.markdown(
    '<div class="section-header">Resume</div>',
    unsafe_allow_html=True
)

st.info(
    "Upload your latest resume PDF and add a download button here."
)

# -------------------------
# CONTACT
# -------------------------

st.markdown(
    '<div class="section-header">Contact</div>',
    unsafe_allow_html=True
)

st.write("""
Interested in collaborating on:

✅ Generative AI Projects

✅ RAG Applications

✅ AI Agent Development

✅ Python Automation

✅ LLM-Powered Solutions
""")

st.success("Let's connect and build intelligent AI solutions together!")

st.markdown("""
📧 your.email@example.com

🔗 https://linkedin.com/in/yourprofile

💻 https://github.com/yourgithub
""")

# -------------------------
# FOOTER
# -------------------------

st.divider()

st.caption(
    "© 2026 Anith C | Generative AI Portfolio"
)
