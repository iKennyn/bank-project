import functools
import logging
from typing import Optional

from pydantic import BaseModel

from main.api.configs.config import Config

logger = logging.getLogger(__name__)


def log_request_response(method_name: str):
    """Декоратор для логирования запроса и ответа (только logging)."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, model: Optional[BaseModel] = None, *args, **kwargs):
            url = f"{Config.fetch('backendUrl')}{self.endpoint.value.url}"

            # 1. Логируем запрос
            logger.info(f"→ {method_name} {url}")
            if model:
                logger.info(f"→ Request body: {model.model_dump_json()}")

            # 2. Выполняем запрос
            response = func(self, model, *args, **kwargs)

            # 3. Логируем ответ
            logger.info(f"← Status: {response.status_code}")
            logger.info(f"← Response body: {response.text}")

            return response
        return wrapper
    return decorator