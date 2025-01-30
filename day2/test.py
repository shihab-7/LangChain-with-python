from decouple import config
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient

SECRECT_KEY = config("HUGGINGFACE_API_KEY")
# print(SECRECT_KEY)
text = input("Enter something...")

template = "<s>[INST] write briefly on </s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)
formatted_template =prompt_template.format(question=text)

# print(formatted_template)
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
llm = InferenceClient(model=repo_id, token=SECRECT_KEY)
response = llm.text_generation(formatted_template)
for s in response:
    print(s,end="")

