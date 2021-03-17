import json
from locust import HttpUser, between, task

from tests.storm.common import execute_async


class EmuUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 10)

    @task(4)
    def capabilities(self):
        query = "/wps?service=WPS&request=GetCapabilities"

        with self.client.get(
            query, catch_response=True, name="capabilities"
        ) as response:
            if "<ows:Title>Emu</ows:Title>" not in response.text:
                response.failure("Capabilities does not match expected XML")

    @task(2)
    def describe_process_subset(self):
        query = (
            "/wps?service=WPS&version=1.0.0&request=DescribeProcess&identifier=hello"
        )
        with self.client.get(
            query, catch_response=True, name="describe_process"
        ) as response:
            if "<ows:Identifier>hello</ows:Identifier>" not in response.text:
                response.failure(
                    "Process description for *hello* does not match expected XML"
                )

    @task
    def execute_async_hello(self):
        # short running async, post
        execute_async(
            client=self.client,
            name="execute_async_hello",
            identifier="hello",
            inputs=[
                ("name", "Stranger"),
            ],
        )

    @task
    def execute_async_sleep(self):
        # long running async, post
        execute_async(
            client=self.client,
            name="execute_async_sleep",
            identifier="sleep",
            inputs=[
                ("delay", "5"),
            ],
        )

    @task
    def execute_sync_nap(self):
        # short running sync, get
        query = "/wps?service=WPS&version=1.0.0&request=Execute&identifier=nap&DataInputs=delay=1"

        with self.client.get(
            query, catch_response=True, name="execute_sync_nap"
        ) as response:
            if "ProcessSucceeded" not in response.text:
                response.failure("Process *nap* failed")
