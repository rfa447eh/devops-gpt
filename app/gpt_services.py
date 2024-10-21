import os
from openai import OpenAI
from fastapi import HTTPException


def gpt_service_IaC(input:str, service:str,max_tokens:int, min_tokens:int):
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

        prompt = f"""
            Write a robust answer about {service},
            focusing on the latest update of {service} and based on this question:{input},
            minimun length of answer is {min_tokens} and maximum length is {max_tokens}

        """
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [{"type": "text", "text": prompt}],
                }
            ],
            model="gpt-4o-mini",
        )
        return chat_completion

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))