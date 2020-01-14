from pywps import Process
from pywps import LiteralInput, LiteralOutput
from pywps.inout.literaltypes import AllowedValue
from pywps.inout.literaltypes import AnyValue
from pywps.inout.literaltypes import ValuesReference
# from pywps import BoundingBoxInput
from pywps import BoundingBoxOutput
from pywps import ComplexInput, ComplexOutput
from pywps import Format, FORMATS
from pywps.validator.mode import MODE
from pywps.app.Common import Metadata


import logging
LOGGER = logging.getLogger("PYWPS")


class InOut(Process):
    """
    This process defines several types of literal type of in- and outputs.

    TODO: add literal input with value range[(0,100)] ... see pywps doc
    """

    def __init__(self):
        inputs = [
            LiteralInput('string', 'String', data_type='string',
                         abstract='Enter a simple string.',
                         default="This is just a string",
                         mode=MODE.SIMPLE),
            LiteralInput('int', 'Integer', data_type='integer',
                         abstract='Choose an integer number from allowed values.',
                         default="7",
                         allowed_values=[1, 2, 3, 5, 7, 11]),
            LiteralInput('float', 'Float', data_type='float',
                         abstract='Enter a float number.',
                         default="3.14",
                         min_occurs=0,
                         max_occurs=5),
            # TODO: boolean default is not displayed in phoenix
            LiteralInput('boolean', 'Boolean', data_type='boolean',
                         abstract='Make your choice :)',
                         default='1'),
            LiteralInput('angle', 'Angle', data_type='angle',
                         abstract='Enter an angle [0, 360] :)',
                         default='90'),
            LiteralInput('time', 'Time', data_type='time',
                         abstract='Enter a time like 12:00:00',
                         default='12:00:00'),
            LiteralInput('date', 'Date', data_type='date',
                         abstract='Enter a date like 2012-05-01',
                         default='2012-05-01'),
            LiteralInput('datetime', 'Datetime', data_type='dateTime',
                         abstract='Enter a datetime like 2016-09-02T12:00:00Z',
                         default='2016-09-02T12:00:00Z'),
            LiteralInput('string_choice', 'String Choice', data_type='string',
                         abstract='Choose one item form list.',
                         allowed_values=['rock', 'paper', 'scissor'],
                         default='scissor'),
            LiteralInput('string_multiple_choice', 'String Multiple Choice',
                         abstract='Choose one or two items from list.',
                         data_type='string',
                         allowed_values=['sitting duck', 'flying goose',
                                         'happy pinguin', 'gentle albatros'],
                         min_occurs=0, max_occurs=2,
                         default='gentle albatros'),
            LiteralInput('int_range', 'Integer Range',
                         abstract='Choose number from range: 1-10 (step 1), 100-200 (step 10)',
                         metadata=[
                            Metadata('PyWPS Docs', 'https://pywps.readthedocs.io/en/master/api.html#pywps.inout.literaltypes.AllowedValue'),  # noqa
                            Metadata('AllowedValue Example', 'http://docs.opengeospatial.org/is/14-065/14-065.html#98'),  # noqa
                            ],
                         data_type='integer',
                         default='1',
                         allowed_values=[
                             AllowedValue(minval=1, maxval=10),
                             AllowedValue(minval=100, maxval=200, spacing=10)
                         ],
                         mode=MODE.SIMPLE,),
            LiteralInput('any_value', 'Any Value',
                         abstract='Enter any value.',
                         metadata=[
                            Metadata('PyWPS Docs', 'https://pywps.readthedocs.io/en/master/api.html#pywps.inout.literaltypes.AnyValue'),  # noqa
                         ],
                         allowed_values=AnyValue(),
                         default='any value',
                         mode=MODE.SIMPLE,),
            LiteralInput('ref_value', 'Referenced Value',
                         abstract='Choose a referenced value',
                         metadata=[
                            Metadata('PyWPS Docs', 'https://pywps.readthedocs.io/en/master/_modules/pywps/inout/literaltypes.html'),  # noqa
                         ],
                         data_type='string',
                         allowed_values=ValuesReference(
                             reference="https://en.wikipedia.org/w/api.php?action=opensearch&search=scotland&format=json"),  # noqa
                         default='Scotland',
                         mode=MODE.SIMPLE,),
            # TODO: bbox is not supported yet by owslib
            # BoundingBoxInput('bbox', 'Bounding Box',
            #                  abstract='Bounding Box with EPSG:4326 and EPSG:3035.',
            #                  crss=['epsg:4326', 'epsg:3035'],
            #                  min_occurs=0),
            ComplexInput('text', 'Text',
                         abstract='Enter a URL pointing to a text document (optional)',
                         metadata=[Metadata('Info')],
                         min_occurs=0,
                         supported_formats=[Format('text/plain')]),
            ComplexInput('dataset', 'Dataset',
                         abstract="Enter a URL pointing to a NetCDF file (optional)",
                         metadata=[
                             Metadata('NetCDF Format', 'https://en.wikipedia.org/wiki/NetCDF',
                                      role='http://www.opengis.net/spec/wps/2.0/def/process/description/documentation')
                         ],
                         min_occurs=0,
                         supported_formats=[FORMATS.NETCDF]),
        ]
        outputs = [
            LiteralOutput('string', 'String', data_type='string'),
            LiteralOutput('int', 'Integer', data_type='integer'),
            LiteralOutput('float', 'Float', data_type='float'),
            LiteralOutput('boolean', 'Boolean', data_type='boolean'),
            LiteralOutput('angle', 'Angle', data_type='angle'),
            LiteralOutput('time', 'Time', data_type='time'),
            LiteralOutput('date', 'Date', data_type='date'),
            LiteralOutput('datetime', 'DateTime', data_type='dateTime'),
            LiteralOutput('string_choice', 'String Choice',
                          data_type='string'),
            LiteralOutput('string_multiple_choice', 'String Multiple Choice',
                          data_type='string'),
            LiteralOutput('int_range', 'Integer Range',
                          data_type='integer'),
            LiteralOutput('any_value', 'Any Value',
                          data_type='string'),
            LiteralOutput('ref_value', 'Referenced Value',
                          data_type='string'),
            ComplexOutput('text', 'Text',
                          abstract='Copy of input text file.',
                          as_reference=False,
                          supported_formats=[FORMATS.TEXT, ]),
            ComplexOutput('dataset', 'Dataset',
                          abstract='Copy of input netcdf file.',
                          as_reference=True,
                          supported_formats=[FORMATS.NETCDF,
                                             FORMATS.TEXT]),
            BoundingBoxOutput('bbox', 'Bounding Box',
                              crss=['epsg:4326']),
        ]

        super(InOut, self).__init__(
            self._handler,
            identifier="inout",
            title="In and Out",
            version="1.0",
            abstract="Testing all WPS input and output parameters.",
            # profile=['birdhouse'],
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/',
                         role='http://www.opengis.net/spec/wps/2.0/def/process/description/documentation')],
            inputs=inputs,
            outputs=outputs,
            status_supported=True,
            store_supported=True)

    @staticmethod
    def _handler(request, response):
        response.update_status('PyWPS Process started.', 0)

        response.outputs['string'].data = request.inputs['string'][0].data
        response.outputs['int'].data = request.inputs['int'][0].data
        response.outputs['float'].data = sum([f.data for f in request.inputs['float']])
        response.outputs['boolean'].data = request.inputs['boolean'][0].data
        response.outputs['angle'].data = request.inputs['angle'][0].data
        response.outputs['time'].data = request.inputs['time'][0].data
        response.outputs['date'].data = request.inputs['date'][0].data
        response.outputs['datetime'].data = request.inputs['datetime'][0].data
        response.outputs['string_choice'].data = \
            request.inputs['string_choice'][0].data
        if 'string_multiple_choice' in request.inputs:
            response.outputs['string_multiple_choice'].data = ', '.join(
                [inpt.data for inpt in request.inputs['string_multiple_choice']])
        else:
            response.outputs['string_multiple_choice'].data = 'no value'
        response.outputs['int_range'].data = \
            request.inputs['int_range'][0].data
        response.outputs['any_value'].data = \
            request.inputs['any_value'][0].data
        response.outputs['ref_value'].data = \
            request.inputs['ref_value'][0].data
        # TODO: bbox is not working
        # response.outputs['bbox'].data = request.inputs['bbox'][0].data
        # TODO: how to copy file?
        response.outputs['text'].data_format = FORMATS.TEXT
        if 'text' in request.inputs:
            response.outputs['text'].file = request.inputs['text'][0].file
        else:
            response.outputs['text'].data = "request didn't have a text file."

        if 'dataset' in request.inputs:
            response.outputs['dataset'].data_format = FORMATS.NETCDF
            response.outputs['dataset'].file = request.inputs['dataset'][0].file
        else:
            response.outputs['dataset'].data_format = FORMATS.TEXT
            response.outputs['dataset'].data = "request didn't have a netcdf file."
        response.outputs['bbox'].data = [0, 0, 10, 10]

        response.update_status('PyWPS Process completed.', 100)
        return response
