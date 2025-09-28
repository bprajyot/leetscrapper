# leetcode_scraper.py
import time
import json
from leetscrape import GetQuestionsList, GetQuestion


def scrape_free_problems(limit: int = 100, output_file: str = "problems.json"):
    """
    Scrape free LeetCode problems and save them into a JSON file.

    Args:
        limit (int): Number of free problems to scrape (default: 100).
        output_file (str): Output JSON file name (default: "problems.json").

    Returns:
        list[dict]: List of scraped problems with title, slug, description, and testcases.
    """
    # Step 1: Get all problems
    ql = GetQuestionsList()
    ql.scrape()  # fetches all problem metadata

    # Step 2: Access the DataFrame of questions
    df = ql.questions  # pandas DataFrame

    # Step 3: Filter free problems
    free_problems = df[df['paidOnly'] == False].head(limit)

    print(f"Total free problems to scrape: {len(free_problems)}")

    # Step 4: Scrape each problem
    problems_list = []
    for idx, row in free_problems.iterrows():
        slug = row['titleSlug']
        title = row['title']

        try:
            q = GetQuestion(titleSlug=slug)
            q.scrape()  # fetch description and examples

            problem_data = {
                "title": title,
                "slug": slug,
                "description": getattr(q, "Body", ""),
                "testcases": getattr(q, "exampleTestcaseList", []),
            }
            problems_list.append(problem_data)
            print(f"✅ Scraped {title} ({idx+1}/{len(free_problems)})")

        except Exception as e:
            print(f"❌ Failed {slug}: {e}")

        time.sleep(1)  # polite delay

    # Step 5: Save results
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(problems_list, f, ensure_ascii=False, indent=2)

    print(f"🎉 Done! Saved {len(problems_list)} problems to {output_file}")
    return problems_list
