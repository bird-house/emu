from .wps_sleep import Sleep
from .wps_nap import Nap
from .wps_ultimate_question import UltimateQuestion
from .wps_bbox import Box
from .wps_say_hello import SayHello
from .wps_dummy import Dummy
from .wps_wordcounter import WordCounter
from .wps_chomsky import Chomsky
from .wps_inout import InOut
from .wps_binaryoperator import BinaryOperator
from .wps_error import ShowError
from .wps_multiple_outputs import MultipleOutputs
from .wps_esgf import ESGFDemo
from .wps_output_formats import OutputFormats
from .wps_poly_centroid import PolyCentroid
from .wps_ncmeta import NCMeta
from .wps_esgf_subset import CDATSubset

processes = [
    UltimateQuestion(),
    Sleep(),
    Nap(),
    Box(),
    SayHello(),
    Dummy(),
    WordCounter(),
    Chomsky(),
    InOut(),
    BinaryOperator(),
    ShowError(),
    MultipleOutputs(),
    ESGFDemo(),
    OutputFormats(),
    PolyCentroid(),
    NCMeta(),
    CDATSubset(),
]
