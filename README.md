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
│   ├── widgets.py         # Inputs, sliders, file upload
│   └── all_inputs_demo.py # Reference sheet: every input widget in one page
│
├── NLP/                   # Natural Language Processing experiments
│   ├── tokenization.ipynb
│   ├── text_processing_stopwords.ipynb
│   ├── text_processing_stemming.ipynb
│   ├── text_processing_lemmatization.ipynb
│   ├── part_of_speech_tag.ipynb
│   ├── named_entity_recognition.ipynb
│   ├── one_hot_encoding/  # One-hot encoding → Keras Tokenizer → Embedding layer
│   ├── bow/               # Bag of Words
│   │   ├── bow_simple.ipynb   # Minimal CountVectorizer example
│   │   ├── bag_of_words.ipynb # Full pipeline on the SMS spam dataset
│   │   └── bow_streamlit.py   # Same pipeline as a Streamlit demo
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
├── deep-learning/         # Neural networks, split by framework
│   ├── tensorflow/
│   │   └── ann/           # Artificial neural networks
│   │       └── ann-classification/
│   │           ├── experiments.ipynb           # Preprocessing, model definition, training
│   │           ├── prediction.ipynb            # Load saved artifacts, predict on one customer
│   │           ├── ann_classification_app.py   # Streamlit churn predictor
│   │           ├── Churn_Modelling.csv         # Bank customer churn dataset (10k rows)
│   │           ├── requirements.txt            # tensorflow, tensorboard, sklearn, streamlit
│   │           ├── gender_label_encoder.pkl    # Fitted LabelEncoder (Gender)
│   │           ├── geo_one_hot_encoder.pkl     # Fitted OneHotEncoder (Geography)
│   │           ├── scaler.pkl                  # Fitted StandardScaler
│   │           ├── sequential_model.h5         # Trained model, legacy HDF5 format
│   │           ├── sequential_model.keras      # Trained model, native Keras format
│   │           └── logs/fit/                   # TensorBoard run logs (gitignored)
│   └── pytorch/
│       ├── basics.ipynb   # Tensors, dtypes, ops, device check
│       └── ann/           # Same ANN problem in PyTorch (in progress)
│           └── experiments.ipynb
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

`genai/` and `deep-learning/tensorflow/ann/ann-classification/` each ship their own `requirements.txt`. Use those if you'd rather keep a lighter, per-topic environment instead of installing everything at the root.

The root `requirements.txt` carries both deep-learning stacks — `tensorflow` / `tensorboard` and `torch` / `torchinfo` — so a single root install covers every notebook here.

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
- **TensorFlow ANN notebooks** — run from `deep-learning/tensorflow/ann/ann-classification/`; every path inside them is relative to that folder. Run `experiments.ipynb` first (it writes the `.pkl` encoders and both model files), then `prediction.ipynb`, which loads them. The encoders and models are committed deliberately — a Streamlit deployment builds from the repo, so they have to be present at runtime rather than refitted on the server.
- **Churn predictor app** — `streamlit run deep-learning/tensorflow/ann/ann-classification/ann_classification_app.py`. Unlike the NLP demo it resolves its artifacts from `os.path.dirname(__file__)`, so the working directory doesn't matter.
- **PyTorch notebooks** — no data files or relative paths, so they run from anywhere. `basics.ipynb` prints `torch.cuda.is_available()` up front; everything in it works on CPU either way.

## Streamlit input widgets

`streamlit/all_inputs_demo.py` is a reference sheet rather than an exercise — one page that renders every input widget and echoes its return value, grouped by kind:

- **Text & number** — `text_input`, `text_area`, `number_input`
- **Selection** — `selectbox`, `multiselect`, `radio`, `checkbox`, `toggle`, `select_slider`
- **Sliders** — `slider` for a single value and for a `(low, high)` tuple
- **Date & time** — `date_input`, `time_input`
- **Buttons** — `button`, `download_button`, `link_button`
- **File & media** — `file_uploader`, `camera_input`, `audio_input`
- **Other** — `color_picker`, `data_editor` (with `num_rows="dynamic"`), `feedback`, `pills`
- **Forms** — `st.form` + `form_submit_button`, which batch their inputs into a single rerun instead of one per interaction

No dataset or state, so it runs from anywhere: `streamlit run streamlit/all_inputs_demo.py`.

## NLP pipeline pattern

The NLP notebooks and `bow_streamlit.py` share the same preprocessing shape:

1. Lowercase the text
2. `re.sub("[^a-zA-Z]", " ", ...)` to strip non-alphabetic characters
3. `word_tokenize`
4. Drop NLTK English stopwords
5. Stem (`PorterStemmer`) or lemmatize (`WordNetLemmatizer`, often `pos="v"`)
6. Re-join words and feed into `CountVectorizer`

## One-hot encoding words

`NLP/one_hot_encoding/one_hot_encoding.ipynb` walks the same three toy sentences (`"The food is good"`, `"The food is bad"`, `"Pizza is amazing"`) through four different ways of turning words into numbers, ending at word embeddings. The notebook first prints the expected matrices by hand, then reproduces them in code.

### 1. `sklearn.OneHotEncoder` — by hand

1. Tokenize each sentence with `.lower().split()`
2. Flatten to `sorted(set(all_words))` — a 7-word vocabulary
3. `reshape(-1, 1)` the vocabulary, since `OneHotEncoder` expects 2D input, and fit with `sparse_output=False` for readable dense output
4. Encode a sentence by transforming its token column, giving one row per word rather than one row per sentence

That last part is the takeaway: a sentence becomes a `(n_words × vocab_size)` matrix whose width grows with the vocabulary and which carries no frequency or ordering information — which is exactly what Bag of Words, n-grams, and TF-IDF go on to address.

### 2. `pd.get_dummies` — the pandas equivalent

Same result with labelled columns instead of a bare array: build a `pd.Series` of every token, call `get_dummies`, then slice the rows back into per-sentence blocks. It also shows the gotcha — encoding unseen words (`["love", "good", "food"]`) needs `.reindex(columns=dummies.columns, fill_value=0)`, because `get_dummies` derives its columns from whatever it's handed and has no memory of a fitted vocabulary.

### 3. `keras.preprocessing.text.one_hot` — and why to avoid it

Despite the name, this hashes each word into `[1, vocab_size)` rather than one-hot encoding it. The notebook demonstrates the failure directly: `"the food is bad"` → `[7, 2, 2, 1]`, where `food` and `is` collide on index 2. Setting `vocab_size=2` makes the collapse total. The problems are that there's no inspectable/reversible word index, uniqueness can't be guaranteed (only made less likely by inflating `vocab_size`), and the allocation is random hashing rather than anything vocabulary-aware. `hash(word) % 30` is run directly to show what's actually happening underneath.

### 4. `Tokenizer` + `Embedding` — the fix

`Tokenizer().fit_on_texts(...)` gives a real, inspectable `word_index` (`{'is': 1, 'the': 2, 'food': 3, ...}`) with no collisions, and `texts_to_sequences` turns sentences into integer sequences. From there:

1. `vocab_size = len(tokenizer.word_index) + 1` — the `+1` reserves index 0 for padding
2. `pad_sequences(..., padding='pre', maxlen=4)` to a uniform length
3. A one-layer `Sequential([Embedding(vocab_size, 10)])` compiled with `adam` / `mse`
4. `model.predict(padded_docs)` to read out each word's 10-dimensional vector

Nothing is trained here — the embeddings are still random initialisations. The point is the shape change: from a sparse `vocab_size`-wide one-hot row per word to a dense 10-dimensional vector per word, which is the representation everything downstream actually uses.

> This notebook imports TensorFlow/Keras for parts 3 and 4, so it needs the root `requirements.txt` rather than an NLP-only environment.

## Bag of Words

`NLP/bow/bow_simple.ipynb` is the minimal version, kept deliberately separate from the SMS spam pipeline in `bag_of_words.ipynb`. It uses `CountVectorizer(stop_words="english")` on two sentences that differ only in a negation and a repeat:

```
"The food is good"          → good: 1
"The food is not good good" → good: 2
```

Two things it makes visible. First, `sklearn.feature_extraction.text.ENGLISH_STOP_WORDS` (printed in full) is a different list from NLTK's — and it contains `not`, so the built-in `stop_words="english"` silently discards the negation and both sentences reduce to the same word. Second, the notebook rebuilds the cleaned text by hand alongside the count matrix in a single DataFrame, so the vocabulary, `vectorizer.vocabulary_` indices, and counts line up row by row.

`bag_of_words.ipynb` and `bow_streamlit.py` then run the full NLTK pipeline above on the real dataset.

## ANN churn classification (TensorFlow / Keras)

Binary classification on the bank customer churn dataset — predict `Exited` from 10 customer attributes. Three pieces: `experiments.ipynb` trains and saves, `prediction.ipynb` loads and infers, `ann_classification_app.py` wraps the same inference in a Streamlit UI.

### Preprocessing (`experiments.ipynb`)

1. Drop identifier columns (`RowNumber`, `CustomerId`, `Surname`)
2. `LabelEncoder` on `Gender`
3. `OneHotEncoder` on `Geography`, expanded into columns and concatenated back — 12 features total
4. `train_test_split` (80/20, `random_state=42`) into `X` / `y` on `Exited`
5. `StandardScaler` — `fit_transform` on train, `transform` on test
6. Pickle the fitted encoders and scaler so inference reuses the exact same transforms

### Model and training

```
Sequential([
    Dense(64, input_shape=(12,), activation="relu"),   # Hidden layer 1
    Dense(32, activation="relu"),                      # Hidden layer 2
    Dense(1,  activation="sigmoid"),                   # Output — churn probability
])
```

2,945 trainable parameters. Compiled with `adam` / `binary_crossentropy`, tracking `accuracy`. Trained for up to 100 epochs with two callbacks:

- **`EarlyStopping`** — `monitor="val_loss"`, `patience=10`, `restore_best_weights=True`
- **`TensorBoard`** — writes to a timestamped `logs/fit/<YYYYMMDD-HHMMSS>` directory

Saved in both formats to compare them: `.h5` (legacy HDF5, emits a deprecation warning) and `.keras` (current recommended).

### Inference (`prediction.ipynb`)

Loads the three pickles plus both model files, then mirrors the training transforms on a single-row DataFrame: label-encode `Gender` → one-hot `Geography` → concat → `scaler.transform` → `predict` → threshold at 0.5. Both model formats produce identical output, which is the point of saving both.

### Streamlit app (`ann_classification_app.py`)

The same inference path, driven by widgets instead of a hardcoded row. Worth noting:

- Model and encoders load once behind `@st.cache_resource` — they're unhashable objects, so this is the right cache decorator rather than `@st.cache_data`.
- The dropdown options come from the fitted encoders themselves (`geo_one_hot_encoder.categories_[0]`, `gender_label_encoder.classes_`), so the UI can't offer a category the model was never trained on.
- It shows each stage — raw → encoded → scaled → prediction — so the transform pipeline is visible rather than hidden.
- Only `sequential_model.keras` is loaded here; the `.h5` copy exists for the notebook comparison.

### Viewing the training run

```bash
tensorboard --logdir deep-learning/tensorflow/ann/ann-classification/logs/fit
```

Or inline in the notebook via `%load_ext tensorboard` and `%tensorboard --logdir logs/fit`. The `logs/` directory is gitignored — it's machine-specific and regenerated on every training run, so a fresh clone has nothing to view until you run `experiments.ipynb`.

## PyTorch

`deep-learning/pytorch/` is the second framework track — the same ANN problem approached from the other side, so the Keras and PyTorch versions can be compared directly.

### `basics.ipynb`

Tensor fundamentals, deliberately including the failure cases:

- **Device check** — `torch.__version__`, `torch.cuda.is_available()`, `torch.cuda.device_count()`
- **Tensors hold numbers, not text** — `torch.tensor([["Love", "Me"], ...])` is run *expecting* it to fail, then fixed by mapping words through a `vocab` dict to integer IDs first. Same idea as the one-hot notebook: text has to become numeric before a model sees it.
- **Shape and dtype** — `.shape`, `.dtype`, and constructors `torch.rand`, `torch.zeros`
- **Operations** — element-wise `+` and `*`, `@` for dot product, plus `.sum()`, `.mean()`, `.view()` (PyTorch's reshape), `.T`
- **Derivatives** — `f = 3a³ - b²` with `df/da = 9a²` and `df/db = -2b` worked out by hand, ahead of letting autograd compute them

### `ann/experiments.ipynb`

Placeholder — the PyTorch port of the churn classifier hasn't been written yet.

## Goals

- Strengthen core Python knowledge for AI development
- Build practical projects with Generative AI
- Experiment with LLMs, agents, and AI tools
- Document learning and progress

## Topics Covered

- Python fundamentals (data structures, OOP, regex)
- Pandas for data analysis
- Streamlit for interactive demos — charts, the full input widget set, forms, caching
- NLP: tokenization, stopwords, stemming, lemmatization, POS tagging, NER, one-hot encoding, Bag of Words, n-grams, TF-IDF
- Text-to-numeric representations: `OneHotEncoder` vs `pd.get_dummies` vs Keras hashing (`one_hot`) vs `Tokenizer`, padding, and dense word embeddings via a Keras `Embedding` layer
- LLM APIs: OpenAI SDK, OpenAI-compatible endpoints, multi-turn conversation history
- Prompt engineering
- RAG and CAG workflows over a SQLite knowledge source
- Deep learning with TensorFlow / Keras: ANN binary classification — feature encoding and scaling, callbacks (early stopping, TensorBoard), model serialization and reload for inference, serving the trained model through Streamlit
- Deep learning with PyTorch: tensor creation, shapes and dtypes, element-wise and matrix operations, reshaping, manual derivatives ahead of autograd
