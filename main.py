# main.py
from scraper import scrape_free_problems
from updater import update_problems_file


def main():
    scraped = scrape_free_problems(
        limit=50,
        output_file="problems.json"
    )
    print(f"✅ Scraped {len(scraped)} problems")

    # Step 2: Update descriptions and testcases
    updated = update_problems_file(
        input_file="problems.json",
        output_file="leetcode_updated.json"
    )
    print(f"✅ Updated {len(updated)} problems with clean descriptions and testcases")


if __name__ == "__main__":
    main()
