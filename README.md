# drest_test

## How to run
The code is run in a 'python:3.6-slim' Docker container. You can test the output with _make_ :
```
make test
```
This will run the pipeline and output the resulting DataFrame.
If you want to clear Docker afterwards I have included:
```
make prune
```

## Componants
I have split the repo into two sections, data and src. 
_data_ is where the json is stored. There was a typo in the 'email' key of the data I recieved. I wasn't sure if it was there as part of the test or not and decided to correct it to get the pipeline working instead of writing a debugging code.
_src_ is where I put the ingestion scripts and the _DataFrameFromDict_ class, this class creates a temporary dataframe with the normalized json data and then deletes it once you have extracted the relevant columns.

## Conclusion
I wasn't sure which data would be considered important so chose user traits that I figured would be useful to the business. I enjoyed this simple challenge and working out how to create a simple and clean pipeline.
