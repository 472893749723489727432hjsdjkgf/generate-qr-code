from server.src.db import TestSendData,TestCheckDb
import pytest

@pytest.mark.asyncio
async def test_TestCheckDb():
    await TestSendData("test","https://google.com")
    assert await TestCheckDb("test") == "https://google.com"


