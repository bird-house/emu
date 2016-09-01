from .wps_sleep import Sleep
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box
from .wps_helloworld import HelloWorld
from .wps_dummy import Dummy
from .wps_wordcounter import WordCounter
from .wps_chomsky import Chomsky

processes = [
    UltimateQuestion(),
    Sleep(),
    Box(),
    HelloWorld(),
    Dummy(),
    WordCounter(),
    Chomsky(),
]
