# PDF Title and Headings Extractor

This project is a simple Python tool to automatically extract:
- Document title
- Headings (H1, H2, H3) based on text size

from any PDF file using PyMuPDF.

---

## Features

- Extracts the PDF metadata title, or uses the filename if no title is found.
- Detects headings by checking text font sizes.
- Processes all PDF files in the input folder.
- Saves each result as a JSON file.
- Can run directly with Python or inside a Docker container.

---

## Project Structure

Your folder should look like this:

your-repo/
├── extract_title_and_headings.py # Main extractor script
├── Dockerfile # For running in a container
├── input/ # Place PDF files here
├── output/ # Extracted JSON files will appear here

---

## How to Use (Python)

1. Clone or download this repository.

2. Install the required Python package:


3. Create an `input` folder and place your PDF files inside it.

4. Run the script:


5. Find your JSON output files in the `output` folder.

---

## How to Use (Docker)

1. Build the Docker image:


2. Run the container, mounting your local folders:


This runs the script inside Docker and saves the output to your local `output` folder.

---

## How it Works

- The script reads each PDF file in the `input` folder.
- It checks the PDF metadata for a title.
- It scans all text blocks on each page.
- It assigns headings (H1, H2, H3) based on font size thresholds.
- It saves the result to a JSON file named like `filename_title_headings.json`.

---
