from .wps_sleep import Sleep
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box

processes = [
    UltimateQuestion(),
    Sleep(),
    Box(),
]
