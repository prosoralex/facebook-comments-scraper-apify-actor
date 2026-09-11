# Facebook Comments Scraper — Apify Actor usage guide

Extract comments from any public Facebook post, reel, or video. Get comment text, date, author name, profile link, reaction count, and reply count. Configure output fields, filter by date, sort results. Export as JSON, CSV, or Excel.

> **This repository does not contain the Actor's source code.** The Actor
> itself is closed-source and runs on Apify's infrastructure — this repo is
> just documentation and example client code showing how to call it via the
> Apify API/SDK with your own Apify API token. Think of it as a "cookbook"
> repo, not the product itself.

**Run it on Apify →** [https://apify.com/leadsbrary/facebook-comments-scraper?fpr=aupara](https://apify.com/leadsbrary/facebook-comments-scraper?fpr=aupara)

## What it does

A scraper that extracts comments and comment-level metadata from public Facebook posts, reels, videos, and photo posts. The Actor visits provided public post URLs, automatically paginates through comment threads, and produces structured records per comment that include comment text, commenter display name and profile link, timestamps, aggregated reaction totals, reply counts and nested replies, unique identifiers, and post context such as post URL, title/excerpt and numeric post ID. The tool supports configurable output fields, date-based filtering, multiple sort-order modes (relevance, threaded/grouped replies, recent activity), and scalable pagination for large comment sections, enabling comment-level engagement and audience data extraction for downstream analysis.…

## Pricing

Pay-per-event pricing — you only pay for what the Actor actually delivers:

- **Actor Start** — $0.00005 (one-time, per run). Charged when the Actor starts running. Number of events charged depends on Actor memory (one event per GB, minimum one event).
- **result** — $0.002–$0.0012 depending on your Apify usage tier. Single result in the default dataset.

*(Apify may also charge a small amount for the platform compute the Actor
uses while running — see the [pricing tab](https://apify.com/leadsbrary/facebook-comments-scraper?fpr=aupara) on the Actor page
for exact current numbers.)*

## Quick start

You need an Apify account and API token (`console.apify.com` → Settings →
Integrations). Don't have one yet? See the signup section below — new
accounts get **$5 of free usage credit every month**.

### cURL

```bash
curl -X POST "https://api.apify.com/v2/acts/leadsbrary~facebook-comments-scraper/runs?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
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
}'
```

### Python (`apify-client`)

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")

run_input = {
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

run = client.actor("leadsbrary/facebook-comments-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
```

### JavaScript (`apify-client`)

```javascript
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: 'YOUR_APIFY_TOKEN' });

const runInput = {
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
};

const run = await client.actor('leadsbrary/facebook-comments-scraper').call(runInput);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items);
```

See [`example.py`](./example.py) in this repo for a complete runnable script.

## Don't have an Apify account yet?

[Sign up here](https://console.apify.com/sign-up?fpr=aupara) — new accounts get **$5 of free platform credit
every month**, enough to try most Actors without paying anything upfront.
Browsing for other tools? The full [Apify Store](https://apify.com/store?fpr=aupara) has thousands
of ready-made Actors.

## Links

- Actor page (run it, see live pricing/reviews): [https://apify.com/leadsbrary/facebook-comments-scraper?fpr=aupara](https://apify.com/leadsbrary/facebook-comments-scraper?fpr=aupara)
- All Actors from this developer: [https://apify.com/leadsbrary?fpr=aupara](https://apify.com/leadsbrary?fpr=aupara)
- Apify API docs: [https://docs.apify.com/api/v2](https://docs.apify.com/api/v2)

## License

The example code in this repository (README snippets, `example.py`) is
released under the MIT License — see [LICENSE](./LICENSE). This does not
cover the Actor itself, which remains closed-source and is operated by its
developer on the Apify platform.
