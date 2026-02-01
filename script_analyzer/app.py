import streamlit as st
import os
from utils.script_loader import load_script
from utils.groq_client import call_groq
from utils.prompts import story_structure_prompt, overall_suggestion_prompt

from utils.emotion_tracker import generate_emotional_graph
from utils.analysis_parser import parse_analysis_sections



# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    local_css("assets/styles.css")
except FileNotFoundError:
    pass # CSS file might not exist yet or path issue, not critical

st.set_page_config(
    page_title="AI Script Analyzer",
    layout="wide"
)

st.title("🎬 AI Script Analyzer for Directors")
st.markdown("## 🧠 Story Structure Analysis")
st.caption(
    "Includes Character Arcs, Story Structures, Production Needs (VFX/Stunts), and Emotional Graph"
)




# Check for API Key
if not os.getenv("GROQ_API_KEY"):
    st.warning("⚠️ GROQ_API_KEY environment variable is not set. Please set it to use the analyzer.")

uploaded_file = st.file_uploader(
    "Upload your movie script (.txt or .pdf)",
    type=["txt", "pdf"]
)

if uploaded_file:
    with st.spinner("Reading script..."):
        try:
            script_text = load_script(uploaded_file)
            st.success("Script loaded successfully!")
        except Exception as e:
            st.error(f"Error loading script: {e}")
            script_text = None

    if script_text:
        # Initialize session state for analysis if not present
        if "analysis_result" not in st.session_state:
            st.session_state.analysis_result = None
        if "analyzed_script" not in st.session_state:
            st.session_state.analyzed_script = None

        if st.button("Run Full Story Structure Analysis"):
            if not os.getenv("GROQ_API_KEY"):
                st.error("Please set the GROQ_API_KEY environment variable.")
            else:
                with st.spinner("Breaking down narrative structures and production requirements..."):
                    try:
                        prompt = story_structure_prompt(script_text)
                        analysis = call_groq(prompt)
                        # Store in session state
                        st.session_state.analysis_result = analysis
                        st.session_state.analyzed_script = script_text
                    except Exception as e:
                        st.error(f"An error occurred during analysis: {e}")
        
        # Display results if available in session state
        if st.session_state.analysis_result and st.session_state.analyzed_script == script_text:
            analysis = st.session_state.analysis_result
            st.markdown("## 📖 Story Structure Report")
                        
            # Parse the analysis into sections
            sections = parse_analysis_sections(analysis)
            
            # Display Executive Snapshot at the Top (if found)
            snapshot_key = next((k for k in sections.keys() if "EXECUTIVE SNAPSHOT" in k.upper()), None)
            if snapshot_key:
                st.markdown(f"## {snapshot_key}")
                st.markdown(sections[snapshot_key])
                st.markdown("---")
                # Remove it from tabs list so it doesn't duplicate
                del sections[snapshot_key]

            if len(sections) > 0:
                # Create tabs for remaining sections
                
                # Check for specific keys to handle intelligently
                emotional_graph_key = next((k for k in sections.keys() if "EMOTIONAL GRAPH" in k.upper()), None)
                
                tab_names = list(sections.keys())
                # Ensure Emotional Graph tab exists if we want to show graph separately
                if not emotional_graph_key and "Emotional Graph" not in tab_names:
                    tab_names.append("Emotional Graph")
                
                tabs = st.tabs(tab_names)
                
                for i, key in enumerate(tab_names):
                    with tabs[i]:
                        if key in sections:
                            st.markdown(f"### {key}")
                            st.markdown(sections[key])
                            
                            # Special handling for Emotional Graph Tab
                            if key == emotional_graph_key:
                                st.markdown("---")
                                st.markdown("#### Visual Graph")
                                with st.spinner("Generating emotional graph..."):
                                    try:
                                        fig = generate_emotional_graph(script_text)
                                        if fig:
                                            st.pyplot(fig)
                                        else:
                                            st.warning("Could not generate graph. Script text might be too short.")
                                    except Exception as e:
                                            st.error(f"Error generating graph: {e}")
                        
                        # Fallback for manual Emotional Graph tab
                        elif key == "Emotional Graph":
                            st.markdown("### Character Emotional Graph")
                            with st.spinner("Generating emotional graph..."):
                                try:
                                    fig = generate_emotional_graph(script_text)
                                    if fig:
                                        st.pyplot(fig)
                                    else:
                                        st.warning("Could not generate graph. Script text might be too short.")
                                except Exception as e:
                                        st.error(f"Error generating graph: {e}")

            else:
                # Fallback to plain markdown
                st.markdown(analysis)
            
            # AI Suggestions Section
            st.markdown("---")
            st.markdown("### 🤖 AI Suggestions for Improvement")
            st.caption("Get tailored suggestions based on the analysis above.")
            
            if st.button("Get AI Suggestions"):
                with st.spinner("Analyzing script for improvements..."):
                    try:
                        # We use the full analysis as context for the suggestions
                        suggestion_prompt = overall_suggestion_prompt(script_text, analysis)
                        suggestions = call_groq(suggestion_prompt)
                        
                        st.markdown("### 🚀 AI Suggestions")
                        st.markdown(suggestions)
                    except Exception as e:
                        st.error(f"Error generating suggestions: {e}")



st.markdown("---")
st.markdown("### UX Notes")
st.markdown("- One feature at a time → no overwhelm")
st.markdown("- Directors see story logic first")
st.markdown("- Output is presentation-ready")
