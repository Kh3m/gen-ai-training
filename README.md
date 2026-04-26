# Gen AI Training

This repository documents my learning journey in **Generative AI**.
It contains notes, experiments, and hands-on projects as I explore LLMs, AI agents, and supporting tools.

## Repository Structure

```
gen-ai-training/
│
├── python-fundamentals/   # Core Python concepts (data structures, OOP, regex)
│   ├── data-structure/    # list.ipynb, dict.ipynb
│   ├── oop/               # oop.ipynb
│   └── regex/             # regex.ipynb
│
├── pandas/                # DataFrames, Series, and common operations
│   └── pandas.ipynb
│
├── streamlit/             # Standalone Streamlit demos (not a multi-page app)
│   ├── core.py            # DataFrames + line chart
│   └── widgets.py         # Inputs, sliders, file upload
│
├── NLP/                   # Natural Language Processing experiments
│   ├── tokenization.ipynb
│   ├── text_processing_stopwords.ipynb
│   ├── text_processing_stemming.ipynb
│   ├── text_processing_lemmatization.ipynb
│   ├── part_of_speech_tag.ipynb
│   ├── named_entity_recognition.ipynb
│   ├── bow/               # Bag of Words (notebook + Streamlit demo)
│   ├── n-grams/           # BoW with n-grams
│   └── datasets/          # Shared datasets (smsspamcollection.csv)
│
└── requirements.txt       # ipykernel, streamlit, pandas, numpy, nltk, scikit-learn
```

## Setup

```bash
# Create + activate a virtual environment (Windows / bash)
python -m venv myvenv
source myvenv/Scripts/activate

# Install dependencies
pip install -r requirements.txt
```

The NLP code uses NLTK corpora that aren't bundled with the pip package. Download them once before running any NLP notebook or `NLP/bow/bow_streamlit.py`:

```python
import nltk
for pkg in [
    "stopwords", "punkt", "punkt_tab", "wordnet",
    "averaged_perceptron_tagger", "averaged_perceptron_tagger_eng",
    "maxent_ne_chunker", "maxent_ne_chunker_tab", "words",
]:
    nltk.download(pkg)
```

## Running things

- **Notebooks** — open in VS Code or Jupyter and select the `myvenv` kernel.
- **Streamlit demos** — `streamlit run <file>.py`. Working directory matters: `NLP/bow/bow_streamlit.py` reads `../datasets/smsspamcollection.csv` relative to its own folder, so run it from `NLP/bow/`.

## NLP pipeline pattern

The NLP notebooks and `bow_streamlit.py` share the same preprocessing shape:

1. Lowercase the text
2. `re.sub("[^a-zA-Z]", " ", ...)` to strip non-alphabetic characters
3. `word_tokenize`
4. Drop NLTK English stopwords
5. Stem (`PorterStemmer`) or lemmatize (`WordNetLemmatizer`, often `pos="v"`)
6. Re-join words and feed into `CountVectorizer`

## Goals

- Strengthen core Python knowledge for AI development
- Build practical projects with Generative AI
- Experiment with LLMs, agents, and AI tools
- Document learning and progress

## Topics Covered

- Python fundamentals (data structures, OOP, regex)
- Pandas for data analysis
- Streamlit for interactive demos
- NLP: tokenization, stopwords, stemming, lemmatization, POS tagging, NER, Bag of Words, n-grams
