import html


def C(cod, lang="python"):
    """Bloc de cod pentru teorie (escape HTML)."""
    return f'<pre data-lang="{lang}"><code>{html.escape(cod.strip(chr(10)), quote=False)}</code></pre>'


def O(text, eticheta="ieșire"):
    return f'<pre class="out" data-lang="{eticheta}"><code>{html.escape(text.strip(chr(10)), quote=False)}</code></pre>'


def T(cap, *randuri):
    """Tabel simplu: T(["a","b"], ["x","y"], ...). Celulele sunt HTML."""
    h = '<div class="tbl"><table><tr>' + "".join(f"<th>{c}</th>" for c in cap) + "</tr>"
    for r in randuri:
        h += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return h + "</table></div>"
