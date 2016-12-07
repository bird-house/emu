from pywps import Process, LiteralInput, LiteralOutput
from pywps.app.Common import Metadata

import logging
logger = logging.getLogger("PYWPS")


class BinaryOperator(Process):
    def __init__(self):
        inputs = [
            LiteralInput('inputa', 'Input 1', data_type='float',
                         abstract='Enter Input 1',
                         default="2.0"),
            LiteralInput('inputb', 'Input 2', data_type='float',
                         abstract='Enter Input 2',
                         default="3.0"),
            LiteralInput('operator', 'Operator', data_type='string',
                         abstract='Choose a binary Operator',
                         default='add',
                         allowed_values=['add', 'substract', 'divide', 'multipy'])]
        outputs = [
            LiteralOutput('output', 'Binary operator result',
                          data_type='float')]

        super(BinaryOperator, self).__init__(
            self._handler,
            identifier='binaryoperatorfornumbers',
            title='Binary Operator for Numbers',
            abstract='Performs operation on two numbers and returns the answer.\
                This example process is taken from Climate4Impact.',
            metadata=[
                Metadata('Birdhouse', 'http://bird-house.github.io/'),
                Metadata('User Guide', 'http://emu.readthedocs.io/en/latest/')],
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        logger.info("run binary_operator")
        operator = request.inputs['operator'][0].data
        input_a = request.inputs['inputa'][0].data
        input_b = request.inputs['inputb'][0].data

        if operator == 'substract':
            response.outputs['output'].data = input_a - input_b
        elif operator == 'multiply':
            response.outputs['output'].data = input_a * input_b
        elif operator == 'divide':
            response.outputs['output'].data = input_a / input_b
        else:
            response.outputs['output'].data = input_a + input_b
        return response
