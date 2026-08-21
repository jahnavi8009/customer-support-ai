# 🤖 CloudDesk Customer Support AI

An AI-powered Tier-1 customer support assistant built using
Retrieval-Augmented Generation (RAG), confidence-based
classification, and human escalation.

## 🚀 Overview

CloudDesk Customer Support AI helps automate Tier-1 customer
support requests.

The system retrieves relevant information from a customer
support knowledge base and determines whether the request can
be confidently answered.

If the system has sufficient confidence, it generates a
grounded response using the retrieved knowledge.

If the confidence is below the defined threshold, the request
is escalated to human support and a support ticket is created.

---

## ✨ Features

- 🔎 Retrieval-Augmented Generation (RAG)
- 🧠 Confidence-based request classification
- 💬 Grounded AI responses
- 🚨 Automatic human escalation
- 🎫 Support ticket creation
- 📚 Knowledge-base retrieval
- 📊 Confidence score display
- 🖥️ Interactive Streamlit interface
- 🔐 Environment-variable based API key configuration

---

## 🏗️ System Architecture

```text
Customer Question
        │
        ▼
┌─────────────────────┐
│   RAG Retriever     │
│ Knowledge Retrieval │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Support Classifier  │
│ Confidence Scoring  │
└──────────┬──────────┘
           │
      ┌────┴────┐
      │         │
      ▼         ▼
 SUPPORTED   ESCALATE
      │         │
      ▼         ▼
 AI Response  Ticket
      │         │
      └────┬────┘
           ▼
      Streamlit UI