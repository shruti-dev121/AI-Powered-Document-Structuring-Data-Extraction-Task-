import os
from google import genai
import pandas as pd
import json
import re

# Initialize Gemini client
client = genai.Client(api_key="AIzaSyB-################api key########")

# Upload PDF
pdf_file = "Data Input.pdf"
uploaded = client.files.upload(file=pdf_file, config={"mime_type": "application/pdf"})

# Prompt: let AI determine keys dynamically
prompt = """
Extract all information from the uploaded PDF.
- Dynamically determine keys (do not predefine them).
- Identify logical relationships and provide context.
- Include any relevant details in 'Comments'.
- Output strictly as JSON: a list of objects with fields: key, value, comments.
"""

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[uploaded, prompt]
)

# Access model output
if hasattr(response, "output") and response.output:
    raw_text = response.output[0].content[0].text
else:
    raw_text = response.text

# Preview first 500 chars
print("Preview of raw output:\n", raw_text[:500], "...")

# Try parsing JSON
try:
    data = json.loads(raw_text)
except json.JSONDecodeError:
    # Fallback: parse Key-Value-Comments dynamically with regex
    pattern = r'"?key"?\s*:\s*"(.*?)"\s*,\s*"?value"?\s*:\s*"(.*?)"\s*,\s*"?comments"?\s*:\s*"(.*?)"'
    matches = re.findall(pattern, raw_text, re.DOTALL | re.IGNORECASE)
    data = [{"Key": k.strip(), "Value": v.strip(), "Comments": c.strip()} for k, v, c in matches]

# Normalize keys if JSON has lowercase
if all(isinstance(i, dict) for i in data):
    df = pd.DataFrame([
        {
            "Key": item.get("key") or item.get("Key"),
            "Value": item.get("value") or item.get("Value"),
            "Comments": item.get("comments") or item.get("Comments")
        } for item in data
    ])
else:
    df = pd.DataFrame(data)

# Save to Excel
df.to_excel("Expected_output.xlsx", index=False)
print(f"✅ Excel saved with {len(df)} rows, keys determined dynamically by LLM.")

