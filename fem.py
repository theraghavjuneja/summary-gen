import streamlit as st
import matplotlib.pyplot as plt

# Introduction
st.title("Gemini API Model Variants and MMLU Scores")
st.markdown("""
This app provides an overview of the different Gemini model variants, their attributes, and displays the MMLU scores of various models.
""")

# Model Variants
st.header("Model Variants")
st.markdown("""
The Gemini API offers different models that are optimized for specific use cases. Here's a brief overview of Gemini variants that are available:
""")

variants = {
    "Gemini 1.5 Pro": {
        "Model variant": "gemini-1.5-pro",
        "Input(s)": "Audio, images, videos, and text",
        "Output": "Text",
        "Optimized for": "Complex reasoning tasks such as code and text generation, text editing, problem solving, data extraction and generation"
    },
    "Gemini 1.5 Flash": {
        "Model variant": "gemini-1.5-flash",
        "Input(s)": "Audio, images, videos, and text",
        "Output": "Text",
        "Optimized for": "Fast and versatile performance across a diverse variety of tasks"
    },
    "Gemini 1.0 Pro": {
        "Model variant": "gemini-1.0-pro",
        "Input(s)": "Text",
        "Output": "Text",
        "Optimized for": "Natural language tasks, multi-turn text and code chat, and code generation"
    },
    "Gemini 1.0 Pro Vision (Deprecated)": {
        "Model variant": "gemini-pro-vision",
        "Input(s)": "Images, videos, and text",
        "Output": "Text",
        "Optimized for": "Visual-related tasks, like generating image descriptions or identifying objects in images"
    },
    "Text Embedding": {
        "Model variant": "text-embedding-004",
        "Input(s)": "Text",
        "Output": "Text embeddings",
        "Optimized for": "Measuring the relatedness of text strings"
    }
}

for variant, details in variants.items():
    st.subheader(variant)
    st.table(details)

# Attributes Table
st.header("Common Attributes")
st.markdown("""
The following table describes the attributes of the Gemini models which are common to all model variants:
""")

attributes = {
    "Attribute": ["Training data", "Supported languages", "Configurable model parameters"],
    "Description": [
        "Gemini's knowledge cutoff is November 2023. Knowledge about events after that time is limited.",
        "[See available languages](#)",
        "Top p, Top k, Temperature, Stop sequence, Max output length, Number of response candidates\n\nNote: The configurable parameters apply only to the text and chat model variations, but not embeddings."
    ]
}

st.table(attributes)

# Detailed Model Descriptions
st.header("Detailed Model Descriptions")

models_details = {
    "Gemini 1.5 Pro": """
Gemini 1.5 Pro is a mid-size multimodal model that is optimized for a wide-range of reasoning tasks such as:
- Code generation
- Text generation
- Text editing
- Problem solving
- Recommendations generation
- Information extraction
- Data extraction or generation
- Creation of AI agents

1.5 Pro can process large amounts of data at once, including 1 hour of video, 9.5 hours of audio, codebases with over 30,000 lines of code or over 700,000 words.
1.5 Pro is capable of handling zero-, one-, and few-shot learning tasks.

**Model details**
- **Model code**: models/gemini-1.5-pro-latest
- **Inputs**: Audio, images, video, and text
- **Output**: Text
- **Supported generation methods**: generateContent
- **Input token limit**: 1,048,576
- **Output token limit**: 8,192
- **Maximum number of images per prompt**: 3,600
- **Maximum video length**: 1 hour
- **Maximum audio length**: Approximately 9.5 hours
- **Maximum number of audio files per prompt**: 1
- **Model safety**: Automatically applied safety settings which are adjustable by developers. See our page on safety settings for details.
- **Rate limits**:
  - Free: 2 RPM, 32,000 TPM, 50 RPD, 46,080,000 TPD
  - Pay-as-you-go: 360 RPM, 2 million TPM, 10,000 RPD, 14,400,000,000 TPD
  - Two million context: 1 RPM, 2 million TPM, 50 RPD
- **System instructions**: Supported
- **JSON mode**: Supported
- **Latest version**: gemini-1.5-pro-latest
- **Latest stable version**: gemini-1.5-pro
- **Stable versions**: gemini-1.5-pro-001
- **Latest update**: May 2024
""",
    "Gemini 1.5 Flash": """
Gemini 1.5 Flash is a fast and versatile multimodal model for scaling across diverse tasks.

**Model details**
- **Model code**: gemini-1.5-flash-latest
- **Input(s)**: Audio, images, video, and text
- **Output**: Text
- **Supported generation methods**: generateContent
- **Input token limit**: 1,048,576
- **Output token limit**: 8,192
- **Maximum number of images per prompt**: 3,600
- **Maximum video length**: 1 hour
- **Maximum audio length**: Approximately 9.5 hours
- **Maximum number of audio files per prompt**: 1
- **Model safety**: Automatically applied safety settings which are adjustable by developers. See our page on safety settings for details.
- **Rate limits**:
  - Free: 15 RPM, 1 million TPM, 1500 RPD
  - Pay-as-you-go: 1000 RPM, 2 million TPM
- **System instructions**: Supported
- **JSON mode**: Supported
- **Model tuning**: Coming soon
- **Latest version**: gemini-1.5-flash-latest
- **Latest stable version**: gemini-1.5-flash
- **Stable versions**: gemini-1.5-flash-001
- **Latest update**: May 2024
""",
    "Gemini 1.0 Pro": """
Gemini 1.0 Pro is an NLP model that handles tasks like multi-turn text and code chat, and code generation.

1.0 Pro is capable of handling zero-, one-, and few-shot learning tasks.

**Model details**
- **Model code**: models/gemini-1.0-pro
- **Input**: Text
- **Output**: Text
- **Supported generation methods**:
  - Python: generate_content
  - REST: generateContent
- **Rate limits**:
  - Free: 15 RPM, 32,000 TPM, 1,500 RPD, 46,080,000 TPD
  - Pay-as-you-go: 360 RPM, 120,000 TPM, 30,000 RPD, 172,800,000 TPD
- **System instructions**: Unsupported
- **JSON mode**: Unsupported
- **Model tuning**: Supported: gemini-1.0-pro-001
- **Latest version**: gemini-1.0-pro-latest
- **Latest stable version**: gemini-1.0-pro
- **Stable versions**: gemini-1.0-pro-001
- **Latest update**: February 2024
"""
}

for model, description in models_details.items():
    st.subheader(model)
    st.markdown(description)

# MMLU Scores Chart
st.header("MMLU Scores of Different Models")

models = ["Gemma 7B", "Gemma 2B", "Mistral 7B", "LLama 2 13B", "Llama 2 7B"]
scores = [64.3, 42.3, 62.5, 54.8, 45.3]

plt.figure(figsize=(10, 6))
plt.bar(models, scores, color='skyblue')
plt.xlabel('Models')
plt.ylabel('MMLU Scores')
plt.title('MMLU Scores of Different Models')
plt.ylim(0, 70)

st.pyplot(plt)
