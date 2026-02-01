def story_structure_prompt(script_text):
    return f"""
You are an expert AI script analyst and story development consultant for film directors.

Analyze the following movie script and generate a DIRECTORIAL STORY STRUCTURE REPORT.
Format the output for quick reading: clear headings, tables for data, and bullet points.

========================
1. EXECUTIVE SNAPSHOT
========================
**Logline:** [One powerful sentence]

**Genre:** [Genre]
**Tone:** [Tone descriptors]
**Target Audience:** [Audience]

**Story Health:** [🟢 Strong | 🟡 Needs Work | 🔴 Risky]
**Pacing:** [Brief summary, e.g., Fast Act I • Heavy Mid-Act II • Strong Climax]

========================
2. CHARACTER OVERVIEW
========================
### Main Characters
| Character | Role | Goal | Emotional Arc |
|-----------|------|------|---------------|
| [Name] | [Role] | [Brief Goal] | [Start] → [End] |
(Add rows for all key characters)

### Character Arcs & Psychology
For each main character:
- **[Name] ([Role])**
    - Starting State: ...
    - Core Wound: ...
    - Key Turning Point: ...
    - End State: ...

========================
3. THREE-ACT STRUCTURE
========================
### ACT I – Setup
- **Ordinary World:** ...
- **Inciting Incident:** ...
- **Dramatic Question:** ...

### ACT II – Confrontation
- **Rising Complications:** ...
- **Midpoint:** ...
- **Stakes Escalation:** ...

### ACT III – Resolution
- **Climax:** ...
- **Transformation:** ...
- **Closure:** ...

========================
4. FIVE-ACT STRUCTURE
========================
- **Act I (Exposition):** ...
- **Act II (Rising Action):** ...
- **Act III (Climax/Reversal):** ...
- **Act IV (Falling Action):** ...
- **Act V (Denouement):** ...

========================
5. SAVE THE CAT BEAT SHEET
========================
1. **Opening Image:** ...
2. **Theme Stated:** ...
3. **Set-Up:** ...
4. **Catalyst:** ...
5. **Debate:** ...
6. **Break into Act II:** ...
7. **B Story:** ...
8. **Fun and Games:** ...
9. **Midpoint:** ...
10. **Bad Guys Close In:** ...
11. **All Is Lost:** ...
12. **Dark Night of the Soul:** ...
13. **Break into Act III:** ...
14. **Finale:** ...
15. **Final Image:** ...

========================
6. DAN HARMON STORY CIRCLE
========================
1. **You:** ...
2. **Need:** ...
3. **Go:** ...
4. **Search:** ...
5. **Find:** ...
6. **Take:** ...
7. **Return:** ...
8. **Change:** ...

========================
7. CHARACTER EMOTIONAL GRAPH
========================
- Track the emotional state of the main character(s) through key scenes.
- **Key Emotional Beats**:
    - Lowest Point: ...
    - Emotional Peak: ...
    - Flat Areas: ...

========================
8. PRODUCTION REQUIREMENTS
========================
### ✨ Visual Effects (VFX)
| Scene | Type | Description | Intensity |
|-------|------|-------------|-----------|
| [Scene #] | [Type] | [Brief Desc] | [Low/Med/High] |

### 🤸 Stunts
| Scene | Stunt | Risk Level |
|-------|-------|------------|
| [Scene #] | [Brief Desc] | [Low/Med/High] |

### 👥 Extras
| Scene | Context | Count |
|-------|---------|-------|
| [Scene #] | [Brief Desc] | [Count] |

========================
9. STRUCTURAL RISKS
========================
- [Risk 1]
- [Risk 2]

========================
10. DIRECTORIAL PRIORITIES
========================
**High Priority**
- ...

**Medium Priority**
- ...

**Low Priority**
- ...

SCRIPT:
\"\"\" 
{script_text}
\"\"\"
"""

def overall_suggestion_prompt(script_text, analysis_summary):
    return f"""
You are an expert AI script consultant and editor. Based on the following comprehensive analysis of the script, provide the director with tailored suggestions for improving the narrative flow, emotional pacing, character development, and production requirements.

========================
PREVIOUS ANALYSIS CONTEXT:
========================
{analysis_summary}

========================
YOUR TASK:
========================
1. **Story Structure Suggestions**: Provide feedback on pacing, plot holes, and areas where the structure feels weak or rushed.
2. **Emotional Flow Suggestions**: Identify any issues with emotional highs/lows, suggest where emotional beats can be heightened, and where pacing might need to slow down or speed up.
3. **Character Development Suggestions**: Offer advice on character arcs, whether any characters feel underdeveloped or need more emotional depth, and whether the character's goals are clearly defined.
4. **VFX, Stunt, and Extras Recommendations**: Advise on the appropriate use of visual effects, stunts, and extras, based on the script’s narrative requirements.
5. **Overall Pacing and Engagement Suggestions**: Provide a summary of pacing throughout the entire script, and recommend improvements to keep the audience engaged.

Your tone should be **concise**, **professional**, and **actionable**. Avoid generic feedback and be specific to the scenes and story elements provided.
"""
