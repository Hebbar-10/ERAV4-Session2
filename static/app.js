function $(sel) { return document.querySelector(sel); }
function $all(sel) { return document.querySelectorAll(sel); }

function humanBytes(n) {
  if (!Number.isFinite(n)) return String(n);
  const units = ["B","KB","MB","GB","TB"];
  let i = 0; let v = n;
  while (v >= 1024 && i < units.length - 1) { v /= 1024; i++; }
  return `${v.toFixed(v < 10 && i ? 1 : 0)} ${units[i]}`;
}

document.addEventListener("DOMContentLoaded", () => {
  const img = $("#animal-image");
  const placeholder = $("#animal-placeholder");
  const boxes = $all('input[name="animal"]');

  boxes.forEach(cb => {
    cb.addEventListener("change", async (e) => {
      if (e.target.checked) {
        boxes.forEach(other => { if (other !== e.target) other.checked = false; });
        try {
          const res = await fetch("/api/animal", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ animal: e.target.value })
          });
          const data = await res.json();
          if (!res.ok) throw new Error(data.error || "Failed to load image");
          img.src = data.url;
          img.style.display = "block";
          placeholder.style.display = "none";
        } catch (err) {
          img.style.display = "none";
          placeholder.textContent = err.message;
          placeholder.style.display = "block";
        }
      } else {
        const anyChecked = Array.from(boxes).some(x => x.checked);
        if (!anyChecked) {
          img.removeAttribute("src");
          img.style.display = "none";
          placeholder.textContent = "No animal selected";
          placeholder.style.display = "block";
        }
      }
    });
  });

  const input = $("#fileInput");
  const result = $("#fileResult");

  input.addEventListener("change", async () => {
    const file = input.files && input.files[0];
    if (!file) {
      result.textContent = "";
      return;
    }
    const form = new FormData();
    form.append("file", file);
    result.textContent = "Uploading...";

    try {
      const res = await fetch("/api/upload", { method: "POST", body: form });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Upload failed");
      result.textContent =
        `name: ${data.name}\nsize: ${data.size_bytes} bytes (${humanBytes(data.size_bytes)})\ntype: ${data.type}`;
    } catch (err) {
      result.textContent = `Error: ${err.message}`;
    }
  });
});


