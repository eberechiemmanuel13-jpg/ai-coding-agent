from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import read_file, write_file, run_code

llm = ChatOllama(model="llama3.2", temperature=0)

tools = [read_file, write_file, run_code]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a FREE AI Coding Agent. You can read, write files and run code. Always test your code with run_code tool. Fix errors automatically."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

while True:
    q = input("\nYou: ")
    if q == 'exit': break
    result = executor.invoke({"input": q})
    print(result['output'])