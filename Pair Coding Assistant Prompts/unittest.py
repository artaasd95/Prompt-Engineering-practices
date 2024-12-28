# test_async_request.py
import pytest
import aiohttp
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
from async_request import fetch_data

class TestFetchData(AioHTTPTestCase):
    async def get_application(self):
        from aiohttp import web

        async def mock_handler(request):
            return web.Response(text="Mock response data")

        app = web.Application()
        app.router.add_get('/test', mock_handler)
        return app

    @unittest_run_loop
    async def test_fetch_data_success(self):
        url = f"http://localhost:{self.server.port}/test"
        response_text = await fetch_data(url)
        assert response_text == "Mock response data"

    @unittest_run_loop
    async def test_fetch_data_404(self):
        url = f"http://localhost:{self.server.port}/nonexistent"
        with pytest.raises(aiohttp.ClientResponseError):
            await fetch_data(url)

# To run the tests, execute the following command in the terminal:
# pytest test_async_request.py
