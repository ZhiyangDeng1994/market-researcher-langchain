import re

_NUM = re.compile(r"\d[\d,.]*\s?(%|x|GW|MW|TWh|bn|billion|million)", re.I)
_SOURCE = re.compile(r"(source|\*[^*]+\*|filing|10-K|report|research|institute|lab|EIA|IEA)", re.I)


def flag_unsourced(text: str) -> str:
    out = []
    for line in text.splitlines():
        stripped = line.lstrip()
        # skip headers, table rows, and blockquotes — only check prose
        if stripped.startswith(("#", "|", ">")):
            out.append(line)
            continue
        if _NUM.search(line) and not _SOURCE.search(line):
            out.append(line + "  `[UNSOURCED]`")
        else:
            out.append(line)
    return "\n".join(out)