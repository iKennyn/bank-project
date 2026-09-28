from typing import List, Any

from main.api.steps.admin_steps import AdminSteps

# для инициализации и отдает все шаги (степы)
class ApiManager:
    def __init__(self, created_obj: List[Any]):
        self.admin_steps = AdminSteps(created_obj)