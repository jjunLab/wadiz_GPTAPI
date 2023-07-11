# Langchain 패키지들
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI

script = ''' 텍스트 입력'''

# 언어모델 설정
llm = ChatOpenAI(temperature=0,
        openai_api_key="OpenAI API",
        max_tokens=4000,
        model_name="gpt-3.5-turbo",
        request_timeout=120
    )
# 프롬프트 설정
prompt = PromptTemplate(
    template="""Summarize the youtube video whose transcript is provided within backticks \
    ```{text}```
    """, input_variables=["text"]
)
combine_prompt = PromptTemplate(
    template="""Combine all the youtube video transcripts  provided within backticks \
    ```{text}```
    Provide a concise summary between 8 to 10 sentences.
    """, input_variables=["text"]
)
# LangChain을 활용하여 긴 글 요약하기
# 글 쪼개기
text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=0)
texts = text_splitter.create_documents([script])
# 요약하기
chain = load_summarize_chain(llm, chain_type="map_reduce", verbose=False,
                            map_prompt=prompt, combine_prompt=combine_prompt)
summerize = chain.run(texts)
# 최종 출력
print(summerize)