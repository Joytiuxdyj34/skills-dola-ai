#!/usr/bin/env python3
"""LostHex site builder — render the repo into a browsable static site (GitHub-style).

    python scripts/build_site.py            # -> site/
    npx wrangler pages deploy site --project-name=losthex-skills

No machine paths: everything is derived from the repo root this file lives in.
"""
import html, json, os, re, shutil, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site")
# .wrangler = wrangler account cache, cfgit = local Pages-worker scaffolding: both are
# untracked deploy artifacts that must never leak into the published site/zip.
SKIP_DIRS = {".git", "__pycache__", "site", "node_modules", ".wrangler", "cfgit"}
SKIP_FILES = {".marked.tmp"}
TEXT_EXT = {".md", ".txt", ".py", ".sh", ".ps1", ".json", ".yml", ".yaml", ".toml", ".cfg",
            ".ini", ".js", ".ts", ".html", ".css", ".rb", ".go", ".rs", ".c", ".h", ".cpp",
            ".java", ".php", ".lua", ".sql", ".diff", ".patch", ".gitignore", ""}
MD_EXT = {".md", ".markdown"}
ICONS = {".md": "📄", ".markdown": "📄", ".py": "🐍", ".sh": "🖥", ".ps1": "🖥", ".json": "🔧",
         ".yml": "🔧", ".yaml": "🔧", ".toml": "🔧", ".zip": "📦", ".txt": "📄"}

CSS = """
:root{--bg:#0d1117;--fg:#e6edf3;--muted:#8b949e;--card:#161b22;--hover:#1f242c;--border:#30363d;--accent:#4493f8;--code:#1f242c}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header{display:flex;gap:12px;align-items:center;padding:10px 20px;background:var(--card);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:5;flex-wrap:wrap}
header .repo{font-weight:600;color:var(--fg);display:flex;align-items:center;gap:8px}
header .pill{border:1px solid var(--border);border-radius:999px;padding:1px 10px;color:var(--muted);font-size:12px}
.tools{margin-left:auto;display:flex;gap:8px}
.btn{border:1px solid var(--border);border-radius:6px;padding:4px 12px;color:var(--fg);font-size:12.5px;background:var(--card);font-weight:500}
.btn:hover{background:var(--hover);text-decoration:none}
.wrap{display:flex;align-items:flex-start;gap:24px;padding:20px;max-width:1440px;margin:0 auto}
aside{width:320px;flex:0 0 320px;position:sticky;top:64px;max-height:calc(100vh - 84px);overflow:auto;font-size:13px;padding-right:4px}
aside::-webkit-scrollbar{width:8px}aside::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
.tsearch{position:relative;margin-bottom:10px}
#q{width:100%;background:var(--bg);border:1px solid var(--border);color:var(--fg);border-radius:6px;padding:6px 10px;font-size:13px}
#q:focus{outline:none;border-color:var(--accent)}
#results{position:absolute;left:0;right:0;top:36px;background:var(--card);border:1px solid var(--border);border-radius:8px;max-height:60vh;overflow:auto;z-index:9;display:none;box-shadow:0 8px 24px rgba(0,0,0,.5)}
#results a{display:block;padding:6px 10px;color:var(--fg);font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
#results a:hover{background:var(--hover);text-decoration:none}
.tree details{margin:0}
.tree summary{display:flex;align-items:center;gap:6px;padding:3px 6px;border-radius:6px;cursor:pointer;list-style:none;font-weight:500}
.tree summary::-webkit-details-marker{display:none}
.tree summary:hover{background:var(--hover)}
.chev{width:9px;flex:none;color:var(--muted);font-size:9px;transition:transform .12s ease}
.chev::before{content:"\25B6"}
details[open]>summary>.chev{transform:rotate(90deg)}
.kids{margin-left:9px;padding-left:7px;border-left:1px solid var(--border)}
.ic{width:16px;flex:none;text-align:center;font-size:12px;opacity:.95}
.nm{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tree a.file{display:flex;align-items:center;gap:6px;padding:3px 6px;border-radius:6px;color:var(--fg)}
.tree a.file:hover{background:var(--hover);text-decoration:none}
.tree a.file.active{background:rgba(68,147,248,.16);color:#fff;font-weight:600}
main{flex:1;min-width:0}
.card{background:var(--card);border:1px solid var(--border);border-radius:8px;overflow:hidden}
.fhead{display:flex;align-items:center;gap:12px;padding:10px 16px;border-bottom:1px solid var(--border);background:var(--bg);font-size:13px}
.crumbs{color:var(--muted);display:flex;gap:6px;align-items:center;flex-wrap:wrap;min-width:0}
.crumbs a{color:var(--accent)}
.crumbs .sep{color:var(--border)}
.crumbs .here{color:var(--fg);font-weight:600}
.fhead .btn{margin-left:auto;flex:none}
.body{padding:20px 24px}
h1,h2,h3{line-height:1.3}h1{border-bottom:1px solid var(--border);padding-bottom:8px}
pre{background:var(--code);border:1px solid var(--border);border-radius:6px;padding:12px;overflow:auto}
code{background:var(--code);padding:2px 5px;border-radius:4px;font:12.5px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
pre code{background:none;padding:0}
table{border-collapse:collapse;display:block;overflow:auto;max-width:100%}
th,td{border:1px solid var(--border);padding:6px 12px}
th{background:var(--code)}
img{max-width:100%}
blockquote{border-left:3px solid var(--border);margin:0;padding:0 14px;color:var(--muted)}
.meta{color:var(--muted);font-size:12px;margin-top:14px;border-top:1px solid var(--border);padding-top:10px}
footer{color:var(--muted);font-size:12px;padding:24px;text-align:center}
@media(max-width:820px){.wrap{flex-direction:column}aside{width:100%;flex:none;position:static;max-height:320px}}
"""

SHELL = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body>
<header>
  <a class="repo" href="/">🐙 LostHex-Skills</a>
  <span class="pill">{count} files</span>
  <span class="pill">MITRE 898 · WSTG 125 · 106 skills</span>
  <span class="tools">
    <a class="btn" href="/">README</a>
    <a class="btn" href="/LostHex-Skills.zip">↓ zip</a>
  </span>
</header>
<div class="wrap">
  <aside>
    <div class="tsearch"><input id="q" placeholder="Go to file…" autocomplete="off"><div id="results"></div></div>
    <div class="tree" id="tree"></div>
  </aside>
  <main>{body}</main>
</div>
<footer>LostHex — static mirror generated by <code>scripts/build_site.py</code></footer>
<script>
// tree + search load from shared assets so every page stays small
fetch('/tree.html').then(r => r.text()).then(h => {{
  const el = document.getElementById('tree');
  el.innerHTML = h;
  const here = decodeURIComponent(location.pathname).replace(/^\\//, '').replace(/\\.html$/, '');
  if (!here) return;
  el.querySelectorAll('a.file').forEach(a => {{ if (a.dataset.path === here) a.classList.add('active'); }});
  el.querySelectorAll('details').forEach(d => {{ if (here.startsWith(d.dataset.path)) d.open = true; }});
  const act = el.querySelector('a.file.active');
  if (act) {{ act.scrollIntoView({{ block: 'center' }}); }}
}});
let FILES = null;
const q = document.getElementById('q'), res = document.getElementById('results');
q.addEventListener('input', async () => {{
  const v = q.value.trim().toLowerCase();
  if (v.length < 2) {{ res.style.display = 'none'; res.innerHTML = ''; return; }}
  if (!FILES) FILES = await (await fetch('/files.json')).json();
  const hits = FILES.filter(f => f.p.toLowerCase().includes(v)).slice(0, 40);
  res.innerHTML = hits.map(f => `<a href="/${{f.h}}">${{f.p}}</a>`).join('') || '<a>no match</a>';
  res.style.display = 'block';
}});
q.addEventListener('keydown', e => {{ if (e.key === 'Escape') {{ q.value = ''; res.style.display = 'none'; }} }});
document.addEventListener('click', e => {{ if (!res.contains(e.target) && e.target !== q) res.style.display = 'none'; }});
</script></body></html>
"""


def is_text(path):
    return os.path.splitext(path)[1].lower() in TEXT_EXT


def icon_for(name):
    return ICONS.get(os.path.splitext(name)[1].lower(), "📄")


def _fix_href(url):
    """Repo-relative links (e.g. ./TOOLS.md, Java.md) point at source names; the site
    writes pages as <path>.html, so append .html. Leave absolute/external/anchor links."""
    if not url or url.startswith(("http://", "https://", "//", "#", "/", "mailto:", "data:")):
        return url
    path, tail = re.match(r"^([^#?]*)(.*)$", url).groups()
    if path.lower().endswith((".md", ".markdown")):
        path += ".html"
    return path + tail


def rewrite_links(html_text):
    return re.sub(r'(href=")([^"]*)(")', lambda m: m.group(1) + _fix_href(m.group(2)) + m.group(3), html_text)


def render_md(text):
    try:
        import markdown
        return rewrite_links(markdown.markdown(text, extensions=["fenced_code", "tables", "toc", "sane_lists"]))
    except Exception:
        return "<pre>" + html.escape(text) + "</pre>"


def build_tree(files):
    """GitHub-style nested tree: dirs first, collapsible <details>, dirs closed by
    default (the page script opens the ancestors of the file you are looking at)."""
    root = {}
    for rel in files:
        node = root
        for part in rel.split("/"):
            node = node.setdefault(part, {})

    def walk(node, prefix="", depth=0):
        dirs = sorted(k for k, v in node.items() if v)
        leaves = sorted(k for k, v in node.items() if not v)
        out = []
        for d in dirs:
            sub = prefix + d + "/"
            out.append(
                f'<details data-path="{html.escape(sub)}"><summary><span class="chev"></span>'
                f'<span class="ic">📁</span><span class="nm">{html.escape(d)}</span></summary>'
                f'<div class="kids">{walk(node[d], sub, depth + 1)}</div></details>')
        for leaf in leaves:
            rel = prefix + leaf
            out.append(f'<a class="file" data-path="{html.escape(rel)}" href="/{html.escape(rel)}.html" '
                       f'title="{html.escape(rel)}"><span class="ic">{icon_for(leaf)}</span>'
                       f'<span class="nm">{html.escape(leaf)}</span></a>')
        return "".join(out)

    return walk(root)


def crumbs_html(rel):
    parts = rel.split("/")
    out = ['<a href="/">LostHex-Skills</a>']
    for i, part in enumerate(parts):
        out.append('<span class="sep">/</span>')
        if i == len(parts) - 1:
            out.append(f'<span class="here">{html.escape(part)}</span>')
        else:
            out.append(f'<span>{html.escape(part)}</span>')
    return "".join(out)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    files, blobs = [], {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in SKIP_FILES:
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT).replace("\\", "/")
            files.append({"p": rel, "s": os.path.getsize(full), "h": rel + ".html"})
            with open(full, "rb") as fh:
                blobs[rel] = fh.read()
    files.sort(key=lambda f: f["p"])

    tree = build_tree([f["p"] for f in files])
    count = len(files)
    manifest = json.dumps([{"p": f["p"], "h": f["h"], "s": f["s"]} for f in files], ensure_ascii=False)

    def write(rel_path, data):
        dst = os.path.join(OUT, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        mode = "wb" if isinstance(data, bytes) else "w"
        with open(dst, mode, **({} if isinstance(data, bytes) else {"encoding": "utf-8", "newline": "\n"})) as fh:
            fh.write(data)

    for f in files:
        rel, raw = f["p"], blobs[f["p"]]
        ext = os.path.splitext(rel)[1].lower()
        head = (f'<div class="fhead"><div class="crumbs">{crumbs_html(rel)}</div>'
                f'<a class="btn" href="/raw/{html.escape(rel)}">Raw</a></div>')
        if not is_text(rel):
            inner = f'<div class="body"><p>Binary file — {f["s"]:,} bytes</p>' \
                    f'<p><a href="/raw/{html.escape(rel)}">download raw</a></p></div>'
        elif ext in MD_EXT:
            inner = f'<div class="body">{render_md(raw.decode("utf-8", "replace"))}' \
                    f'<div class="meta">{f["s"]:,} bytes · <a href="/raw/{html.escape(rel)}">view raw</a></div></div>'
        else:
            inner = f'<div class="body"><pre><code>{html.escape(raw.decode("utf-8", "replace"))}</code></pre>' \
                    f'<div class="meta">{f["s"]:,} bytes · <a href="/raw/{html.escape(rel)}">view raw</a></div></div>'
        write(os.path.join("raw", rel), raw)
        write(rel + ".html", SHELL.format(title=rel, css=CSS, count=count,
                                          body=f'<div class="card">{head}{inner}</div>'))

    readme = blobs.get("README.md", b"# LostHex-Skills\n").decode("utf-8", "replace")
    index_head = ('<div class="fhead"><div class="crumbs"><a href="/">LostHex-Skills</a>'
                  '<span class="sep">/</span><span class="here">README.md</span></div>'
                  '<a class="btn" href="/raw/README.md">Raw</a></div>')
    write("index.html", SHELL.format(title="LostHex-Skills", css=CSS, count=count,
                                     body=f'<div class="card">{index_head}'
                                          f'<div class="body">{render_md(readme)}</div></div>'))

    # full repo zip (no .git)
    zp = os.path.join(OUT, "LostHex-Skills.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for f in files:
            z.writestr("LostHex-Skills/" + f["p"], blobs[f["p"]])
    write("tree.html", tree)
    write("files.json", manifest)
    # Cloudflare Pages: security headers for everything, and a real 404 page so
    # unknown paths stop returning index.html with HTTP 200.
    write("_headers", "/*\n"
                      "  x-frame-options: DENY\n"
                      "  x-content-type-options: nosniff\n"
                      "  referrer-policy: strict-origin-when-cross-origin\n")
    write("404.html", SHELL.format(
        title="404 — not found", css=CSS, count=count,
        body='<div class="card"><div class="fhead"><div class="crumbs">'
             '<a href="/">LostHex-Skills</a><span class="sep">/</span>'
             '<span class="here">404</span></div><a class="btn" href="/">home</a></div>'
             '<div class="body"><h1>404 — ไม่พบไฟล์นี้</h1>'
             '<p>ลองค้นจากช่อง <b>Go to file…</b> ข้างซ้าย หรือเปิด '
             '<a href="/files.json">files.json</a></p></div></div>'))
    print(f"site: {count} files -> {OUT}")
    print(f"zip : {os.path.getsize(zp)/1e6:.1f} MB")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        assert _fix_href("./TOOLS.md") == "./TOOLS.md.html"
        assert _fix_href("Java.md#x") == "Java.md.html#x"
        assert _fix_href("sub/a.markdown") == "sub/a.markdown.html"
        assert _fix_href("https://x/y.md") == "https://x/y.md"
        assert _fix_href("/raw/a.md") == "/raw/a.md"
        assert _fix_href("#frag") == "#frag"
        t = build_tree(["a/b/c.md", "a/d.md", "top.md"])
        assert t.count("<details") == 2, t
        assert 'data-path="a/b/"' in t and 'data-path="a/b/c.md"' in t
        assert 'href="/top.md.html"' in t
        assert crumbs_html("a/b/c.md").count("here") == 1
        print("selftest ok")
        sys.exit(0)
    main()
