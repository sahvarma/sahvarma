"""Configuration management for AmeriLife project"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Base configuration class"""

    # API Configuration
    API_ENDPOINT = os.getenv(
        "API_ENDPOINT",
        "https://api.designer-na.cloud.varicent.com/api/v1/customtables/stgContractDetailsAPI/inputforms/0/data/rows"
    )
    AUTH_TOKEN = os.getenv("AUTH_TOKEN", "")
    API_MODEL = os.getenv("API_MODEL", "AmeriLifeDev")
    CONTENT_TYPE = "application/json"
    
    # Request Configuration
    TIMEOUT = int(os.getenv("TIMEOUT", 60))
    BATCH_SIZE = int(os.getenv("BATCH_SIZE", 2000))
    
    # Data Configuration
    CSV_PATH = os.getenv("CSV_PATH", "data/stgContractDetails.csv")
    DEFAULT_RECORDS = int(os.getenv("DEFAULT_RECORDS", 100000))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    @staticmethod
    def get_headers():
        """Get API request headers"""
        return {
            "Content-Type": Config.CONTENT_TYPE,
            "Authorization": f"Bearer {Config.AUTH_TOKEN}",
            "Model": Config.API_MODEL,
        }


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    LOG_LEVEL = "WARNING"
