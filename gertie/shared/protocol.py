"""JSON-RPC Protocol Bridge for GERTIE System"""
import json
import uuid
from typing import Any, Dict, Optional

class JSONRPCMessage:
    """Standard JSON-RPC 2.0 message format"""
    
    @staticmethod
    def request(method: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        """Create JSON-RPC request"""
        msg = {
            "jsonrpc": "2.0",
            "method": method,
            "id": str(uuid.uuid4())
        }
        if params:
            msg["params"] = params
        return msg
    
    @staticmethod
    def response(request_id: str, result: Any) -> Dict:
        """Create JSON-RPC response"""
        return {
            "jsonrpc": "2.0",
            "result": result,
            "id": request_id
        }
    
    @staticmethod
    def error(request_id: str, code: int, message: str) -> Dict:
        """Create JSON-RPC error response"""
        return {
            "jsonrpc": "2.0",
            "error": {
                "code": code,
                "message": message
            },
            "id": request_id
        }
