# Stubs for thinc.neural._classes.embed (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ...check import is_int
from ...describe import Dimension, Gradient, Synapses, Weights
from .._lsuv import do_lsuv
from ..ops import CupyOps
from ..util import copy_array
from .model import Model
from typing import Any, Optional

def LSUVinit(model: Any, X: Any, y: Optional[Any] = ...): ...

class Embed(Model):
    name: str = ...
    is_static: Any = ...
    column: Any = ...
    nO: Any = ...
    nM: Any = ...
    nV: Any = ...
    def __init__(self, nO: Any, nM: Optional[Any] = ..., nV: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def predict(self, ids: Any): ...
    def begin_update(self, ids: Any, drop: float = ...): ...
    def use_params(self, params: Any) -> None: ...