let LAST_ANALYSIS = null;

function getTexts() {
  return [0,1,2].map(i => document.getElementById(`t${i}`).value || "");
}

async function analyze() {
  const payload = {
    texts: getTexts(),
    top_n: parseInt(document.getElementById("top_n").value || "15", 10),
    gap_base: parseInt(document.getElementById("gap_base").value || "0", 10),
    gap_top: parseInt(document.getElementById("gap_top").value || "10", 10),
    gap_min_delta: parseFloat(document.getElementById("gap_min_delta").value || "0.05")
  };

  const res = await fetch("/api/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });
  const data = await res.json();
  renderResults(data);
}

function renderResults(data) {
  LAST_ANALYSIS = data;           // <-- keep it for SEO rewrite
  document.getElementById("results").classList.remove("hidden");
  renderTopKeywords(data.top_keywords);
  renderSimilarity(data.similarity);
  renderGaps(data.gaps);
}

function renderTopKeywords(topKeywords) {
  const container = document.getElementById("tops");
  container.innerHTML = "";
  topKeywords.forEach((list, idx) => {
    const tbl = document.createElement("table");
    const thead = document.createElement("thead");
    thead.innerHTML = `<tr><th colspan="2">Text ${idx} <span class="badge">${list.length} terms</span></th></tr><tr><th>Term</th><th>TF-IDF</th></tr>`;
    tbl.appendChild(thead);
    const tb = document.createElement("tbody");
    list.forEach(item => {
      const tr = document.createElement("tr");
      tr.innerHTML = `<td>${item.term}</td><td>${item.score}</td>`;
      tb.appendChild(tr);
    });
    tbl.appendChild(tb);
    container.appendChild(tbl);
  });
}

function renderSimilarity(matrix) {
  const tbl = document.getElementById("sim");
  const n = matrix.length;
  let html = "<tr><th></th>";
  for (let j=0; j<n; j++) html += `<th>T${j}</th>`;
  html += "</tr>";
  for (let i=0; i<n; i++) {
    html += `<tr><th>T${i}</th>`;
    for (let j=0; j<n; j++) {
      html += `<td>${matrix[i][j].toFixed ? matrix[i][j].toFixed(3) : matrix[i][j]}</td>`;
    }
    html += "</tr>";
  }
  tbl.innerHTML = html;
}

function renderGaps(gaps) {
  const container = document.getElementById("gaps");
  container.innerHTML = "";
  if (!gaps || gaps.length === 0) {
    container.textContent = "No gap suggestions — add more texts or adjust thresholds.";
    return;
  }
  const grid = document.createElement("div");
  grid.className = "gap-list";
  gaps.forEach(g => {
    const box = document.createElement("div");
    box.className = "gap-item";
    const title = document.createElement("div");
    title.innerHTML = `<strong>Stronger in base vs Text ${g.vs}</strong>`;
    box.appendChild(title);
    const ul = document.createElement("ul");
    g.items.forEach(it => {
      const li = document.createElement("li");
      li.textContent = `${it.term}  (Δ ${it.delta} | base ${it.base} vs ${it.other})`;
      ul.appendChild(li);
    });
    box.appendChild(ul);
    grid.appendChild(box);
  });
  container.appendChild(grid);
}

async function seoRewrite() {
  const baseIdx = parseInt(document.getElementById("seo_base").value || "0", 10);
  const wordLimit = parseInt(document.getElementById("seo_words").value || "120", 10);
  const tone = document.getElementById("seo_tone").value || "confident, clear, helpful";
  const audience = document.getElementById("seo_audience").value || "safety managers";

  // get source text from the input boxes
  const baseText = document.getElementById(`t${baseIdx}`)?.value || "";

  // use the top keywords we already computed for that text (fall back to empty list)
  let keywords = [];
  if (LAST_ANALYSIS && LAST_ANALYSIS.top_keywords && LAST_ANALYSIS.top_keywords[baseIdx]) {
    keywords = LAST_ANALYSIS.top_keywords[baseIdx].map(it => it.term).slice(0, 12);
  }

  const res = await fetch("/api/rewrite", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      text: baseText,
      keywords,
      word_limit: wordLimit,
      tone,
      audience,
      model: "gemini-2.5-flash"
    })
  });

  const data = await res.json();
  document.getElementById("seo_output").value = data.result || (data.error ? `Error: ${data.error}` : "(no output)");
}

document.getElementById("analyze").addEventListener("click", analyze);
document.getElementById("seo_rewrite").addEventListener("click", seoRewrite);
