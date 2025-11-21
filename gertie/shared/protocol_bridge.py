"""Bridge between legacy string protocol and JSON-RPC"""
import json
from typing import Dict, Any, Optional
from gertie.shared.protocol import JSONRPCMessage

class ProtocolBridge:
    """Translates between legacy string commands and JSON-RPC"""
    
    @staticmethod
    def legacy_to_jsonrpc(legacy_command: str) -> Optional[Dict]:
        """Convert legacy string command to JSON-RPC format"""
        # Examples of legacy commands:
        # "SET_CAMERA_CROP_ENABLED_True"
        # "CAPTURE_IMAGE"
        # "GET_SETTINGS"
        
        if legacy_command.startswith("SET_CAMERA_CROP_ENABLED_"):
            enabled = legacy_command.split("_")[-1] == "True"
            return JSONRPCMessage.request("set_camera_crop", {"enabled": enabled})
        
        elif legacy_command == "CAPTURE_IMAGE":
            return JSONRPCMessage.request("capture_image")
        
        elif legacy_command == "GET_SETTINGS":
            return JSONRPCMessage.request("get_settings")
        
        elif legacy_command.startswith("SET_TRANSFORM_"):
            parts = legacy_command.split("_")
            if len(parts) >= 3:
                transform = parts[2].lower()
                value = "_".join(parts[3:])
                return JSONRPCMessage.request("set_transform", {
                    "type": transform,
                    "value": value
                })
        
        # Default: pass through as generic command
        return JSONRPCMessage.request("legacy_command", {"command": legacy_command})
    
    @staticmethod
    def jsonrpc_to_legacy(jsonrpc_msg: Dict) -> Optional[str]:
        """Convert JSON-RPC message to legacy string format"""
        if "method" not in jsonrpc_msg:
            return None
        
        method = jsonrpc_msg["method"]
        params = jsonrpc_msg.get("params", {})
        
        if method == "set_camera_crop":
            enabled = params.get("enabled", False)
            return f"SET_CAMERA_CROP_ENABLED_{enabled}"
        
        elif method == "capture_image":
            return "CAPTURE_IMAGE"
        
        elif method == "get_settings":
            return "GET_SETTINGS"
        
        elif method == "set_transform":
            transform_type = params.get("type", "")
            value = params.get("value", "")
            return f"SET_TRANSFORM_{transform_type.upper()}_{value}"
        
        elif method == "legacy_command":
            return params.get("command", "")
        
        return None
