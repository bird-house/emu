from .wps_sleep import Sleep
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box
from .wps_helloworld import HelloWorld
from .wps_dummyprocess import Dummy

processes = [
    UltimateQuestion(),
    Sleep(),
    Box(),
    HelloWorld(),
    Dummy(),
]
