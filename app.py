import os
from flask import Flask, render_template, request, jsonify, url_for


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB


FALLBACK_IMAGES = {
	"cat": "https://placekitten.com/600/400",
	"dog": "https://placedog.net/600/400",
	"elephant": "https://source.unsplash.com/600x400/?elephant",
}
ALLOWED_ANIMALS = set(FALLBACK_IMAGES.keys())


def get_local_image_url(animal: str) -> str | None:
	images_dir = os.path.join(app.static_folder, "images")
	for ext in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
		filename = f"{animal}{ext}"
		path = os.path.join(images_dir, filename)
		if os.path.isfile(path):
			return url_for("static", filename=f"images/{filename}")
	return None


@app.route("/")
def index():
	return render_template("index.html")


@app.post("/api/animal")
def api_animal():
	data = request.get_json(silent=True) or {}
	animal = (data.get("animal") or "").lower().strip()

	if animal not in ALLOWED_ANIMALS:
		return jsonify({"error": "Invalid animal. Choose cat, dog, or elephant."}), 400

	local_url = get_local_image_url(animal)
	url = local_url or FALLBACK_IMAGES[animal]
	return jsonify({"url": url})


@app.post("/api/upload")
def api_upload():
	file = request.files.get("file")
	if not file:
		return jsonify({"error": "No file uploaded under form field 'file'."}), 400

	# Compute size safely without saving
	cursor = file.stream.tell()
	file.stream.seek(0, os.SEEK_END)
	size = file.stream.tell()
	file.stream.seek(cursor)

	return jsonify(
		{
			"name": file.filename,
			"size_bytes": size,
			"type": file.mimetype or "application/octet-stream",
		}
	)


@app.errorhandler(413)
def too_large(_e):
	return jsonify({"error": "File too large"}), 413


if __name__ == "__main__":
	app.run(debug=True)


