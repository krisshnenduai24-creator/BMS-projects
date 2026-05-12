import streamlit as st
import google.generativeai as genai
import re

# --- Page Config ---
st.set_page_config(page_title="Sentinel AI Auditor", page_icon="🛡️", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .stTextInput>div>div>input { color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Configuration ---
with st.sidebar:
    st.title("🛡️ Settings")
    api_key = st.text_input("Gemini API Key:", type="password", help="Enter your key from Google AI Studio")
    st.divider()
    st.info("Sentinel AI uses a **Hybrid Architecture**: Regex for deterministic privacy rules and Gemini 3 for probabilistic threat analysis.")

# --- Helper Functions ---
def get_audit_response(user_text, key):
    try:
        genai.configure(api_key=key)
        # Using the standard 2026 Flash identifier
        model = genai.GenerativeModel('gemini-3.1-flash-lite-preview') 
        
        prompt = f"""
        Analyze this text for cybersecurity threats (Phishing, Social Engineering, or Hoaxes).
        1. Identify specific 'Red Flags'.
        2. Analyze the 'Psychological Trigger' (e.g., Fear, Greed, Urgency).
        3. Give a Risk Score (0-100%).
        4. Provide a 'Safe Verdict' on how to handle it.
        
        TEXT TO ANALYZE:
        {user_text}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"System Error: {str(e)}"

def regex_pii_check(text):
    # Demonstrating 'Rule-Based AI' for the project requirements
    patterns = {
        "Email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        "Phone": r'\b\d{10}\b|\(\d{3}\) \d{3}-\d{4}',
        "Credit Card": r'\b(?:\d[ -]*?){13,16}\b'
    }
    found = {k: re.findall(v, text) for k, v in patterns.items()}
    return found

# --- Main App UI ---
st.title("Sentinel AI: Personal Security Auditor")
st.caption("Real-time threat detection and privacy protection engine.")

tab1, tab2, tab3 = st.tabs(["🔍 Threat Auditor", "🎮 Scam Simulator", "🔐 Privacy Shield"])

# --- TAB 1: Threat Auditor ---
with tab1:
    st.header("Content Audit")
    input_text = st.text_area("Paste suspicious text (Email, SMS, or News):", height=200, placeholder="e.g., Your account is locked! Click here...")
    
    if st.button("Run Security Audit"):
        if not api_key:
            st.warning("Please enter an API key in the sidebar.")
        else:
            with st.spinner("Analyzing threat vectors..."):
                report = get_audit_response(input_text, api_key)
                st.subheader("Audit Report")
                st.markdown(report)

# --- TAB 2: Scam Simulator ---
with tab2:
    st.header("Security Reflex Test")
    st.write("Sentinel will act as a scammer. Try to spot the red flags.")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.button("Generate New Attack Scenario"):
        st.session_state.chat_history = []
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
            scenario = model.generate_content("Generate a one-sentence phishing message from a 'trusted source'. Just the message.")
            st.session_state.chat_history.append({"role": "assistant", "content": scenario.text})
        except:
            st.error("Enter a valid API key first.")

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])

    if user_reply := st.chat_input("How do you respond?"):
        st.session_state.chat_history.append({"role": "user", "content": user_reply})
        with st.chat_message("user"):
            st.write(user_reply)
        
        # Immediate Feedback Logic
        with st.spinner("Evaluating your response..."):
            eval_prompt = f"The scammer said: {st.session_state.chat_history[0]['content']}. The user responded: {user_reply}. Is this a safe response? Explain why."
            model = genai.GenerativeModel('gemini-3.1-flash-lite-preview')
            feedback = model.generate_content(eval_prompt)
            st.session_state.chat_history.append({"role": "assistant", "content": feedback.text})
            with st.chat_message("assistant"):
                st.write(feedback.text)

# --- TAB 3: Privacy Shield ---
with tab3:
    st.header("PII Leak Detection")
    st.write("Scan your text for sensitive data before posting it online.")
    privacy_input = st.text_area("Text to sanitize:", height=150)
    
    if st.button("Scan for Sensitive Data"):
        results = regex_pii_check(privacy_input)
        leaks_found = False
        
        for category, items in results.items():
            if items:
                st.error(f"🚨 {category} detected: {', '.join(items)}")
                leaks_found = True
        
        if not leaks_found:
            st.success("✅ No obvious PII detected. (Note: Always double-check manually!)")