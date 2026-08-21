import streamlit as st

from src.rag import RAGRetriever
from src.classifier import SupportClassifier
from src.answer_generator import AnswerGenerator
from src.ticket_manager import TicketManager


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CloudDesk Customer Support AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background-color: #0b1020;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #080e1c;
        border-right: 1px solid #263044;
    }

    section[data-testid="stSidebar"] .block-container {
        padding: 2rem 1.2rem;
    }

    /* Main container */
    .main .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Hero */
    .hero {
        padding: 10px 0 30px 0;
    }

    .hero-title {
        font-size: 42px;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        color: #9aa9c4;
        font-size: 17px;
    }

    /* Status cards */
    .status-card {
        background: #141a29;
        border: 1px solid #29344a;
        border-radius: 12px;
        padding: 20px;
        min-height: 120px;
    }

    .status-label {
        color: #91a0bb;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    .status-value {
        font-size: 27px;
        font-weight: 600;
    }

    .online {
        color: #35d07f;
    }

    .active {
        color: #4da3ff;
    }

    .enabled {
        color: #35d07f;
    }

    /* Section titles */
    .section-title {
        font-size: 27px;
        font-weight: 650;
        margin-bottom: 5px;
    }

    .section-description {
        color: #91a0bb;
        margin-bottom: 20px;
    }

    /* Workflow cards */
    .workflow-card {
        background: #141a29;
        border: 1px solid #29344a;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .workflow-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: #2563eb;
        color: white;
        font-weight: 700;
        margin-right: 12px;
    }

    .workflow-text {
        font-size: 15px;
        color: #e8edf7;
    }

    /* Result cards */
    .success-card {
        background: #0c2921;
        border: 1px solid #167453;
        border-radius: 14px;
        padding: 22px;
        margin-top: 20px;
    }

    .success-title {
        font-size: 23px;
        font-weight: 650;
        color: #42df92;
        margin-bottom: 7px;
    }

    .success-text {
        color: #b8c8c1;
    }

    .escalation-card {
        background: #28151b;
        border: 1px solid #a53c4c;
        border-radius: 14px;
        padding: 22px;
        margin-top: 20px;
    }

    .escalation-title {
        font-size: 23px;
        font-weight: 650;
        color: #ff7b8c;
        margin-bottom: 7px;
    }

    .escalation-text {
        color: #d8b8be;
    }

    /* AI response */
    .answer-box {
        background: #102a46;
        border: 1px solid #244d76;
        border-radius: 12px;
        padding: 20px;
        color: #d9eaff;
        line-height: 1.7;
        font-size: 16px;
    }

    /* Ticket */
    .ticket-box {
        background: #111c2c;
        border: 1px solid #2d4968;
        border-radius: 12px;
        padding: 20px;
    }

    .ticket-id {
        font-size: 22px;
        font-weight: 700;
        color: #4dd4ff;
    }

    /* Metric labels */
    div[data-testid="stMetricLabel"] {
        color: #91a0bb;
    }

    div[data-testid="stMetricValue"] {
        color: #f3f6fb;
    }

    /* Button */
    .stButton > button {
        border-radius: 9px;
        font-weight: 600;
        min-height: 48px;
    }

    /* Text area */
    textarea {
        background-color: #171b28 !important;
        color: #f3f6fb !important;
        border-radius: 10px !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD SYSTEM
# ============================================================

@st.cache_resource
def load_system():

    retriever = RAGRetriever(
        "data/knowledge_base.txt"
    )

    classifier = SupportClassifier(
        retriever,
        threshold=0.30
    )

    generator = AnswerGenerator()

    ticket_manager = TicketManager()

    return retriever, classifier, generator, ticket_manager


retriever, classifier, generator, ticket_manager = load_system()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:26px;
            font-weight:700;
            margin-bottom:8px;
        ">
            ☁️ CloudDesk
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color:#91a0bb;
            line-height:1.6;
            font-size:14px;
        ">
            AI-powered customer support employee for
            Tier-1 SaaS support operations.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("System Capabilities")

    st.write("🔎 Knowledge Retrieval")
    st.write("🧠 Confidence Evaluation")
    st.write("💬 Grounded Responses")
    st.write("🚨 Human Escalation")
    st.write("🎫 Ticket Management")

    st.divider()

    st.subheader("Supported Categories")

    st.write("🔐 Account Access")
    st.write("💳 Billing")
    st.write("🛠️ Technical Support")


# ============================================================
# HERO
# ============================================================

# FIX:
# Keep the HTML elements together without blank lines that can
# cause Streamlit Markdown to interpret the content as code.

st.markdown(
    """
<div class="hero">
    <div class="hero-title">
        🤖 CloudDesk Customer Support AI
    </div>
    <div class="hero-subtitle">
        AI-powered Tier-1 support with knowledge retrieval,
        confidence-based decisions, and human escalation.
    </div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# SYSTEM STATUS
# ============================================================

status_cols = st.columns(4)

with status_cols[0]:

    st.markdown(
        """
<div class="status-card">
    <div class="status-label">System</div>
    <div class="status-value online">● ONLINE</div>
</div>
""",
        unsafe_allow_html=True
    )


with status_cols[1]:

    st.markdown(
        """
<div class="status-card">
    <div class="status-label">Knowledge Base</div>
    <div class="status-value active">● ACTIVE</div>
</div>
""",
        unsafe_allow_html=True
    )


with status_cols[2]:

    st.markdown(
        """
<div class="status-card">
    <div class="status-label">AI Engine</div>
    <div class="status-value">RAG</div>
</div>
""",
        unsafe_allow_html=True
    )


with status_cols[3]:

    st.markdown(
        """
<div class="status-card">
    <div class="status-label">Escalation</div>
    <div class="status-value enabled">● ENABLED</div>
</div>
""",
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# MAIN TWO-COLUMN LAYOUT
# ============================================================

left_col, right_col = st.columns(
    [1.55, 1],
    gap="large"
)


# ============================================================
# CUSTOMER SUPPORT
# ============================================================

with left_col:

    st.markdown(
        '<div class="section-title">💬 Customer Support</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Ask a question and let the AI determine whether it can safely resolve the request.'
        '</div>',
        unsafe_allow_html=True
    )

    question = st.text_area(
        "Customer Question",
        placeholder=(
            "Example: How do I reset my password?"
        ),
        height=130,
        key="customer_question"
    )

    submit = st.button(
        "🚀 Get Support",
        type="primary",
        use_container_width=True
    )


# ============================================================
# AI WORKFLOW
# ============================================================

with right_col:

    st.markdown(
        '<div class="section-title">🧠 AI Workflow</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'How CloudDesk processes every request'
        '</div>',
        unsafe_allow_html=True
    )

    workflow_steps = [
        "Customer submits a question",
        "RAG retrieves relevant knowledge",
        "Confidence score is calculated",
        "High-confidence requests are answered",
        "Low-confidence requests are escalated",
        "A support ticket is created"
    ]

    for i, step in enumerate(workflow_steps, start=1):

        st.markdown(
            f"""
<div class="workflow-card">
    <span class="workflow-number">{i}</span>
    <span class="workflow-text">{step}</span>
</div>
""",
            unsafe_allow_html=True
        )


# ============================================================
# PROCESS REQUEST
# ============================================================

if submit:

    if not question.strip():

        st.warning(
            "Please enter a customer question."
        )

    else:

        result = classifier.classify(
            question
        )

        confidence = result.get(
            "confidence",
            0.0
        )

        status = result.get(
            "status",
            "ESCALATE"
        )

        source = result.get(
            "source",
            ""
        )

        st.divider()


        # ====================================================
        # SUPPORTED
        # ====================================================

        if status == "SUPPORTED":

            st.markdown(
                """
<div class="success-card">
    <div class="success-title">
        ✅ Request Resolved
    </div>
    <div class="success-text">
        The AI found relevant knowledge and can
        safely answer this request.
    </div>
</div>
""",
                unsafe_allow_html=True
            )

            metric1, metric2 = st.columns(2)

            with metric1:

                st.metric(
                    "Confidence",
                    f"{confidence * 100:.1f}%"
                )

                st.progress(
                    min(max(confidence, 0.0), 1.0)
                )

            with metric2:

                try:

                    title = generator._extract_title(
                        source
                    )

                except Exception:

                    title = "Knowledge Base"

                st.metric(
                    "Knowledge Source",
                    title
                )


            st.subheader("🤖 AI Response")

            answer = generator.generate(
                question,
                source
            )

            # Render generated answer as normal Streamlit Markdown
            # instead of injecting it directly into HTML.
            st.markdown(
                '<div class="answer-box">'
                + answer
                + '</div>',
                unsafe_allow_html=True
            )


            with st.expander(
                "📚 View Retrieved Knowledge"
            ):

                st.write(source)


        # ====================================================
        # ESCALATION
        # ====================================================

        else:

            st.markdown(
                """
<div class="escalation-card">
    <div class="escalation-title">
        🚨 Human Escalation Required
    </div>
    <div class="escalation-text">
        The AI could not confidently answer
        this request from the knowledge base.
    </div>
</div>
""",
                unsafe_allow_html=True
            )

            metric1, metric2 = st.columns(2)

            with metric1:

                st.metric(
                    "Confidence",
                    f"{confidence * 100:.1f}%"
                )

            with metric2:

                st.metric(
                    "Status",
                    "OPEN"
                )


            # =================================================
            # CREATE TICKET
            # =================================================

            ticket = None

            try:

                ticket = ticket_manager.create_ticket(
                    customer_query=question,
                    category="General / Out of Scope",
                    priority="Medium",
                    reason=(
                        "The retrieved knowledge did not "
                        "meet the confidence threshold."
                    )
                )

            except TypeError:

                try:

                    ticket = ticket_manager.create_ticket(
                        question
                    )

                except Exception:

                    ticket = None

            except Exception:

                ticket = None


            # =================================================
            # TICKET DISPLAY
            # =================================================

            st.subheader("🎫 Support Ticket")

            if ticket:

                if isinstance(ticket, dict):

                    ticket_id = ticket.get(
                        "ticket_id",
                        ticket.get(
                            "id",
                            "Ticket Created"
                        )
                    )

                    ticket_status = ticket.get(
                        "status",
                        "OPEN"
                    )

                    category = ticket.get(
                        "category",
                        "General / Out of Scope"
                    )

                    priority = ticket.get(
                        "priority",
                        "Medium"
                    )

                    created_at = ticket.get(
                        "created_at",
                        ""
                    )

                else:

                    ticket_id = str(ticket)
                    ticket_status = "OPEN"
                    category = "General / Out of Scope"
                    priority = "Medium"
                    created_at = ""

                st.success(
                    f"Ticket {ticket_id} has been created for human support."
                )

                t1, t2 = st.columns(2)

                with t1:

                    st.markdown(
                        "### Ticket ID"
                    )

                    st.markdown(
                        f"""
<div class="ticket-box">
    <div class="ticket-id">
        {ticket_id}
    </div>
</div>
""",
                        unsafe_allow_html=True
                    )

                with t2:

                    st.markdown(
                        "### Status"
                    )

                    st.write(
                        ticket_status
                    )

                    st.markdown(
                        "### Priority"
                    )

                    st.write(
                        priority
                    )


                t3, t4 = st.columns(2)

                with t3:

                    st.markdown(
                        "### Category"
                    )

                    st.write(
                        category
                    )

                with t4:

                    st.markdown(
                        "### Created At"
                    )

                    st.write(
                        created_at
                    )


                st.markdown(
                    "### Customer Query"
                )

                st.info(
                    question
                )

                st.markdown(
                    "### Escalation Reason"
                )

                st.write(
                    "The retrieved knowledge did not meet "
                    "the confidence threshold."
                )

            else:

                st.warning(
                    "The request requires human support, "
                    "but the ticket could not be created."
                )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "CloudDesk Customer Support AI • "
    "RAG + Confidence-Based Escalation + Ticket Management"
)