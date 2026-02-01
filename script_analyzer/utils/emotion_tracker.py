import matplotlib.pyplot as plt
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib

# Use a non-interactive backend for streamit compatibility logic if needed, 
# although streamlit's logic usually handles pyplot well.
# We'll stick to standard pyplot usage as requested.

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """Analyze sentiment of text and return a compound score (-1 to 1)."""
    sentiment = analyzer.polarity_scores(text)
    return sentiment['compound']

def split_script_into_scenes(script_text):
    """
    Splits the script into scenes based on heuristics.
    Simple approach: Split by double newlines or common scene headers if detectable.
    For this implementation, we'll try to split by 'EXT.' and 'INT.' if present, 
    otherwise we fall back to paragraph-based splitting.
    """
    
    # Check if standard scene headers are likely present
    if "INT." in script_text or "EXT." in script_text:
        # Very naive split - in a real production app we'd use regex
        # This keeps the separator.
        import re
        # Split by INT. or EXT. at start of line
        scenes = re.split(r'(?=\n(?:INT\.|EXT\.))', script_text)
        # Filter out empty strings
        scenes = [s.strip() for s in scenes if s.strip()]
        if len(scenes) > 1:
            return scenes

    # Fallback: Split by double distinct newlines (paragraphs)
    # Group every N paragraphs into a "scene" to avoid too much noise?
    # For now, let's treat every substantial block as a scene/beat.
    paragraphs = [p.strip() for p in script_text.split('\n\n') if p.strip()]
    return paragraphs

def generate_emotional_graph(script_text):
    """
    Generates a matplotlib figure showing the emotional arc of the script.
    """
    scenes = split_script_into_scenes(script_text)
    
    # If script is too short or split failed effectively
    if not scenes:
        return None

    # Step 1: Analyze sentiment for each scene
    emotion_scores = [analyze_sentiment(scene) for scene in scenes]

    # Step 2: Prepare data for plotting
    scene_numbers = list(range(1, len(scenes) + 1))
    data = {'Scene': scene_numbers, 'Emotion Score': emotion_scores}

    # Convert to a DataFrame (not strictly necessary but good practice as per user request)
    df = pd.DataFrame(data)

    # Step 3: Plot the emotional graph
    # Create figure explicitly to return it
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Plot line
    ax.plot(df['Scene'], df['Emotion Score'], marker='o', color='b', linestyle='-', linewidth=2, markersize=6)

    # Adding titles and labels
    ax.set_title("Character Emotional Progression Over Scenes", fontsize=14)
    ax.set_xlabel("Scene / Beat Number", fontsize=12)
    ax.set_ylabel("Emotional Score (Range: -1 to 1)", fontsize=12)
    ax.grid(True)
    
    # Customize x-ticks to not be too crowded
    if len(scenes) > 20:
        ax.xaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True, nbins=20))
    else:
        ax.set_xticks(df['Scene'])

    # Marking major shifts? Maybe too messy for user if many scenes.
    # We will skip textual annotation of every point to avoid clutter if many scenes.

    plt.tight_layout()
    
    return fig
