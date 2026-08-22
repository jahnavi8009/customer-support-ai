import streamlit as st

from src.rag import RAGRetriever
from src.classifier import SupportClassifier
from src.answer_generator import AnswerGenerator
from src.ticket_manager import TicketManager


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CloudDesk Customer Support AI",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }

    .status-card {
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
    }

    .supported-card {
        border: 1px solid #2e8b57;
        background-color: rgba(46, 139, 87, 0.08);
    }

    .escalation-card {
        border: 1px solid #d9534f;
        background-color: rgba(217, 83, 79, 0.08);
    }

    .ticket-card {
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.3);
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# LOAD BACKEND COMPONENTS
# --------------------------------------------------

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

    return (
        retriever,
        classifier,
        generator,
        ticket_manager
    )


(
    retriever,
    classifier,
    generator,
    ticket_manager
) = load_system()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 CloudDesk Customer Support AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered Tier-1 support with knowledge retrieval, '
    'confidence-based decisions, and human escalation.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "System",
        "ONLINE"
    )

with col2:
    st.metric(
        "Knowledge Base",
        "ACTIVE"
    )

with col3:
    st.metric(
        "AI Mode",
        "RAG"
    )

with col4:
    st.metric(
        "Escalation",
        "ENABLED"
    )


st.divider()


# --------------------------------------------------
# MAIN LAYOUT
# --------------------------------------------------

left, right = st.columns(
    [1.5, 1]
)


# ==================================================
# LEFT COLUMN — CUSTOMER QUERY
# ==================================================

with left:

    st.subheader(
        "💬 Customer Support"
    )

    question = st.text_area(
        "Customer Question",
        placeholder=(
            "Example:\n"
            "I was charged twice for my subscription."
        ),
        height=150
    )

    submit = st.button(
        "🚀 Get Support",
        type="primary",
        use_container_width=True
    )


    # ----------------------------------------------
    # PROCESS REQUEST
    # ----------------------------------------------

    if submit:

        if not question.strip():

            st.warning(
                "Please enter a customer question."
            )

        else:

            result = classifier.classify(
                question
            )

            confidence = result["confidence"]

            st.divider()


            # ======================================
            # SUPPORTED
            # ======================================

            if result["status"] == "SUPPORTED":

                st.markdown(
                    """
                    <div class="status-card supported-card">
                    <h3>✅ Request Supported</h3>
                    <p>
                    The AI found relevant information in
                    the CloudDesk knowledge base.
                    </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Confidence",
                        f"{confidence * 100:.1f}%"
                    )

                with col2:

                    title = generator._extract_title(
                        result["source"]
                    )

                    st.metric(
                        "Knowledge Source",
                        title
                    )


                st.subheader(
                    "🤖 AI Response"
                )

                answer = generator.generate(
                    question,
                    result["source"]
                )

                st.info(
                    answer
                )


                with st.expander(
                    "📚 View Retrieved Knowledge"
                ):

                    st.write(
                        result["source"]
                    )


            # ======================================
            # ESCALATION
            # ======================================

            else:

                st.markdown(
                    """
                    <div class="status-card escalation-card">
                    <h3>🚨 Human Escalation Required</h3>
                    <p>
                    The AI could not confidently answer
                    this request from the knowledge base.
                    </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Confidence",
                        f"{confidence * 100:.1f}%"
                    )

                with col2:

                    st.metric(
                        "Status",
                        "OPEN"
                    )


                # ----------------------------------
                # CREATE TICKET
                # ----------------------------------

                ticket = ticket_manager.create_ticket(

                    customer_query=question,

                    reason=(
                        "The retrieved knowledge did not "
                        "meet the confidence threshold."
                    ),

                    confidence=confidence,

                    category="General / Out of Scope",

                    priority="Medium"
                )


                st.subheader(
                    "🎫 Support Ticket Created"
                )


                st.success(
                    f"Ticket {ticket['ticket_id']} "
                    "has been created for human support."
                )


                col1, col2 = st.columns(2)

                with col1:

                    st.write("**Ticket ID**")

                    st.code(
                        ticket["ticket_id"]
                    )

                    st.write("**Category**")

                    st.write(
                        ticket["category"]
                    )

                    st.write("**Priority**")

                    st.write(
                        ticket["priority"]
                    )


                with col2:

                    st.write("**Status**")

                    st.write(
                        ticket["status"]
                    )

                    st.write("**Created At**")

                    st.write(
                        ticket["created_at"]
                    )


                st.write(
                    "**Customer Query**"
                )

                st.info(
                    ticket["customer_query"]
                )

                st.write(
                    "**Escalation Reason**"
                )

                st.write(
                    ticket["reason"]
                )


# ==================================================
# RIGHT COLUMN — SYSTEM INFORMATION
# ==================================================

with right:

    st.subheader(
        "🧠 AI Workflow"
    )

    st.write(
        "The system follows a safe support workflow:"
    )

    st.write(
        "1️⃣ Customer submits a question"
    )

    st.write(
        "2️⃣ RAG retrieves relevant knowledge"
    )

    st.write(
        "3️⃣ Confidence score is calculated"
    )

    st.write(
        "4️⃣ Supported questions receive an answer"
    )

    st.write(
        "5️⃣ Low-confidence questions are escalated"
    )

    st.write(
        "6️⃣ A support ticket is created"
    )


    st.divider()


    st.subheader(
        "📚 Supported Categories"
    )

    st.write(
        "🔐 Account Access"
    )

    st.write(
        "💳 Billing"
    )

    st.write(
        "🛠️ Technical Support"
    )


    st.divider()


    st.subheader(
        "🎫 Ticket Dashboard"
    )

    tickets = ticket_manager.get_tickets()

    if not tickets:

        st.caption(
            "No support tickets created yet."
        )

    else:

        st.metric(
            "Open Tickets",
            len(tickets)
        )

        for ticket in reversed(tickets):

            with st.expander(
                f"{ticket['ticket_id']} • "
                f"{ticket['status']}"
            ):

                st.write(
                    "**Customer:**",
                    ticket["customer_query"]
                )

                st.write(
                    "**Category:**",
                    ticket["category"]
                )

                st.write(
                    "**Priority:**",
                    ticket["priority"]
                )

                st.write(
                    "**Confidence:**",
                    f"{ticket['confidence'] * 100:.1f}%"
                )

                st.write(
                    "**Created:**",
                    ticket["created_at"]
                )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "CloudDesk Customer Support AI • "
    "RAG + Confidence-Based Escalation + Ticket Management"
)