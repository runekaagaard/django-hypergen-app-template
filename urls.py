from hypergen.contrib import hypergen_urls
from {{ app_name }} import views

app_name = '{{ app_name }}'

# Automatically creates urlpatterns for all functions in views.py decorated with @hypergen_view or
# @hypergen_callback.
urlpatterns = hypergen_urls(views, namespace="{{ app_name }}")
