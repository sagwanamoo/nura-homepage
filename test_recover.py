import json

log_file = "/Users/shimseunggi/.gemini/antigravity/brain/6621248f-250a-448a-bcb4-ea882757d524/.system_generated/logs/transcript.jsonl"

with open(log_file, "r") as f:
    for line in f:
        data = json.loads(line)
        if data.get("type") == "TOOL_RESPONSE":
            for tool_resp in data.get("tool_responses", []):
                if tool_resp.get("name") == "default_api:view_file":
                    out = tool_resp.get("response", {}).get("output", "")
                    if "Total Lines: 712" in out:
                        print("Found view_file with 712 lines!")
                        print(out[:500])
                        exit(0)
