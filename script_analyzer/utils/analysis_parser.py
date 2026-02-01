import re

def parse_analysis_sections(analysis_text):
    """
    Parses the LLM analysis text into a dictionary of sections.
    Expects headers in the format:
    ========================
    N. SECTION TITLE
    ========================
    """
    sections = {}
    
    # Regex to find the headers
    # Pattern looks for lines starting with ===, a number.title, then ===
    # We capture the Title and the Content following it.
    
    # Split by the separator lines
    # This acts as a rough split.
    # A improved regex approach:
    
    pattern = r"={24}\n\d+\.\s*(.*?)\n={24}\n(.*?)(?=\n={24}|$)"
    
    matches = re.findall(pattern, analysis_text, re.DOTALL)
    
    if not matches:
        # Fallback if strict formatting fails: return full text as "Full Report"
        return {"Full Report": analysis_text}
    
    for title, content in matches:
        clean_title = title.strip()
        clean_content = content.strip()
        sections[clean_title] = clean_content
        
    return sections

def extract_production_requirements(analysis_text):
    """
    Specific helper to extract just the production requirements if needed.
    """
    sections = parse_analysis_sections(analysis_text)
    # flexible search
    for key in sections:
        if "PRODUCTION REQUIREMENTS" in key.upper() or "VFX" in key.upper():
            return sections[key]
    return None
