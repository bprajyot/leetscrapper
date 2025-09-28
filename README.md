# LeetCode Scraper

This repository contains a Python-based tool for scraping free LeetCode problem data, including problem descriptions and test cases, and updating them in a structured JSON format. The tool uses the `leetscrape` library along with `BeautifulSoup` for parsing HTML content to extract clean problem descriptions and test cases.

## Features
- **Scrape Free Problems**: Fetches metadata, descriptions, and test cases for free LeetCode problems.
- **Clean Descriptions**: Extracts problem descriptions in plain text, removing unnecessary HTML and stopping before examples or constraints.
- **Test Case Extraction**: Captures test cases from problem examples for use in testing or validation.
- **Update Existing Data**: Updates an existing JSON file with refreshed descriptions and test cases.

## Files
- **`scraper.py`**: Contains the `scrape_free_problems` function to scrape free LeetCode problems and save them to a JSON file.
- **`updater.py`**: Includes the `update_problems_file` function to update problem descriptions and test cases in an existing JSON file.
- **`main.py`**: Orchestrates the scraping and updating process, serving as the entry point for the tool.

## Prerequisites
- Python 3.8+
- Required libraries:
  - `leetscrape`
  - `beautifulsoup4`
  - `pandas`
- Install dependencies using:
  ```bash
  pip install leetscrape beautifulsoup4 pandas
