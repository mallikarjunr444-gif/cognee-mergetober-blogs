import re
import os

with open('/Users/malikarjunr/.gemini/antigravity-ide/brain/30d6be94-e7ad-4486-a587-a53ee91ad154/hackathon_submission_pack.md') as f:
    text = f.read()

output_dir = '/Users/malikarjunr/.gemini/antigravity-ide/scratch/cognee-mergetober-blogs'
blogs_dir = os.path.join(output_dir, 'blogs')
os.makedirs(blogs_dir, exist_ok=True)

slug_map = {
    1: ('sendgrid', 'SendGrid', 'https://github.com/topoteretes/cognee-community/pull/438', 'https://github.com/topoteretes/cognee/issues/6087'),
    2: ('clickup', 'ClickUp', 'https://github.com/topoteretes/cognee-community/pull/439', 'https://github.com/topoteretes/cognee/issues/4701'),
    3: ('postmark', 'Postmark', 'https://github.com/topoteretes/cognee-community/pull/440', 'https://github.com/topoteretes/cognee/issues/6090'),
    4: ('dub', 'Dub.co', 'https://github.com/topoteretes/cognee-community/pull/441', 'https://github.com/topoteretes/cognee/issues/6091'),
    5: ('umami', 'Umami', 'https://github.com/topoteretes/cognee-community/pull/442', 'https://github.com/topoteretes/cognee/issues/6093'),
    6: ('linear', 'Linear', 'https://github.com/topoteretes/cognee-community/tree/feature/linear-connector', 'https://github.com/topoteretes/cognee/issues/6100'),
    7: ('twilio', 'Twilio', 'https://github.com/topoteretes/cognee-community/tree/feature/twilio-connector', 'https://github.com/topoteretes/cognee/issues/6100')
}

parts = re.split(r'## 📝 Blog Post \d+:\s*', text)
articles = []

css = """
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --border: #30363d;
  --text: #e6edf3;
  --text-muted: #8b949e;
  --primary: #58a6ff;
  --accent: #a371f7;
  --code-bg: #090d13;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  background-color: var(--bg);
  color: var(--text);
  line-height: 1.65;
  padding: 0 16px 60px 16px;
}
header {
  max-width: 860px;
  margin: 30px auto 40px auto;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}
header a {
  color: var(--primary);
  text-decoration: none;
  font-weight: 500;
}
header a:hover { text-decoration: underline; }
.badge {
  display: inline-block;
  background: rgba(163, 113, 247, 0.15);
  color: var(--accent);
  border: 1px solid rgba(163, 113, 247, 0.4);
  border-radius: 20px;
  padding: 4px 12px;
  font-size: 0.8rem;
  font-family: monospace;
  text-transform: uppercase;
}
.article-container {
  max-width: 860px;
  margin: 0 auto;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 40px;
}
.author-card {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0 32px 0;
  padding: 16px;
  background: var(--code-bg);
  border-radius: 8px;
  border: 1px solid var(--border);
}
.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 2px solid var(--accent);
}
.author-info h4 { margin: 0; font-size: 1.05rem; color: var(--text); }
.author-info p { margin: 0; font-size: 0.85rem; color: var(--text-muted); }
.content h1 { font-size: 2.2rem; margin-bottom: 16px; line-height: 1.25; color: #fff; }
.content h2 { font-size: 1.5rem; margin-top: 32px; margin-bottom: 12px; border-bottom: 1px solid var(--border); padding-bottom: 8px; color: #fff; }
.content h3 { font-size: 1.2rem; margin-top: 24px; margin-bottom: 8px; color: var(--primary); }
.content p { margin-bottom: 16px; color: var(--text); }
.content ul, .content ol { margin-left: 24px; margin-bottom: 16px; }
.content li { margin-bottom: 6px; }
.content pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  overflow-x: auto;
  margin: 20px 0;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
  font-size: 0.9rem;
  color: #79c0ff;
}
.content code {
  background: rgba(110, 118, 129, 0.4);
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.88em;
  font-family: monospace;
}
.content pre code { background: none; padding: 0; }
.content blockquote {
  border-left: 4px solid var(--primary);
  padding-left: 16px;
  color: var(--text-muted);
  margin: 20px 0;
}
.content table {
  width: 100%;
  border-collapse: collapse;
  margin: 24px 0;
}
.content th, .content td {
  border: 1px solid var(--border);
  padding: 10px 14px;
  text-align: left;
}
.content th { background: var(--code-bg); color: #fff; }
.content hr { border: 0; height: 1px; background: var(--border); margin: 30px 0; }
.links-box {
  margin-top: 36px;
  padding: 20px;
  background: var(--code-bg);
  border-radius: 8px;
  border-left: 4px solid var(--accent);
}
.links-box a { color: var(--primary); font-weight: 600; text-decoration: none; }
.links-box a:hover { text-decoration: underline; }
"""

def md_to_html(md):
    # Basic markdown parser to produce clean HTML
    lines = md.split('\n')
    out = []
    in_code = False
    in_list = False
    in_table = False
    
    for line in lines:
        if line.startswith('```'):
            if in_code:
                out.append('</code></pre>')
                in_code = False
            else:
                lang = line[3:].strip()
                out.append(f'<pre><code class="language-{lang}">')
                in_code = True
            continue
        if in_code:
            escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            out.append(escaped)
            continue
        
        # Table detection
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                out.append('<table><tbody>')
                in_table = True
            cols = [c.strip() for c in line.strip().strip('|').split('|')]
            if all(set(c).issubset({'-', ':', ' '}) for c in cols):
                continue  # separator line
            cells = "".join(f'<td>{c}</td>' for c in cols)
            out.append(f'<tr>{cells}</tr>')
            continue
        elif in_table:
            out.append('</tbody></table>')
            in_table = False

        if line.startswith('### '):
            out.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('## '):
            out.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('# '):
            out.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('---'):
            out.append('<hr/>')
        elif line.startswith('- ') or line.startswith('* '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            item = line[2:]
            # formatting
            item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'`(.*?)`', r'<code>\1</code>', item)
            item = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', item)
            out.append(f'<li>{item}</li>')
        elif re.match(r'^\d+\.\s', line):
            if not in_list:
                out.append('<ol>')
                in_list = True
            item = re.sub(r'^\d+\.\s', '', line)
            item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
            item = re.sub(r'`(.*?)`', r'<code>\1</code>', item)
            item = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', item)
            out.append(f'<li>{item}</li>')
        else:
            if in_list:
                out.append('</ul>')
                in_list = False
            if line.strip():
                para = line
                para = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', para)
                para = re.sub(r'`(.*?)`', r'<code>\1</code>', para)
                para = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', para)
                out.append(f'<p>{para}</p>')
    if in_code:
        out.append('</code></pre>')
    if in_list:
        out.append('</ul>')
    if in_table:
        out.append('</tbody></table>')
    return '\n'.join(out)

for i in range(1, len(parts)):
    slug, name, pr_link, issue_link = slug_map[i]
    part_text = parts[i]
    
    # Extract markdown block
    match = re.search(r'```markdown\s*(.*?)\s*```', part_text, re.DOTALL)
    if match:
        md_content = match.group(1).strip()
    else:
        # fallback
        lines = part_text.split('\n')
        md_content = '\n'.join(lines[3:]).strip()
    
    # Extract title
    title_match = re.search(r'^#\s*(.+)$', md_content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else f"{name} Connector for Cognee"
    
    # Save .md file
    md_file_path = os.path.join(blogs_dir, f"{slug}.md")
    with open(md_file_path, 'w') as f:
        f.write(f"<!-- Mergetober 2026 Blog Post: {name} Integration -->\n")
        f.write(f"<!-- Author: Mallikarjun R (@mallikarjunr444-gif) -->\n")
        f.write(f"<!-- Pull Request: {pr_link} -->\n")
        f.write(f"<!-- Issue: {issue_link} -->\n\n")
        f.write(md_content)
    
    # Render HTML
    html_body = md_to_html(md_content)
    html_page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Mergetober 2026</title>
  <meta name="description" content="Open Source Cognee Integration for Mergetober 2026 by Mallikarjun R">
  <meta name="author" content="Mallikarjun R (@mallikarjunr444-gif)">
  <style>{css}</style>
</head>
<body>
  <header>
    <div>
      <a href="../index.html">← Back to Mergetober Hub</a>
    </div>
    <div>
      <span class="badge">Mergetober 2026 · Cognee</span>
    </div>
  </header>
  <main class="article-container">
    <div class="author-card">
      <img src="https://avatars.githubusercontent.com/u/237906152?v=4" alt="Mallikarjun R" class="author-avatar"/>
      <div class="author-info">
        <h4>Mallikarjun R (<a href="https://github.com/mallikarjunr444-gif" target="_blank" rel="noopener">@mallikarjunr444-gif</a>)</h4>
        <p>CSE Student &amp; Open Source Contributor · Bangalore, India</p>
      </div>
    </div>
    <article class="content">
      {html_body}
    </article>
    <div class="links-box">
      <p><strong>🔗 Submission Links:</strong></p>
      <p>• GitHub Pull Request: <a href="{pr_link}" target="_blank" rel="noopener">{pr_link}</a></p>
      <p>• GitHub Issue: <a href="{issue_link}" target="_blank" rel="noopener">{issue_link}</a></p>
      <p>• Built for: <a href="https://www.wemakedevs.org/hackathons/mergetober" target="_blank" rel="noopener">WeMakeDevs Mergetober Hackathon</a></p>
    </div>
  </main>
</body>
</html>
"""
    html_file_path = os.path.join(blogs_dir, f"{slug}.html")
    with open(html_file_path, 'w') as f:
        f.write(html_page)
    
    articles.append({
        'slug': slug,
        'name': name,
        'title': title,
        'pr': pr_link,
        'issue': issue_link,
        'md_file': f"blogs/{slug}.md",
        'html_file': f"blogs/{slug}.html"
    })

# Now generate index.html
cards_html = ""
for a in articles:
    cards_html += f"""
    <div style="background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 24px; margin-bottom: 20px; transition: transform 0.2s, border-color 0.2s;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
        <span class="badge">{a['name']} Connector</span>
        <a href="{a['pr']}" target="_blank" rel="noopener" style="font-size: 0.85rem; color: var(--primary); text-decoration: none;">View GitHub PR ↗</a>
      </div>
      <h3 style="font-size: 1.35rem; margin-bottom: 12px; color: #fff;">
        <a href="{a['html_file']}" style="color: inherit; text-decoration: none;">{a['title']}</a>
      </h3>
      <div style="display: flex; gap: 12px; margin-top: 16px;">
        <a href="{a['html_file']}" style="display: inline-block; background: var(--accent); color: #fff; padding: 8px 16px; border-radius: 6px; text-decoration: none; font-size: 0.9rem; font-weight: 600;">Read Full Blog Post</a>
        <a href="{a['md_file']}" style="display: inline-block; background: var(--code-bg); border: 1px solid var(--border); color: var(--text-muted); padding: 8px 16px; border-radius: 6px; text-decoration: none; font-size: 0.9rem;">Raw Markdown</a>
      </div>
    </div>
    """

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mallikarjun R | Cognee Mergetober 2026 Submission Portfolio</title>
  <meta name="description" content="Open Source Cognee Connectors and Real-World Technical Blog Posts by Mallikarjun R for Mergetober 2026">
  <style>{css}</style>
</head>
<body>
  <div style="max-width: 860px; margin: 40px auto 30px auto; text-align: center;">
    <div class="badge" style="margin-bottom: 16px;">WeMakeDevs × Cognee · Mergetober 2026</div>
    <h1 style="font-size: 2.8rem; font-weight: 700; color: #fff; margin-bottom: 12px; line-height: 1.15;">
      AI Memory Layer Connectors
    </h1>
    <p style="font-size: 1.15rem; color: var(--text-muted); max-width: 650px; margin: 0 auto 24px auto;">
      Complete integration suite and architectural blog posts by <strong>Mallikarjun R</strong> (<a href="https://github.com/mallikarjunr444-gif" target="_blank" rel="noopener" style="color: var(--primary);">@mallikarjunr444-gif</a>).
    </p>
    <div class="author-card" style="max-width: 500px; margin: 0 auto 40px auto; text-align: left;">
      <img src="https://avatars.githubusercontent.com/u/237906152?v=4" alt="Mallikarjun R" class="author-avatar"/>
      <div class="author-info">
        <h4>Mallikarjun R</h4>
        <p>GitHub: @mallikarjunr444-gif · Email: mallikarjunr444@gmail.com</p>
        <p>Bangalore, India · Top Contributor Candidate ($2,000 Prize)</p>
      </div>
    </div>
  </div>

  <main style="max-width: 860px; margin: 0 auto;">
    <h2 style="font-size: 1.6rem; color: #fff; margin-bottom: 20px; border-bottom: 1px solid var(--border); padding-bottom: 10px;">
      Published Integration Blog Posts (7 Total)
    </h2>
    {cards_html}
  </main>
</body>
</html>
"""

with open(os.path.join(output_dir, 'index.html'), 'w') as f:
    f.write(index_html)

# Now generate README.md
readme_content = f"""# Cognee Mergetober 2026 Integration Portfolio & Blogs
**Author:** Mallikarjun R ([@mallikarjunr444-gif](https://github.com/mallikarjunr444-gif))  
**Email:** mallikarjunr444@gmail.com  
**Event:** [WeMakeDevs Mergetober 2026](https://www.wemakedevs.org/hackathons/mergetober)  

---

## 🏆 Published Integration Blog Posts

| Connector | Type | Pull Request | Linked Issue | Live Blog Post |
|---|---|---|---|---|
| **SendGrid** | Path B (Email) | [#438](https://github.com/topoteretes/cognee-community/pull/438) | [#6087](https://github.com/topoteretes/cognee/issues/6087) | [Read Post](blogs/sendgrid.md) |
| **ClickUp** | Path A (Tasks) | [#439](https://github.com/topoteretes/cognee-community/pull/439) | [#4701](https://github.com/topoteretes/cognee/issues/4701) | [Read Post](blogs/clickup.md) |
| **Postmark** | Path B (Email) | [#440](https://github.com/topoteretes/cognee-community/pull/440) | [#6090](https://github.com/topoteretes/cognee/issues/6090) | [Read Post](blogs/postmark.md) |
| **Dub.co** | Path B (Analytics) | [#441](https://github.com/topoteretes/cognee-community/pull/441) | [#6091](https://github.com/topoteretes/cognee/issues/6091) | [Read Post](blogs/dub.md) |
| **Umami** | Path B (Analytics) | [#442](https://github.com/topoteretes/cognee-community/pull/442) | [#6093](https://github.com/topoteretes/cognee/issues/6093) | [Read Post](blogs/umami.md) |
| **Linear** | Path A (Tickets) | [Branch](https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/linear-connector) | [#6100](https://github.com/topoteretes/cognee/issues/6100) | [Read Post](blogs/linear.md) |
| **Twilio** | Path B (Comms) | [Branch](https://github.com/mallikarjunr444-gif/cognee-community/tree/feature/twilio-connector) | [#6100](https://github.com/topoteretes/cognee/issues/6100) | [Read Post](blogs/twilio.md) |

---

## 🛡️ Production Standards
- **100% Ruff Clean**: Enforcing PEP 8 and 100-character line standards.
- **DCO Certified**: All commits signed by Mallikarjun R (`git commit -s`).
- **Resilient Fallback**: Tested against real API schemas with automatic backoff retry logic on rate limits.
"""

with open(os.path.join(output_dir, 'README.md'), 'w') as f:
    f.write(readme_content)

print("Generated all blog markdown, HTML, and index.html successfully!")
