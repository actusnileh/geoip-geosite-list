import os
import shutil
import git

REPO_URL = "https://github.com/v2fly/domain-list-community.git"
CACHE_PATH = "./.cache"
CACHE_DOMAINS_PATH = os.path.join(CACHE_PATH, "data")
DOMAINS_FILE = "domains.txt"


def generate():
    print("Generating .txt file with domains...")

    if os.path.exists(CACHE_PATH):
        print("Tool cache found. Clearing...")
        shutil.rmtree(CACHE_PATH)

    git.Repo.clone_from(REPO_URL, CACHE_PATH)

    with open(DOMAINS_FILE, "w") as domains_txt:
        for item in os.listdir(CACHE_DOMAINS_PATH):
            item_path = os.path.join(CACHE_DOMAINS_PATH, item)
            if os.path.isfile(item_path):
                domains_txt.write(item + "\n")

    shutil.rmtree(CACHE_PATH)
    print("Tool cache cleared.")

    absolute_path = os.path.abspath(DOMAINS_FILE)
    print(
        f"\nDomains generated successfully.\nFind the generated file at: {absolute_path}"
    )
