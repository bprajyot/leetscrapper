# leetcode_updater.py
import json
import re
from leetscrape import GetQuestion
from bs4 import BeautifulSoup


def extract_problem_description(html_body: str) -> str:
    """Extracts clean problem description from HTML body."""
    soup = BeautifulSoup(html_body, "html.parser")
    problem_paragraphs = []
    for p in soup.find_all('p'):
        # Stop at examples, constraints, or follow-ups
        if p.find('strong', class_="example") or "Constraints" in p.get_text() or "Follow-up" in p.get_text():
            break
        text = p.get_text(" ", strip=True)  # Replace tags with spaces
        text = re.sub(r'\s+', ' ', text)    # Collapse multiple spaces
        problem_paragraphs.append(text)
    return "\n".join(problem_paragraphs)


def extract_testcases(html_body: str) -> list[str]:
    """Extracts test cases/examples from HTML body."""
    soup = BeautifulSoup(html_body, "html.parser")
    testcases = []

    # Each example is usually under <strong class="example"> followed by <pre> block
    for example in soup.find_all('strong', class_='example'):
        pre_tag = example.find_next('pre')
        if pre_tag:
            text = pre_tag.get_text().strip()
            if text:
                testcases.append(text)
    return testcases


def update_problems_file(input_file: str = "problems.json", output_file: str = "problems.json") -> list[dict]:
    """
    Update problem descriptions and testcases for problems in a JSON file.

    Args:
        input_file (str): Path to input JSON file (default: "problems.json").
        output_file (str): Path to output JSON file (default: same as input_file).

    Returns:
        list[dict]: Updated list of problems with refreshed description and testcases.
    """
    # Load problems
    with open(input_file, "r", encoding="utf-8") as f:
        problems = json.load(f)

    for problem in problems:
        slug = problem["slug"]
        try:
            q = GetQuestion(titleSlug=slug)
            q.scrape()
            html_body = getattr(q, "Body", "")

            # Extract updated data
            problem["description"] = extract_problem_description(html_body)
            problem["testcases"] = extract_testcases(html_body)

            print(f"✅ Updated: {problem['title']} ({len(problem['testcases'])} testcases)")
        except Exception as e:
            print(f"❌ Failed to update {problem['title']}: {e}")

    # Save updated problems
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)

    print(f"🎉 All problems updated and saved to {output_file}")
    return problems
