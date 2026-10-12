# Threat Intel Lookup

Fetches the most-reported IPs from the AbuseIPDB blacklist, enriches each one with country, ISP, and usage type, and ranks them by total reports to help prioritize which to investigate. It also summarizes the results by usage type.

## How it works

`fetch_data.py` pulls the top-reported IPs from the AbuseIPDB blacklist (50 by default) and saves them to `blacklist.json`.
2. `lookup.py` reads `blacklist.json` and queries the AbuseIPDB check endpoint for each IP, adding details like country, ISP, and usage type. Results are cached in `checked.json`, keyed by IP, and IPs that are already cached are skipped, so re-runs don't use up API quota.
3. `report.py` reads `checked.json`, ranks IPs by total reports, prints category and country counts, and writes `top-10.csv`.

## Setup

1. Python 3.13 or newer.
2. Install dependencies:
```
   pip install -r requirements.txt
```
3. Create a free account at [abuseipdb.com](https://www.abuseipdb.com) and generate an API key.
4. Create a `.env` file in the project folder containing:
```
   API_KEY=your_key_here
```

Make sure to add .env to .gitignore before pushing the code.

## Usage

```
python fetch_data.py
python lookup.py
python report.py
```

## Finding

In a snapshot of the 50 highest-confidence IPs on the AbuseIPDB blacklist, 33 (66%) belonged to data centers or hosting providers, 16 (32%) to fixed-line ISPs, and 1 to a mobile ISP. The seven most-reported IPs were all in data centers, with roughly 53,000 to 209,000 reports each. The most-reported fixed-line IP ranked eighth, with about 9,700.

This is a single day's snapshot at one confidence level, so it says nothing about attackers in general. Report counts show how often an IP was reported, not how much harm it caused.

## Limitations and next steps

- Every IP on the free blacklist has a confidence score of 100, so the score can't be used to rank them. Ranking uses total reports instead.
- Country is where an IP is registered, which isn't necessarily where the attacker is.

## Data and terms

All data comes from AbuseIPDB through each user's own API key. Real API results are not included in this repository. Please read [AbuseIPDB's terms](https://www.abuseipdb.com) before reusing or sharing results.
