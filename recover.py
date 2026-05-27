import json
import re

log_file = "/Users/shimseunggi/.gemini/antigravity/brain/6621248f-250a-448a-bcb4-ea882757d524/.system_generated/logs/transcript.jsonl"

with open(log_file, "r") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "TOOL_RESPONSE":
            for tool_resp in data.get("tool_responses", []):
                if tool_resp.get("name") == "default_api:view_file":
                    out = tool_resp.get("response", {}).get("output", "")
                    if "Total Lines: 712" in out:
                        # Extract the lines
                        lines = out.split("\n")
                        content = []
                        start = False
                        for l in lines:
                            if re.match(r'^1: ', l):
                                start = True
                            if start:
                                m = re.match(r'^\d+: (.*)$', l)
                                if m:
                                    content.append(m.group(1))
                                else:
                                    # Might be an empty line or end of file output
                                    if re.match(r'^\d+:$', l):
                                        content.append("")
                        with open("/Users/shimseunggi/Desktop/NURA/shim/nura-homepage/index.html", "w") as out_f:
                            out_f.write("\n".join(content) + "\n")
                        print("Recovered!")
                        exit(0)
