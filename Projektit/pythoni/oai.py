import openai

openai.api_key = "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"

def useAI(PROMPT, MaxToken=50, outputs=3):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=PROMPT,
        max_tokens=MaxToken,
        n=outputs
    )
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output
