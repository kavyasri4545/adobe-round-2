# 1(a)PDF Title and Headings Extractor

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


# 1(b)PDF Persona-Based Content Extractor

This project is a simple Python tool to automatically extract sections of text from PDF files that are relevant for a specific user persona or goal.

It uses PyMuPDF to scan PDF pages and match keywords that describe what the persona cares about.

---

## Features

- Searches all text in each PDF file for specific keywords.
- Extracts page number, matched keyword, and a text snippet.
- Saves results for each PDF as a JSON file.
- Adds metadata about the persona, goal, and extraction time.
- Can run directly with Python or inside a Docker container.

---

## Project Structure

Your folder should look like this:

your-repo/
├── extract_persona.py # Main extraction script
├── Dockerfile # For running in a container
├── input/ # Place PDF files here
├── output/ # JSON results will be saved here

---

## How to Use with Python

1. Clone or download this repository.

2. Install the required dependency:


3. Create an `input` folder in the same directory and place your PDF files inside it.

4. Open `extract_persona.py` and set your custom settings:

- `PERSONA`: The type of user, for example `Analyst`.
- `JOB`: The task or goal, for example `Find key insights`.
- `KEYWORDS`: A list of words to search for, for example `["revenue", "investment", "trend"]`.

5. Run the script:


6. After the script runs, find your extracted JSON files inside the `output` folder.

---

## How to Use with Docker

1. Build the Docker image:


2. Run the container, mounting your local input and output folders:


This will run the script inside the container and write the results to your local `output` folder.

---

## How It Works

- The script opens each PDF file in the `input` folder.
- It checks the text on each page.
- When a keyword match is found, it saves:
- Document name
- Page number
- Matched keyword
- Rank
- A short text snippet
- All matches are saved with metadata about the persona and goal in a JSON file named `filename_persona.json`.

---


# Requirements
- Python 3.8 or higher
- PyMuPDF

