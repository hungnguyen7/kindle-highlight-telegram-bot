import os
import psycopg2
import psycopg2.extras
import json


class BaseConnection:
    def __init__(self, collection_name=None):
        if collection_name is None:
            raise ValueError("Collection name must be provided.")
        
        self.collection_name = collection_name
        self.database_url = os.getenv("DATABASE_URL")
        
        if not self.database_url:
            raise ValueError("DATABASE_URL environment variable is required")
        
        # Use PostgreSQL
        try:
            self.conn = psycopg2.connect(self.database_url)
            self.conn.autocommit = True
            self._init_postgres_tables()
        except Exception as e:
            print(f"Error connecting to PostgreSQL: {e}")
            raise
    
    def _init_postgres_tables(self):
        with self.conn.cursor() as cur:
            if self.collection_name == 'schedules':
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS schedules (
                        id BIGINT PRIMARY KEY,
                        interval INTEGER NOT NULL
                    )
                """)
            elif self.collection_name == 'highlights':
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS highlights (
                        id SERIAL PRIMARY KEY,
                        chat_id BIGINT NOT NULL,
                        book_title TEXT NOT NULL,
                        location TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        text TEXT NOT NULL
                    )
                """)
    
    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()
