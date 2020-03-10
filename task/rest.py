import inspect
from wq.db import rest
import task.models as models
from task.views import CustomViewSet

model_names = [m[0] for m in inspect.getmembers(models, inspect.isclass) if m[1].__module__ == 'task.models']

for model_name in model_names:
    rest.router.register_model(
        getattr(models, model_name),
        fields="__all__",
        viewset=CustomViewSet,
    )
