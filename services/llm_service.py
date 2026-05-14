import os
import httpx
from dotenv import load_dotenv

load_dotenv()

async def call_llm(prompt: str) -> str:
    """
    Call the LLM with the formatted prompt and return the response.
    """
    url = os.getenv("LLM_URL")
    async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
        response = await client.post(url,
                                     json={"prompt": prompt}
                                    )

        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"]