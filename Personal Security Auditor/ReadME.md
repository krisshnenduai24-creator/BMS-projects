# 🛡️ Sentinel AI: Personal Security Auditor

**Sentinel AI** is a specialized security companion designed to detect and mitigate digital threats using a hybrid AI approach. Unlike standard chatbots, Sentinel focuses on **behavioral auditing**, identifying the psychological manipulation behind phishing attempts, and protecting user privacy.

---

## 🌟 Key Features

- **🔍 Threat Auditor**: Uses the **Gemini 3 Flash** model to analyze emails and messages for "Urgency Bias," "Authority Mimicry," and other social engineering red flags.
- **🎮 Scam Simulator**: An interactive "Security Sandbox" that uses **Session State** to simulate live attacks and evaluate user security reflexes.
- **🔐 Privacy Shield**: A deterministic **Regex-based scanner** that identifies PII (Personally Identifiable Information) before it is shared online.

---

## 🛠️ Technical Stack

- **Language:** Python 3.11+
- **AI Engine:** Google Generative AI (Gemini 3 Flash)
- **Frontend:** Streamlit
- **Logic:** Hybrid (Probabilistic LLM + Deterministic Regular Expressions)

---

## 🚀 Getting Started

Follow these steps to run Sentinel AI on your local machine.

### 1. Prerequisites
Ensure you have Python installed. You will also need a **Google AI Studio API Key**.
- Get a free key at [Google AI Studio](https://aistudio.google.com/).

### 2. Installation
Clone this repository and navigate to the project folder:
cd sentinel-ai

Install the required dependencies:

Bash
pip install streamlit google-generativeai
3. Running the App
Launch the Streamlit dashboard:

Bash
streamlit run sentinel_ai.py
🏗️ Architecture
Sentinel AI is built on a Hybrid AI Architecture:

The Brain (LLM): Handles complex reasoning and linguistic patterns to detect deception.

The Guardrail (Regex): Handles strict pattern matching for data privacy, ensuring zero false negatives for formatted data like emails or phone numbers.

👥 Contributors
Person A: AI Architect (Prompt Engineering, API Logic, Regex Development)

Person B: Systems Engineer (Streamlit UI, Session State Management, Security Scenarios)