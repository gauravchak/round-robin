"""rankable item definition"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Item:
    """rankable item"""

    id: str  # pylint: disable=invalid-name
    cg1_feature: Optional[float]
    cg2_feature: Optional[float]
