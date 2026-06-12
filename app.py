import streamlit as st

st.set_page_config(
    page_title="Anith C | GenAI Portfolio",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🤖 Anitha Devi C")
st.subheader("Generative AI & Agentic AI Developer")

st.markdown("""
Building intelligent AI systems using **LangGraph, AutoGen, RAG, OpenAI, Supabase, and FastAPI**.

I specialize in:

- Agentic AI Workflows
- Retrieval Augmented Generation (RAG)
- Multi-Agent Systems
- LangGraph
- AutoGen Swarm
- Vector Databases
- LLM Applications
""")

st.divider()

# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------

st.header("👨‍💻 About Me")

st.write("""
I am passionate about building practical Generative AI applications that solve real-world problems.

My focus areas include:

- Agentic AI
- Multi-Agent Systems
- Retrieval-Augmented Generation (RAG)
- Workflow Orchestration using LangGraph
- AutoGen Swarm Teams
- OpenAI Ecosystem

I enjoy creating AI solutions that combine reasoning, planning, retrieval, and autonomous decision-making.
""")

st.divider()

# ---------------------------------------------------
# SKILLS
# ---------------------------------------------------

st.header("🛠️ Technical Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("AI Frameworks")
    st.markdown("""
    - LangChain
    - LangGraph
    - AutoGen
    - CrewAI
    - Google ADK
    """)

with col2:
    st.subheader("LLM Technologies")
    st.markdown("""
    - OpenAI GPT Models
    - Embeddings
    - RAG
    - Prompt Engineering
    - Tool Calling
    """)

with col3:
    st.subheader("Backend & Storage")
    st.markdown("""
    - Python
    - FastAPI
    - Supabase
    - Vector Databases
    - Git & GitHub
    """)

st.divider()

# ---------------------------------------------------
# PROJECTS
# ---------------------------------------------------

st.header("🚀 Featured Projects")

# ===================================================
# PROJECT 1
# ===================================================

with st.container():

    st.subheader("1️⃣ Multimodal RAG Assistant")

    st.write("""
    A Retrieval-Augmented Generation (RAG) system that understands both
    text and images from web content.

    ### Key Features
    - Reads content from web URLs
    - Extracts text and images
    - Chunks and embeds content
    - Stores embeddings in Supabase Vector Store
    - Stores image metadata with relevant chunks
    - Retrieves answers with contextual images

    ### Tech Stack
    Python • LangChain • OpenAI Embeddings • Supabase • RAG
    """)

    try:
        st.video("assets/rag_demo.mp4")
    except:
        st.info("Add rag_demo.mp4 inside assets folder")

st.divider()

# ===================================================
# PROJECT 2
# ===================================================

with st.container():

    st.subheader("2️⃣ AI Travel Planner Agent")

    st.write("""
    An Agentic AI Travel Planner built using LangGraph.

    The agent collects and analyzes:

    - Travel Preferences
    - Budget Constraints
    - Hotel Options
    - Weather Conditions
    - Local Experiences
    - Destination Information

    It generates a detailed itinerary and continuously improves
    recommendations based on user feedback.

    ### Agent Capabilities
    - Dynamic Planning
    - Tool Usage
    - User Feedback Loop
    - Iterative Itinerary Optimization

    ### Tech Stack
    LangGraph • OpenAI • Python • Agentic Workflows
    """)

    try:
        st.video("assets/travel_agent_demo.mp4")
    except:
        st.info("Add travel_agent_demo.mp4 inside assets folder")

st.divider()

# ===================================================
# PROJECT 3
# ===================================================

with st.container():

    st.subheader("3️⃣ Study Buddy - AutoGen Swarm Team")

    st.write("""
    An AI-powered learning assistant built using AutoGen Swarm Teams.

    Users can upload PDF documents and interact with a team of AI agents
    designed to enhance learning.

    ### Features

    📘 Concept Explainer
    - Explains concepts directly from uploaded PDFs

    🧠 Quiz Generator
    - Creates MCQs from learning material

    ✅ Answer Validator
    - Evaluates user responses
    - Provides correct answers and feedback

    ### Multi-Agent Workflow

    Agent 1 → Content Retrieval

    Agent 2 → Concept Explanation

    Agent 3 → Quiz Generation

    Agent 4 → Answer Validation

    ### Tech Stack

    AutoGen
    Swarm Team
    OpenAI
    PDF Processing
    Python
    """)

    try:
        st.video("assets/study_buddy_demo.mp4")
    except:
        st.info("Add study_buddy_demo.mp4 inside assets folder")

st.divider()

# ---------------------------------------------------
# LEARNING JOURNEY
# ---------------------------------------------------

st.header("📚 Currently Exploring")

st.markdown("""
- Advanced Agentic AI Systems
- MCP (Model Context Protocol)
- Multi-Agent Collaboration
- AI Workflow Orchestration
- Production-Ready GenAI Applications
- Evaluation Frameworks for AI Agents
""")

st.divider()

# ---------------------------------------------------
# CONTACT
# ---------------------------------------------------

st.header("📬 Connect With Me")
gmail_url = "anithachelamuthu@gmail.com"
github_url = "https://github.com/AnithaChellamuthu"
linkedin_url = "https://www.linkedin.com/in/anitha-chelamuthu-b93757b0/"

st.markdown(f"""
🔗 Gmail: {gmail_url}

🔗 GitHub: {github_url}

🔗 LinkedIn: {linkedin_url}
""")

st.divider()

st.success("Thanks for visiting my AI Portfolio 🚀")
