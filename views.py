from hypergen.core import *
from hypergen.core import callback as cb
from hypergen.contrib import hypergen_view, hypergen_callback, NO_PERM_REQUIRED, base_template

HYPER = dict(perm=NO_PERM_REQUIRED, base_template=base_template(title="Hello {{ app_name }}"))

@hypergen_view(**HYPER)
def counter(request):
    template(0)

@hypergen_callback(**HYPER)
def increment(request, n):
    template(n + 1)

def template(n):
    label("Current value: ")
    input_(id_="n", type_="number", value=n)
    button("Increment", id_="increment", onclick=cb(increment, n))
