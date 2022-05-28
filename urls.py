from hypergen.hypergen import autourls
from {{ app_name }} import views

app_name = '{{ app_name }}'

# Automatically creates urlpatterns for all functions in views.py decorated with @liveview or
# @action.
urlpatterns = autourls(views, namespace="{{ app_name }}")
