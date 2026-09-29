import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path("official-waveshare-source/ESP-IDF/08_ESP32-S3_e-Paper-3.97")
CACHE = Path("translation-cache.json")
HAN = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")
LITERAL = re.compile(r'"(?:\\.|[^"\\])*"')
SKIP = {
    "高温 %d℃", "低温 %d℃", "特别行政区", "自治州", "自治区",
    "省", "市", "区", "县", "盟", "初一",
}


def translate(text: str) -> str:
    params = urllib.parse.urlencode({
        "client": "gtx", "sl": "zh-CN", "tl": "en", "dt": "t", "q": text
    })
    url = "https://translate.googleapis.com/translate_a/single?" + params
    with urllib.request.urlopen(url, timeout=30) as response:
        data = json.load(response)
    return "".join(part[0] for part in data[0]).strip()


cache = json.loads(CACHE.read_text("utf-8")) if CACHE.exists() else {}
files = [p for p in ROOT.rglob("*") if p.suffix.lower() in {".c", ".cc", ".cpp", ".h", ".hpp", ".html", ".js"}]

for path in files:
    source = path.read_text("utf-8")
    changed = False
    lines = []
    for line in source.splitlines(keepends=True):
        stripped = line.lstrip()
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
            lines.append(line)
            continue
        for match in reversed(list(LITERAL.finditer(line))):
            raw = match.group()[1:-1]
            if not HAN.search(raw) or raw in SKIP or any(x in line for x in ("sscanf(", "ESP_LOG", "strcmp(", "strstr(")):
                continue
            if raw not in cache:
                cache[raw] = translate(raw)
                CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), "utf-8")
                time.sleep(0.08)
            replacement = cache[raw].replace("\\", "\\\\").replace('"', '\\"')
            line = line[:match.start() + 1] + replacement + line[match.end() - 1:]
            changed = True
        lines.append(line)
    if changed:
        path.write_text("".join(lines), "utf-8")

print(f"translated {len(cache)} unique UI strings")
