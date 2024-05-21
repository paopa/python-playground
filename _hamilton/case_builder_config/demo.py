from hamilton import driver
from _hamilton.case_builder_config import my_dataflow

dr = (
    driver.Builder()
    .with_modules(my_dataflow)
    .with_config(dict(version="default"))
    .build()
)

result = dr.execute(["B"])

print(result)
