from .wps_sleep import Sleep
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box
from .wps_hello import Hello
from .wps_dummy import Dummy
from .wps_wordcounter import WordCounter
from .wps_chomsky import Chomsky
from .wps_inout import InOut

processes = [
    UltimateQuestion(),
    Sleep(),
    Box(),
    Hello(),
    Dummy(),
    WordCounter(),
    Chomsky(),
    InOut(),
]
