# async_request.py
import aiohttp
import asyncio

async def fetch_data(url: str) -> str:
    """
    Sends a GET request to the specified URL asynchronously and returns the response as text.
    
    Args:
        url (str): The URL to send the request to.
        
    Returns:
        str: The response text from the URL.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an error for bad HTTP status codes
            return await response.text()

if __name__ == "__main__":
    url = "https://example.com"
    response_text = asyncio.run(fetch_data(url))
    print(response_text)
