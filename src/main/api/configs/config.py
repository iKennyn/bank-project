from pathlib import Path
from typing import Any


class Config:
    _isinstance = None # хранит единственный экземпляр
    _dictionary = {} # хранит конфигурацию (ключ-значение) в словаре
# реализуется синглтон, если конфиг не создан то создается новый
    def __new__(cls):
        if cls._isinstance is None:
            cls._isinstance = super(Config, cls).__new__(cls)

            config_path = Path(__file__).parents[4] / "resources" / "urls.properties"

            if not config_path.exists():
                raise FileNotFoundError(f"Config path not found: {config_path}")

            with open(config_path, "r") as file:
                for line in file:
                    if "=" in line:
                        key, value = line.split("=")
                        cls._dictionary[key] = value.strip()
        return cls._isinstance


# из словаря урлов мы вытаскиваем значение по ключу
    @staticmethod
    def fetch(key: str, default_value: Any = None) -> Any:
        return Config()._dictionary.get(key, default_value)