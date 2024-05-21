# run.py
from hamilton import driver
from _hamilton.driver import my_dataflow  # <- module containing functions to define dataflow

# variable `dr` is of type `driver.Driver`
# it is created by a `driver.Builder` object
dr = driver.Builder().with_modules(my_dataflow).build()

# have to install graphviz to visualize the dataflow
# reference: https://stackoverflow.com/questions/35064304/runtimeerror-make-sure-the-graphviz-executables-are-on-your-systems-path-aft
dr.visualize_execution(["C"], "execute_c.png")
results = dr.execute(["C"])

print(results["C"])  # access results dictionary
