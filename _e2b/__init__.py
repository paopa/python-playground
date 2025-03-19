from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv

load_dotenv()

with Sandbox() as sandbox:
    sandbox.run_code("x = 1")
    sandbox.run_code("x+=1")
    execution = sandbox.run_code("x")
    breakpoint()
    print(execution.text)  # outputs 2
