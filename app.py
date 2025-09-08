import math
import re
from collections import Counter, defaultdict
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Tiny built-in English stopword list (editable)
STOPWORDS = {
    "a","about","above","after","again","against","all","am","an","and","any",
    "are","as","at","be","because","been","before","being","below","between",
    "both","but","by","could","did","do","does","doing","down","during","each",
    "few","for","from","further","had","has","have","having","he","her","here",
    "hers","herself","him","himself","his","how","i","if","in","into","is","it",
    "its","itself","just","me","more","most","my","myself","no","nor","not","now",
    "of","off","on","once","only","or","other","our","ours","ourselves","out",
    "over","own","same","she","should","so","some","such","than","that","the",
    "their","theirs","them","themselves","then","there","these","they","this",
    "those","through","to","too","under","until","up","very","was","we","were",
    "what","when","where","which","while","who","whom","why","with","you","your",
    "yours","yourself","yourselves"
}

WORD_RE = re.compile(r"[a-zA-Z']{2,}")

def tokenize(text: str):
    tokens = [w.lower().strip("'") for w in WORD_RE.findall(text)]
    return [t for t in tokens if t and t not in STOPWORDS]

def tfidf(texts):
    """
    Compute TF-IDF dictionaries per document.
    Returns: list of dict(term -> tfidf), plus idf dict and vocabulary set.
    """
    docs_tokens = [tokenize(t or "") for t in texts]
    N = len(docs_tokens)
    # term frequencies
    tfs = []
    for toks in docs_tokens:
        counts = Counter(toks)
        total = sum(counts.values()) or 1
        tf = {term: counts[term] / total for term in counts}
        tfs.append(tf)
    # document frequencies
    df = defaultdict(int)
    for tf in tfs:
        for term in tf:
            df[term] += 1
    # smoothed IDF
    idf = {term: math.log((1 + N) / (1 + dfc)) + 1.0 for term, dfc in df.items()}
    # TF-IDF
    tfidfs = []
    vocab = set()
    for tf in tfs:
        vec = {term: tfv * idf[term] for term, tfv in tf.items()}
        tfidfs.append(vec)
        vocab.update(vec.keys())
    return tfidfs, idf, vocab

def cosine(a: dict, b: dict):
    if not a or not b:
        return 0.0
    # dot product
    dot = 0.0
    # iterate through smaller dict for speed
    if len(a) > len(b):
        a, b = b, a
    for t, av in a.items():
        bv = b.get(t, 0.0)
        if bv:
            dot += av * bv
    # norms
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json(force=True)
    texts = data.get("texts", [])[:3]  # up to 3 docs
    top_n = int(data.get("top_n", 15))
    gap_base = int(data.get("gap_base", 0))  # which doc is "base" for gap analysis
    gap_top = int(data.get("gap_top", 10))
    gap_min_delta = float(data.get("gap_min_delta", 0.05))

    # compute tf-idf
    tfidfs, idf, vocab = tfidf(texts)

    # top keywords per doc
    top_keywords = []
    for vec in tfidfs:
        items = sorted(vec.items(), key=lambda x: x[1], reverse=True)[:top_n]
        top_keywords.append([{"term": t, "score": round(s, 4)} for t, s in items])

    # cosine similarity matrix
    sims = []
    for i in range(len(tfidfs)):
        row = []
        for j in range(len(tfidfs)):
            row.append(round(cosine(tfidfs[i], tfidfs[j]), 4))
        sims.append(row)

    # simple content gaps: terms strong in base but weak in others
    gaps = []
    if 0 <= gap_base < len(tfidfs):
        base_vec = tfidfs[gap_base]
        for other_idx, other_vec in enumerate(tfidfs):
            if other_idx == gap_base:
                continue
            deltas = []
            # consider union of terms, but rank by base strength - other strength
            terms = set(base_vec.keys()) | set(other_vec.keys())
            for t in terms:
                delta = base_vec.get(t, 0.0) - other_vec.get(t, 0.0)
                if delta > gap_min_delta:
                    deltas.append((t, delta, base_vec.get(t, 0.0), other_vec.get(t, 0.0)))
            deltas.sort(key=lambda x: x[1], reverse=True)
            gaps.append({
                "vs": other_idx,
                "items": [
                    {"term": t, "delta": round(d, 4), "base": round(bv, 4), "other": round(ov, 4)}
                    for t, d, bv, ov in deltas[:gap_top]
                ]
            })

    return jsonify({
        "top_keywords": top_keywords,
        "similarity": sims,
        "gaps": gaps,
        "vocab_size": len(vocab)
    })

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(debug=True)
