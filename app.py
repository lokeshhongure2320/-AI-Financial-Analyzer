import streamlit as st
from src.pipeline.rag_pipeline import run_pipeline


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="AI Financial Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #111827 50%, #172554 100%);
        color: white;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Header */
    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        background: linear-gradient(90deg, #60a5fa, #a78bfa, #22d3ee);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 18px;
        margin-bottom: 35px;
    }

    /* Cards */
    .card {
        background: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .card h3 {
        color: #f8fafc;
        margin-bottom: 10px;
    }

    .card p {
        color: #cbd5e1;
    }

    /* Feature cards */
    .feature {
        background: rgba(255,255,255,0.06);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        height: 130px;
    }

    .feature-icon {
        font-size: 30px;
    }

    .feature-title {
        font-weight: 700;
        color: white;
        margin-top: 8px;
    }

    .feature-text {
        font-size: 13px;
        color: #94a3b8;
    }

    /* Text input */
    .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.08);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 12px;
        padding: 14px;
        font-size: 16px;
    }

    .stTextInput label {
        color: #e2e8f0 !important;
        font-weight: 600;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        background: linear-gradient(90deg, #2563eb, #7c3aed);
        color: white;
        border: none;
        font-size: 16px;
        font-weight: 700;
        transition: 0.3s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 8px 25px rgba(59,130,246,0.35);
    }

    /* Answer box */
    .answer-box {
        background: rgba(15, 23, 42, 0.75);
        border: 1px solid rgba(96,165,250,0.25);
        border-radius: 18px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    .answer-title {
        color: #60a5fa;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    .sidebar-title {
        font-size: 24px;
        font-weight: 700;
        color: #60a5fa;
    }

    .sidebar-text {
        color: #94a3b8;
        font-size: 14px;
        line-height: 1.6;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid rgba(255,255,255,0.1);
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">📊 Financial AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div class="sidebar-text">
        <b>AI Financial Analyzer</b><br><br>

        Ask questions about financial reports
        and get intelligent answers using
        Retrieval-Augmented Generation (RAG).
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 🧠 Technology")

    st.markdown(
        """
        <div class="sidebar-text">
        • Python<br>
        • Streamlit<br>
        • RAG Pipeline<br>
        • Vector Database<br>
        • Sentence Transformers<br>
        • Large Language Model
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption("AI Financial Analyzer v1.0")


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    '<div class="main-title">📊 AI Financial Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Analyze financial reports and get intelligent AI-powered insights'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Report Analysis</div>
        <div class="feature-text">Understand financial documents</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">Smart Search</div>
        <div class="feature-text">Find relevant information</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Answers</div>
        <div class="feature-text">Get intelligent responses</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Insights</div>
        <div class="feature-text">Extract financial insights</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)


# --------------------------------------------------
# QUESTION SECTION
# --------------------------------------------------
st.markdown(
    """
    <div class="card">
        <h3>💬 Ask About Your Financial Report</h3>
        <p>
        Ask questions about revenue, profit, expenses,
        financial performance, risks, or other information
        available in your report.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


query = st.text_input(
    "Your Question",
    placeholder="Example: What was the company's revenue in 2024?"
)


# --------------------------------------------------
# QUICK QUESTIONS
# --------------------------------------------------
st.markdown("### 💡 Example Questions")

q1, q2, q3 = st.columns(3)

with q1:
    if st.button("📈 What was the revenue?"):
        query = "What was the company's revenue?"

with q2:
    if st.button("💰 What was the net profit?"):
        query = "What was the company's net profit?"

with q3:
    if st.button("📊 Financial performance?"):
        query = "How was the company's financial performance?"


# --------------------------------------------------
# RUN RAG PIPELINE
# --------------------------------------------------
if query:

    with st.spinner("🤖 Analyzing financial report..."):

        try:

            result = run_pipeline(query)

            st.markdown(
                '<div class="answer-box">'
                '<div class="answer-title">🤖 AI Analysis</div>',
                unsafe_allow_html=True
            )

            st.write(result)

            st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:

            st.error(
                f"⚠️ Something went wrong while analyzing the report: {e}"
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Built with Python • Streamlit • RAG • AI
        <br>
        📊 AI Financial Analyzer
    </div>
    """,
    unsafe_allow_html=True
)