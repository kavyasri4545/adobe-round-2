import os
import fitz  # PyMuPDF
import json

def detect_heading_level(size):
    if size > 20:
        return "H1"
    elif size > 15:
        return "H2"
    elif size > 12:
        return "H3"
    return None

def extract_title_and_headings(filepath):
    doc = fitz.open(filepath)
    title = doc.metadata.get("title") or os.path.basename(filepath).replace(".pdf", "")
    headings = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                spans = [
                    span for line in block["lines"] for span in line["spans"]
                    if span["text"].strip()
                ]
                for span in spans:
                    text = span["text"].strip()
                    size = span["size"]
                    heading_level = detect_heading_level(size)
                    if heading_level:
                        headings.append({
                            "level": heading_level,
                            "text": text,
                            "page": page_num
                        })

    return {
        "file": os.path.basename(filepath),
        "title": title,
        "headings": headings
    }

def run(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(input_dir, filename)
            result = extract_title_and_headings(filepath)
            output_path = os.path.join(output_dir, filename.replace(".pdf", "_title_headings.json"))
            with open(output_path, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Saved: {output_path}")

if __name__ == "__main__":
    INPUT_DIR = "input"
    OUTPUT_DIR = "output"
    run(INPUT_DIR, OUTPUT_DIR)
