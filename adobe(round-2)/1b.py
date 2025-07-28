import os
import fitz
import json
from datetime import datetime

def persona_extraction(filepath, persona, job, keywords):
    doc = fitz.open(filepath)
    relevant = []
    rank = 0
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        for kw in keywords:
            if kw.lower() in text.lower():
                relevant.append({
                    "document": os.path.basename(filepath),
                    "page_number": page_num,
                    "matched_keyword": kw,
                    "importance_rank": rank + 1,
                    "snippet": text[:300]
                })
                rank += 1
                break
    return relevant

def run(input_dir, output_dir, persona, job, keywords):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(input_dir, filename)
            result = {
                "metadata": {
                    "persona": persona,
                    "job": job,
                    "input_document": filename,
                    "timestamp": datetime.now().isoformat()
                },
                "extracted_sections": persona_extraction(filepath, persona, job, keywords)
            }
            output_path = os.path.join(output_dir, filename.replace(".pdf", "_persona.json"))
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Saved persona extract: {output_path}")

if __name__ == "__main__":
    INPUT_DIR = "input"
    OUTPUT_DIR = "output"
    PERSONA = "Analyst"
    JOB = "Find key business info"
    KEYWORDS = ["revenue", "market", "trend", "investment", "methodology"]
    run(INPUT_DIR, OUTPUT_DIR, PERSONA, JOB, KEYWORDS)
