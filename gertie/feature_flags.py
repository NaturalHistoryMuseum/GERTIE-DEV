"""Feature flag management for parallel implementation"""
import os

class FeatureFlags:
    USE_NEW_GERTIE = os.environ.get('USE_NEW_GERTIE', 'false').lower() == 'true'
    USE_UNIFIED_CONFIG = os.environ.get('USE_UNIFIED_CONFIG', 'false').lower() == 'true'
    USE_JSONRPC = os.environ.get('USE_JSONRPC', 'false').lower() == 'true'
    USE_ANSIBLE = os.environ.get('USE_ANSIBLE', 'false').lower() == 'true'
    USE_WEBSOCKETS = os.environ.get('USE_WEBSOCKETS', 'false').lower() == 'true'
    
    @classmethod
    def status(cls):
        return {
            'USE_NEW_GERTIE': cls.USE_NEW_GERTIE,
            'USE_UNIFIED_CONFIG': cls.USE_UNIFIED_CONFIG,
            'USE_JSONRPC': cls.USE_JSONRPC,
            'USE_ANSIBLE': cls.USE_ANSIBLE,
            'USE_WEBSOCKETS': cls.USE_WEBSOCKETS
        }
