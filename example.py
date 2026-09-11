"""
Minimal working example: run the "Facebook Comments Scraper" Apify Actor
and print its results.

Setup:
    pip install apify-client
    export APIFY_TOKEN=your_apify_token_here   # console.apify.com > Settings > Integrations

This repo is just usage documentation for the Actor — the Actor's own source
code is not included here (it runs on Apify's infrastructure).
"""
import os
import sys

from apify_client import ApifyClient

APIFY_TOKEN = os.environ.get("APIFY_TOKEN")
ACTOR_ID = "leadsbrary/facebook-comments-scraper"

RUN_INPUT = {
    "startUrls": [
        {
            "url": "https://www.facebook.com/humansofnewyork/posts/pfbid0BbKbkisExKGSKuhee9a7i86RwRuMKFC8NSkKStB7CsM3uXJuAAfZLrkcJMXxhH4Yl"
        }
    ],
    "resultsLimit": 100,
    "viewOption": "RANKED_UNFILTERED",
    "includeNestedComments": false,
    "includeDate": true,
    "includeAuthor": true,
    "includeProfileUrl": true,
    "includeLikes": true,
    "includeReplies": true,
    "includePostUrl": true,
    "includeCommentUrl": true,
    "includePostId": true
}


def main() -> None:
    if not APIFY_TOKEN:
        sys.exit("Set the APIFY_TOKEN environment variable first (get one at console.apify.com).")

    client = ApifyClient(APIFY_TOKEN)

    print(f"Starting {ACTOR_ID} ...")
    run = client.actor(ACTOR_ID).call(run_input=RUN_INPUT)
    print(f"Run finished with status: {run['status']}")

    print("Results:")
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)


if __name__ == "__main__":
    main()
