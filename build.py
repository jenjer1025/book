#!/usr/bin/env python3
"""把 chapters/ 裡的 .md 檔轉成靜態網頁，輸出到 docs/。"""
import json, html, re, shutil, pathlib
R = pathlib.Path(__file__).parent
cfg = json.loads((R/"config.json").read_text(encoding="utf-8"))
out = R/"docs"; shutil.rmtree(out, ignore_errors=True); out.mkdir()
shutil.copy(R/"style.css", out/"style.css")
JS = """<script>
const d=document.documentElement,s=localStorage;
if(s.theme)d.dataset.theme=s.theme;if(s.fs)d.style.setProperty('--fs',s.fs+'px');
function tg(){d.dataset.theme=d.dataset.theme=='dark'?'':'dark';s.theme=d.dataset.theme}
function fz(k){let v=parseInt(s.fs||19)+k;v=Math.max(14,Math.min(28,v));s.fs=v;d.style.setProperty('--fs',v+'px')}
</script>"""
def page(title, body, home="index.html"):
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">{JS}</head><body>
<div class="bar"><a href="{home}">{html.escape(cfg['title'])}</a><div>
<button onclick="fz(-1)" title="縮小字體">A－</button><button onclick="fz(1)" title="放大字體">A＋</button>
<button onclick="tg()" title="切換深色／淺色">☾ 深淺</button></div></div>
<main>{body}</main><footer>© {html.escape(cfg['author'])}</footer></body></html>"""
chs = []; n = 0
for f in sorted((R/"chapters").glob("*.md")):
    pre = f.stem.startswith("00")
    if not pre: n += 1
    lines = f.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("#") else f.stem
    paras = []
    for ln in (lines[1:] if lines and lines[0].startswith("#") else lines):
        t = ln.strip()
        if not t: continue
        if re.fullmatch(r"[＊*\s　]+", t) or t in ("***", "---"):
            paras.append('<p class="break">＊ ＊ ＊</p>')
        else:
            cls = ' class="q"' if t[0] in "「『" else ""
            paras.append(f"<p{cls}>{html.escape(t)}</p>")
    chs.append(("preface.html" if pre else f"chapter-{n:02d}.html", title, "\n".join(paras), "序" if pre else f"第 {n} 章"))
for i, (fn, title, body, _) in enumerate(chs):
    prev = f'<a href="{chs[i-1][0]}">← {html.escape(chs[i-1][1])}</a>' if i else ""
    nxt = f'<a href="{chs[i+1][0]}">{html.escape(chs[i+1][1])} →</a>' if i+1 < len(chs) else ""
    nav = f'<nav class="pn"><span>{prev}</span><span class="c"><a href="index.html">目錄</a></span><span class="r">{nxt}</span></nav>'
    (out/fn).write_text(page(f"{title}｜{cfg['title']}", f"<h1>{html.escape(title)}</h1>\n{body}\n{nav}"), encoding="utf-8")
toc = "".join(f'<li><span class="n">{lab}</span><a href="{fn}">{html.escape(t)}</a></li>' for fn, t, _, lab in chs)
ip = R/"intro.md"
intro = "".join(f"<p>{html.escape(l.strip())}</p>" for l in ip.read_text(encoding="utf-8").splitlines() if l.strip()) if ip.exists() else ""
intro = f"<section class='intro'><h2>《{html.escape(cfg['title'])}》簡介</h2>{intro}</section>" if intro else ""
(out/"index.html").write_text(page(cfg["title"], f"<h1>{html.escape(cfg['title'])}</h1><p class='sub'>{html.escape(cfg['author'])}</p>{intro}<h2 style='font-size:1.1em;margin-top:2.5rem'>目錄</h2><ul class='toc'>{toc}</ul>"), encoding="utf-8")
print(f"完成：{len(chs)} 章 → docs/")
