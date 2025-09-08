# Keyword Compass — TF-IDF & Similarity Explorer

Paste up to 3 texts and instantly see:
- **Top keywords** per text (TF–IDF)
- **Cosine similarity** between texts
- **Content gaps** (terms strong in base doc but weak in others)

Tiny, fast stack: **Flask** backend + vanilla **HTML/CSS/JS** frontend. Package management via **uv**.

---

## 1) Quick start (local, with uv)

### Install uv (one-time)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# Make sure uv is on PATH (add line below to your shell rc for persistence)
export PATH="$HOME/.local/bin:$PATH"
```

### Windows (PowerShell)
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Add to PATH: $env:PATH += ";$env:USERPROFILE\.local\bin"
```

### Clone and run
```bash
git clone <your-repo>
cd keyword-compass
uv sync
uv run python app.py
```

Visit `http://localhost:5000`

---

## 2) What it does

**TF-IDF Analysis**: Computes term frequency × inverse document frequency to find the most distinctive keywords in each text.

**Cosine Similarity**: Measures how similar your texts are (0 = completely different, 1 = identical).

**Content Gaps**: Identifies terms that are strong in your "base" text but weak in others — perfect for finding missing topics or keywords.

---

## 3) How it works

1. **Tokenization**: Splits text into words, removes punctuation
2. **Stopword removal**: Filters out common words like "the", "and", "is"
3. **TF calculation**: Counts how often each term appears in each document
4. **IDF calculation**: Measures how rare/common each term is across all documents
5. **TF-IDF**: Combines TF and IDF to score term importance
6. **Cosine similarity**: Compares document vectors using dot product
7. **Gap analysis**: Finds terms with high TF-IDF in base doc but low in others

---

## 4) Use cases

- **SEO**: Compare your content to competitors, find missing keywords
- **Content strategy**: Identify gaps between blog posts or product pages
- **Academic writing**: Analyze research papers for topic coverage
- **Marketing**: Ensure consistent messaging across materials

---

## 5) Deployment

### Local development
```bash
uv run python app.py
```

### Production (with gunicorn)
```bash
uv run gunicorn -b 0.0.0.0:8000 wsgi:app
```

### Docker (optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install uv && uv sync
EXPOSE 8000
CMD ["uv", "run", "gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
```

---

## 6) Customization

- **Stopwords**: Edit the `STOPWORDS` set in `app.py`
- **Tokenization**: Modify the `WORD_RE` regex pattern
- **UI**: Customize colors and layout in `static/style.css`
- **Analysis**: Adjust TF-IDF smoothing or similarity metrics

---

## 7) Technical details

- **No external ML libraries**: Pure Python with math, collections, and regex
- **Lightweight**: ~200 lines of backend code
- **Fast**: Processes thousands of words in milliseconds
- **Educational**: Clear implementation of core IR/NLP concepts

Perfect for learning information retrieval fundamentals!
