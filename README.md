# Gen AI Training

This repository documents my learning journey in **Generative AI**.
It contains notes, experiments, and hands-on projects as I explore LLMs, AI agents, deep learning, and supporting tools.

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
│   ├── tf-idf/            # TF-IDF vectorization
│   └── datasets/          # Shared datasets (smsspamcollection.csv)
│
├── genai/                 # LLM API work (OpenAI SDK against a Groq endpoint)
│   ├── openai-api/        # main.py — chat loop with conversation history
│   ├── prompting/         # prompt_engineering_demo.ipynb
│   ├── rag-workflow/      # main.py — pull staff rows from SQLite, build context
│   ├── cag-workflow/      # main.py — cache/context-augmented generation over staff.db
│   ├── staff.db           # SQLite sample data for the RAG/CAG scripts
│   └── requirements.txt   # openai, python-dotenv, pydantic, httpx
│
├── deep-learning/         # Neural networks with TensorFlow / Keras
│   └── ann-classification/
│       ├── experiments.ipynb        # ANN churn prediction: preprocessing pipeline
│       ├── Churn_Modelling.csv      # Bank customer churn dataset
│       ├── requirements.txt         # tensorflow, tensorboard, sklearn, streamlit
│       ├── gender_label_encoder.pkl # Fitted LabelEncoder (Gender)
│       ├── geo_one_hot_encoder.pkl  # Fitted OneHotEncoder (Geography)
│       └── scaler.pkl               # Fitted StandardScaler
│
└── requirements.txt       # Combined deps for the workspace
```

## Setup

```bash
# Create + activate a virtual environment (Windows / bash)
python -m venv .venv
source .venv/Scripts/activate

# Install dependencies
pip install -r requirements.txt
```

`genai/` and `deep-learning/ann-classification/` each ship their own `requirements.txt`. Use those if you'd rather keep a lighter, per-topic environment instead of installing everything at the root.

### NLTK corpora

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

### API keys

The scripts under `genai/` read credentials from `genai/.env` (gitignored) via `python-dotenv`:

```
GROQ_API_KEY=...
GROQ_BASE_URL=https://api.groq.com/openai/v1
GROQ_MODEL=...
```

They use the official `openai` SDK pointed at that base URL, so the same code works against any OpenAI-compatible endpoint.

## Running things

- **Notebooks** — open in VS Code or Jupyter and select the `.venv` kernel.
- **Streamlit demos** — `streamlit run <file>.py`. Working directory matters: `NLP/bow/bow_streamlit.py` reads `../datasets/smsspamcollection.csv` relative to its own folder, so run it from `NLP/bow/`.
- **`genai/` scripts** — `python main.py` from inside the script's own folder; they resolve `staff.db` and `.env` by relative path.
- **`deep-learning/` notebooks** — run from `deep-learning/ann-classification/`; the notebook reads `Churn_Modelling.csv` and writes the `.pkl` encoders into the same folder. The pickles are committed deliberately — a Streamlit deployment builds from the repo, so the fitted encoders and scaler have to be present at runtime rather than refitted on the server.

## NLP pipeline pattern

The NLP notebooks and `bow_streamlit.py` share the same preprocessing shape:

1. Lowercase the text
2. `re.sub("[^a-zA-Z]", " ", ...)` to strip non-alphabetic characters
3. `word_tokenize`
4. Drop NLTK English stopwords
5. Stem (`PorterStemmer`) or lemmatize (`WordNetLemmatizer`, often `pos="v"`)
6. Re-join words and feed into `CountVectorizer`

## ANN preprocessing pattern

`deep-learning/ann-classification/experiments.ipynb` follows the standard tabular prep flow before the network is built:

1. Drop identifier columns (`RowNumber`, `CustomerId`, `Surname`)
2. `LabelEncoder` on `Gender`
3. `OneHotEncoder` on `Geography`, expanded into columns and concatenated back
4. `train_test_split` (80/20, `random_state=42`) into `X` / `y` on `Exited`
5. `StandardScaler` — `fit_transform` on train, `transform` on test
6. Pickle the fitted encoders and scaler so inference reuses the exact same transforms

## Goals

- Strengthen core Python knowledge for AI development
- Build practical projects with Generative AI
- Experiment with LLMs, agents, and AI tools
- Document learning and progress

## Topics Covered

- Python fundamentals (data structures, OOP, regex)
- Pandas for data analysis
- Streamlit for interactive demos
- NLP: tokenization, stopwords, stemming, lemmatization, POS tagging, NER, Bag of Words, n-grams, TF-IDF
- LLM APIs: OpenAI SDK, OpenAI-compatible endpoints, multi-turn conversation history
- Prompt engineering
- RAG and CAG workflows over a SQLite knowledge source
- Deep learning: ANN classification with TensorFlow / Keras, feature encoding and scaling
