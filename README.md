Animal Picker & File Upload (Flask + HTML/CSS/JS)

What this app does

- Select exactly one of three checkboxes (cat, dog, elephant) and the page shows the corresponding image.
- Upload any file and the backend responds with its name, size (bytes and human-readable), and MIME type.
- If local images exist at `static/images/cat.jpg`, `dog.jpg`, `elephant.jpg`, those are used; otherwise online placeholders are used.

Project structure

```
app.py                    # Flask app with two endpoints
templates/                # HTML template
  index.html
static/                   # Front-end assets
  app.js
  styles.css
  images/
    cat.jpg
    dog.jpg
    elephant.jpg
```

Quickstart (uv on Windows PowerShell)

- Option A: Run without modifying pyproject (recommended for quick try)

```
uv run --with Flask app.py
```

- Option B: Add Flask to the project, then run

```
uv add Flask
uv run app.py
```

Open `http://127.0.0.1:5000` in your browser.

API endpoints

- POST `/api/animal`
  - Body (JSON): `{ "animal": "cat" | "dog" | "elephant" }`
  - Response (JSON): `{ "url": "<image_url>" }`

- POST `/api/upload`
  - Form-data: `file` (any file)
  - Response (JSON): `{ "name": "...", "size_bytes": <int>, "type": "..." }`

cURL examples

```
curl -s -X POST http://127.0.0.1:5000/api/animal \
  -H "Content-Type: application/json" \
  -d '{"animal":"cat"}' | jq

curl -s -X POST http://127.0.0.1:5000/api/upload \
  -F file=@path/to/anyfile | jq
```

Notes

- Local images are auto-detected; place files as `static/images/cat.jpg`, `dog.jpg`, `elephant.jpg`.
- Max upload size is 16 MB (see `MAX_CONTENT_LENGTH` in `app.py`).
- To change the port, edit the `app.run(...)` call in `app.py` (e.g., `port=5001`).