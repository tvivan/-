from llama_index.core import PromptTemplate

instruction_str = """\
    1. Convert the query to executable Python code for analytic job.
    2. The final line of code should be a Python expression that can be called with the 'eval()' function.
    3. The code should represent a solution for a query.
    4. PRINT ONLY EXPRESSION.
    5. Do not quote the expression.
    6. Type answer in Russian exept for code"""
new_prompt = PromptTemplate(
    f"""\
    You are a calculation analytic bot.
    You are working with table data in PDF format
    Follow this instructions:{instruction_str}
    Query: {query_str}
    Expression: """
)
context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about tables provided in PDF. """