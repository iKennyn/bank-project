from src.main.api.fixtures.api_fixture import *
from src.main.api.fixtures.object_fixture import *

import logging
# логирование добавил чисто для тестов, на практике так оставлять не нужно
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),  # вывод в консоль
    ]
)
