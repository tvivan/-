
import os
from noteengine import note_engine
from llama_index.core.tools import QueryEngineTool,ToolMetadata
from llama_index.core.agent import ReActAgent
from pdfread import cyr_engine
from llama_index.llms.openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
os.environ["OPENAI_API_KEY"] = "API KEY"
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=cyr_engine,
        metadata=ToolMetadata(
            name = "cyr_data",
            description="this gives detailed information about Sustainable Development Goals"
        )
    )
]

agent = ReActAgent.from_tools(tools,llm=client,verbose=True,context=context)
while (prompt:= input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
