import os
import pandas as pd
from dotenv import load_dotenv
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

load_dotenv()

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

db_path = os.getenv("LANCEDB_PATH")
table_name = os.getenv("LANCEDB_TABLE")

# If db_path is not set or doesn't exist, use a default relative to script directory
if not db_path:
    db_path = os.path.join(script_dir, "data", "lancedb")
    print(f"LANCEDB_PATH not set, using default: {db_path}")

# If table_name is not set, use default
if not table_name:
    table_name = "tweets"
    print(f"LANCEDB_TABLE not set, using default: {table_name}")

# Ensure the directory exists
os.makedirs(db_path, exist_ok=True)

model = get_registry().get("sentence-transformers").create(name="all-mpnet-base-v2")

class TweetDocument(LanceModel):
    tweet_count: int
    tweet_id: int
    username: str
    text: str = model.SourceField()
    created_at: str
    url: str
    vector: Vector(model.ndims()) = model.VectorField()

db = lancedb.connect(db_path)
model = get_registry().get("sentence-transformers").create(name="all-mpnet-base-v2")

def initialize_database():
    print(f"Initializing database...")
    print(f"Script directory: {script_dir}")
    print(f"Database path: {db_path}")
    print(f"Table name: {table_name}")
    print(f"Current working directory: {os.getcwd()}")
    
    db = lancedb.connect(db_path)
    
    # Debug: Print available tables
    existing_tables = db.table_names()
    print(f"Existing tables: {existing_tables}")

    if table_name in existing_tables:
        print(f"Table '{table_name}' already exists. Opening...")
        try:
            tbl = db.open_table(table_name)
            print(f"Successfully opened table '{table_name}' with {len(tbl)} rows")
            return tbl
        except Exception as e:
            print(f"Error opening existing table: {str(e)}")
            print("Dropping table and recreating...")
            db.drop_table(table_name)
    
    print("Creating new table...")
    try:
        # Try to read CSV with different encodings and different possible paths
        csv_path = os.path.join(script_dir, "data", "elonmusk_tweets.csv")
        
        # If the file doesn't exist in the expected location, try alternative paths
        if not os.path.exists(csv_path):
            # Try current directory
            csv_path = "data/elonmusk_tweets.csv"
            if not os.path.exists(csv_path):
                # Try parent directory
                csv_path = os.path.join(os.path.dirname(script_dir), "data", "elonmusk_tweets.csv")
                if not os.path.exists(csv_path):
                    raise FileNotFoundError(f"Could not find elonmusk_tweets.csv in expected locations. Script dir: {script_dir}")
        
        print(f"Loading CSV from: {csv_path}")
        
        try:
            tweets_df = pd.read_csv(csv_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                tweets_df = pd.read_csv(csv_path, encoding='latin-1')
            except UnicodeDecodeError:
                tweets_df = pd.read_csv(csv_path, encoding='cp1252')
        
        print(f"Loaded CSV with {len(tweets_df)} rows")
        print(f"CSV columns: {tweets_df.columns.tolist()}")
        
        # Clean the data and handle missing URLs
        def clean_text(text):
            if pd.isna(text):
                return ""
            return str(text).replace('\xa0', ' ').replace('\u00a0', ' ').strip()
        
        # Apply text cleaning
        tweets_df['text'] = tweets_df['text'].apply(clean_text)
        tweets_df['username'] = tweets_df['username'].apply(clean_text)
        
        # Generate URL if missing
        if 'url' not in tweets_df.columns:
            tweets_df['url'] = tweets_df.apply(
                lambda row: f"https://twitter.com/{row['username']}/status/{row['tweet_id']}" 
                if pd.notna(row.get('tweet_id')) and pd.notna(row.get('username')) 
                else "", axis=1
            )
        
        data = tweets_df.apply(
            lambda row: {
                "tweet_count": row["tweet_count"],
                "tweet_id": row["tweet_id"],
                "username": row["username"],
                "text": row["text"],
                "created_at": row["created at"],
                "url": row["url"]
            },
            axis=1
        ).tolist()
        
        print(f"Prepared {len(data)} records for insertion")

        table = db.create_table(table_name, schema=TweetDocument)
        table.add(data)
        table.create_fts_index("text")

        print(f"Table '{table_name}' created successfully with {len(table)} rows")
        return table
        
    except Exception as e:
        print(f"Error during database initialization: {str(e)}")
        import traceback
        traceback.print_exc()
        raise