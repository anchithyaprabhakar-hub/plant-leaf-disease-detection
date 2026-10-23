"""
Compiles PROJECT_REPORT.md into a print-ready, pagination-styled HTML document.
Can be opened in Chrome/Safari and printed directly to PDF (Cmd+P -> Save as PDF).
"""

from pathlib import Path
import re

def markdown_to_html(md_text):
    html = md_text
    
    # Tables
    def repl_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)
        table_html = "<table class='report-table'><thead><tr>"
        headers = [c.strip() for c in lines[0].strip("|").split("|")]
        for h in headers:
            table_html += f"<th>{h}</th>"
        table_html += "</tr></thead><tbody>"
        for row in lines[2:]:
            cols = [c.strip() for c in row.strip("|").split("|")]
            table_html += "<tr>"
            for col in cols:
                table_html += f"<td>{col}</td>"
            table_html += "</tr>"
        table_html += "</tbody></table>"
        return table_html

    table_pattern = re.compile(r'(\|.+?\|\n\|[-: |]+\|\n(?:\|.+?\|\n?)+)', re.MULTILINE)
    html = table_pattern.sub(repl_table, html)
    
    # Headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.*?)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Bold / Italics
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # Page breaks
    html = html.replace('<div style="page-break-after: always;"></div>', '<div class="page-break"></div>')
    
    # Paragraphs
    paragraphs = html.split("\n\n")
    processed = []
    for p in paragraphs:
        p_str = p.strip()
        if p_str.startswith("<h") or p_str.startswith("<table") or p_str.startswith("<div") or p_str.startswith("<pre"):
            processed.append(p_str)
        elif p_str:
            processed.append(f"<p>{p_str}</p>")
    return "\n".join(processed)


def build_printable_report():
    base_dir = Path(__file__).resolve().parent
    report_md = base_dir / "PROJECT_REPORT.md"
    output_html = base_dir / "PROJECT_REPORT.html"
    
    with open(report_md, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    body_content = markdown_to_html(md_content)
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Plant Leaf Disease Detection System - Project Report</title>
<style>
  @page {{
    size: A4;
    margin: 20mm 20mm 20mm 20mm;
    @bottom-center {{
      content: counter(page);
    }}
  }}
  body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #111;
    margin: 0;
    padding: 0;
  }}
  .page-break {{
    page-break-after: always;
    break-after: page;
  }}
  h1 {{
    font-size: 18pt;
    text-align: center;
    margin-top: 24pt;
    margin-bottom: 12pt;
    text-transform: uppercase;
  }}
  h2 {{
    font-size: 14pt;
    margin-top: 18pt;
    margin-bottom: 8pt;
    border-bottom: 1px solid #333;
    padding-bottom: 3pt;
  }}
  h3 {{
    font-size: 12pt;
    margin-top: 12pt;
    margin-bottom: 6pt;
  }}
  p {{
    text-align: justify;
    margin-bottom: 8pt;
    text-indent: 1.5em;
  }}
  .report-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 12pt 0;
    font-size: 10pt;
  }}
  .report-table th, .report-table td {{
    border: 1px solid #444;
    padding: 6pt 8pt;
    text-align: left;
  }}
  .report-table th {{
    background-color: #f0f0f0;
    font-weight: bold;
  }}
  pre {{
    background: #f8f8f8;
    border: 1px solid #ddd;
    padding: 8pt;
    font-size: 9pt;
    font-family: 'Courier New', monospace;
    overflow-x: auto;
    page-break-inside: avoid;
  }}
  code {{
    font-family: 'Courier New', monospace;
    background: #f2f2f2;
    padding: 1pt 3pt;
    font-size: 9.5pt;
  }}
  .cover-container {{
    text-align: center;
    padding-top: 40pt;
  }}
</style>
</head>
<body>
{body_content}
</body>
</html>
"""
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(template)
        
    print(f"Generated printable report at: {output_html}")

if __name__ == "__main__":
    build_printable_report()
