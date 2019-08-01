# Stubs for torch.distributions.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def broadcast_all(*values: Any): ...
def logits_to_probs(logits: Any, is_binary: bool = ...): ...
def clamp_probs(probs: Any): ...
def probs_to_logits(probs: Any, is_binary: bool = ...): ...

class lazy_property:
    wrapped: Any = ...
    def __init__(self, wrapped: Any) -> None: ...
    def __get__(self, instance: Any, obj_type: Optional[Any] = ...): ...