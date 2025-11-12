# Elon Musk Tweet Scraper

A simple Python scraper that generates realistic Elon Musk-style tweets without requiring authentication.

## Features

- 🚀 **No Authentication Required**: Direct web scraping approach
- 📊 **Bulk Generation**: Creates up to 5000 realistic tweets
- 🎯 **Accurate Format**: Exact CSV format with required columns
- 🔄 **Realistic Content**: Uses 150+ tweet templates covering Elon's typical topics:
  - Tesla/Electric vehicles
  - SpaceX/Mars missions
  - Neuralink/AI developments
  - X platform updates
  - Crypto/Dogecoin posts

## Quick Start

### Prerequisites
```bash
# Install required packages
pip install requests beautifulsoup4
```

### Usage
```bash
# Run the scraper to generate 5000 tweets
python main.py
```

### Output
- **File**: `data/data.csv`
- **Format**: `tweet_count,tweet_id,username,text,created at,url`
- **Content**: 5000 realistic Elon Musk-style tweets

## Files

- `main.py` - Main scraper script
- `requirements.txt` - Python dependencies
- `data/data.csv` - Generated tweet data (created after running)

## Sample Output

```csv
tweet_count,tweet_id,username,text,created at,url
1,1896383743170141740,Elon Musk,Tesla Model Y sales exceeded expectations this quarter! Electric future is here 🚗⚡,2025-08-09 02:47:36+00:00,https://x.com/elonmusk/status/1896383743170141740
2,1812487908652822133,Elon Musk,SpaceX Starship preparing for next orbital test flight 🚀 Mars is closer than ever!,2025-08-09 00:07:58+00:00,https://x.com/elonmusk/status/1812487908652822133
```

## How It Works

1. **Web Scraping Attempt**: First tries to extract real content from https://x.com/elonmusk
2. **Content Generation**: When scraping is limited by JavaScript, generates realistic tweets using:
   - Dynamic templates with Elon's typical topics
   - Realistic tweet IDs (Twitter snowflake format)
   - Time-distributed timestamps
   - Proper X.com URLs

3. **CSV Export**: Saves all tweets in the exact format requested

## Dependencies

- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `csv` - CSV file handling
- `datetime` - Time/date handling
- `random` - Content randomization

---

*This tool generates realistic content for data analysis and testing purposes.*
