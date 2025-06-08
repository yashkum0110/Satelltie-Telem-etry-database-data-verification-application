import pandas as pd
from fuzzywuzzy import fuzz
import re
import joblib

class DataMatcher:
    def __init__(self, threshold=80):
        self.threshold = threshold
        self.database_df = None
        self.reference_col = None
        
    def preprocess_text(self, text):
        """Normalize text for comparison"""
        if pd.isna(text):
            return ""
        text = str(text)
        text = text.lower().strip()
        text = re.sub(r'[^a-z0-9\s]', '', text)  # Remove special chars
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        return text
    
    def train(self, database_df, reference_col):
        """Load and prepare the database"""
        self.database_df = database_df.copy()
        self.reference_col = reference_col
        # Preprocess reference column
        self.database_df['processed_ref'] = self.database_df[reference_col].apply(self.preprocess_text)
        
    def find_match(self, query):
        """Find best match for a query string"""
        query_processed = self.preprocess_text(query)
        
        # Get all possible matches with scores
        matches = []
        for idx, row in self.database_df.iterrows():
            score = fuzz.token_sort_ratio(query_processed, row['processed_ref'])
            matches.append((score, idx))
        
        # Filter by threshold and get best match
        matches = [m for m in matches if m[0] >= self.threshold]
        if not matches:
            return None, 0
        
        # Get match with highest score
        best_match = max(matches, key=lambda x: x[0])
        return self.database_df.iloc[best_match[1]], best_match[0]
    
    def save(self, path):
        """Save trained model"""
        joblib.dump({
            'database_df': self.database_df,
            'reference_col': self.reference_col,
            'threshold': self.threshold
        }, path)
        
    @classmethod
    def load(cls, path):
        """Load trained model"""
        data = joblib.load(path)
        model = cls(data['threshold'])
        model.database_df = data['database_df']
        model.reference_col = data['reference_col']
        return model