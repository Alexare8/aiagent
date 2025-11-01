import os, sys, types
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions.get_files_info import schema_get_files_info

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    if type(sys.argv[1]) != str:
        sys.exit("invalid arguments")
    verbose = "--verbose" in sys.argv[1:]
    user_prompt = sys.argv[1]

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    available_functions = types.Tool(function_declarations=[schema_get_files_info,])
    config = genai.types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions])

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=config)

    if verbose:
        print(f"User prompt: {user_prompt}")
    print(response.text)
    if len(response.function_calls) > 0:
        for call in response.function_calls:
            print(f"Calling function: {call.name}({call.args})")
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
