Animal picker & file upload (Flask)

Run with uv (Windows PowerShell)

1. Install Flask into the uv environment

```
uv add Flask
```

2. Start the app

```
uv run app.py
```

Open http://127.0.0.1:5000

Endpoints

- POST /api/animal
  - body: { "animal": "cat" | "dog" | "elephant" }
  - response: { "url": "..." }

- POST /api/upload
  - form-data: file (any file)
  - response: { "name", "size_bytes", "type" }

Optional local images

- static/images/cat.jpg
- static/images/dog.jpg
- static/images/elephant.jpg

If missing, the app uses online placeholders.