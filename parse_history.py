import json
import re

# We will parse the javascript object from site-data.js manually
with open('data/site-data.js', 'r') as f:
    content = f.read()

# Extract historyData string
history_match = re.search(r'historyData:\s*\[(.*?)\]\s*,', content, re.DOTALL)
if not history_match:
    print("Could not find historyData")
    exit(1)

history_str = '[' + history_match.group(1) + ']'
# It's not pure JSON, it has unquoted keys like `year:`, `featured:`, `items:`
history_str = re.sub(r'(\w+):', r'"\1":', history_str)
# Remove trailing commas
history_str = re.sub(r',\s*}', '}', history_str)
history_str = re.sub(r',\s*\]', ']', history_str)

history = json.loads(history_str)

presidents = []
launches = []
conferences = []

for entry in history:
    year = entry.get('year')
    for item in entry.get('items', []):
        # 1. Presidents
        # e.g., "제1대 회장 인하대학교 이훈희"
        # e.g., "제15대 회장 경북대학교 손민수, 부회장 건국대학교 길하종, 총무 조선대학교 엄태호"
        # e.g., "제34대 회장 한국항공대학교 신동욱, 부회장 서울대학교 서지완(직무대행 광주과학기술원 이창현), 총무 이화여자대학교 박세연"
        if "회장" in item and "대 회장" in item:
            m = re.match(r'제(\d+)대\s+회장\s+([^,]+)(?:,\s*부회장\s+([^,]+))?(?:,\s*총무\s+([^,]+))?', item)
            if m:
                gen = int(m.group(1))
                # Next year is year+1? Actually term is year-year+1 or similar.
                # In site-data.js: { generation: 35, name: "이창현", term: "2025-2026", vicePresident: "한재경", secretary: "윤원빈" }
                term = f"{year-1}-{year}" if year > 1992 else str(year)
                # Let's fix term later, just get values
                name = m.group(2).strip()
                president_name = name.split()[-1]
                president_univ = " ".join(name.split()[:-1])
                vp = m.group(3).strip() if m.group(3) else ""
                sec = m.group(4).strip() if m.group(4) else ""
                vp_clean = vp.split()[-1] if vp else ""
                sec_clean = sec.split()[-1] if sec else ""
                if "(" in vp: # "서지완(직무대행 광주과학기술원 이창현)"
                    vp_clean = vp
                if " " in vp:
                    vp_name = vp.split()[-1]
                else:
                    vp_name = vp
                    
                presidents.append({
                    "generation": gen,
                    "name": name, # keep full name with university for now
                    "term": year,
                    "vicePresident": vp,
                    "secretary": sec,
                    "raw": item
                })
        
        # 2. Launch
        # e.g., "제1회 로켓발사대회(한국항공대학교)", "7월 11일 제12회 로켓발사대회", "제26회 전국대학교 로켓발사대회 및 학술대회"
        if "발사대회" in item:
            m = re.search(r'제(\d+)회[^\(]*발사대회(?:\((.*?)\))?', item)
            if m:
                gen = int(m.group(1))
                info = m.group(2) if m.group(2) else ""
                launches.append({
                    "year": gen, # it's actually generation
                    "rank": "",
                    "university": info,
                    "raw": item,
                    "year_val": year
                })

        # 3. Conference
        # e.g., "제28회 전국대학교 로켓학술대회(순천대학교)"
        if "학술대회" in item:
            m = re.search(r'제(\d+)회[^\(]*학술대회(?:\((.*?)\))?', item)
            if m:
                gen = int(m.group(1))
                info = m.group(2) if m.group(2) else ""
                conferences.append({
                    "year": gen,
                    "rank": "",
                    "university": info,
                    "raw": item,
                    "year_val": year
                })

print("Presidents:", json.dumps(presidents, ensure_ascii=False, indent=2))
print("Launches:", json.dumps(launches, ensure_ascii=False, indent=2))
print("Conferences:", json.dumps(conferences, ensure_ascii=False, indent=2))
