import os, sys, json
import openai


openai.api_key = os.environ['OPENAI_API_KEY']


def response(ask, type="c", directions=None):
    if type == "c":
        return openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.0,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
    else:
        return openai.Edit.create(
            model="text-davinci-edit-001", 
            input=ask, 
            instruction=directions,
            n=10
        )


if __name__ == "__main__":
    print(
        "Provide completion prompts to write, explain, edit, or compare. Works with text or code. See https://github.com/openai/openai-cookbook/#examples-organized-by-capability for examples.\n\n"
    )
    

    while True:
        try:
            type = input("Completion or edit? (c|e)")
            while True:
                if type == "c":
                    print("Completion: \n")
                else:
                    print("Edit: \n")
                    directions = input("Instruction: ")

                if type == "c":
                    print("Enter prompt:\n")
                else:
                    print("Enter text to edit:\n")
                lines = []
                test = False

                while test == False:
                    lines.append(input())
                    if "eof" in "\n".join(lines).lower():
                        test == True
                        break
                user_input = "\n".join(lines)
                user_input = user_input.lower().replace('eof', '')
                if type == "c":
                    r = json.loads(str(response(user_input, type="c")))
                else:
                    r = json.loads(
                        str(response(user_input, type="c", directions=directions))
                    )
                print(r["choices"][0]["text"], "\n\n")
                break
        except KeyboardInterrupt:
            break