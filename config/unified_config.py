from dataclasses import dataclass, field
from pathlib import Path
import json
import os

@dataclass
class UnifiedConfig:
    CONTROL_PORT: int = 5001
    VIDEO_PORT: int = 5002
    HEARTBEAT_PORT: int = 5003
    BASE_DIR: Path = field(default_factory=lambda: Path.home() / 'Desktop/camera_system_integrated_final')
    IMAGE_DIR: Path = field(default_factory=lambda: Path.home() / 'Desktop/gertie_images')
    
    @classmethod
    def load_with_fallback(cls):
        try:
            config_path = Path.home() / '.gertie/config/main.json'
            if config_path.exists():
                with open(config_path) as f:
                    return cls(**json.load(f))
        except:
            pass
        try:
            from shared.config import settings
            return cls.from_legacy(settings)
        except:
            return cls()
