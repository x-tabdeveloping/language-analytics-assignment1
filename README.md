# language-analytics-assignment1
First assignment for language analytics course.

The assignment is about extracting POS tag and NER data from the Uppsala Student English Corpus using the SpaCy NLP framework.
The data can be downloaded from the [official website](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

## Setup:

The corpus needs to be in the `data/` folder, where the USEcorpus folder should contain all the subcorpora in its subfolders:

The file hierarchy should follow this structure:
```
- data
  - USEcorpus
    - a1
      - 1011.a1.txt
        ...
      - 5031.a1.txt
    ...
    - c1
```

Install the requirements of the scripts:

```bash
pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python3 src/run_analysis.py
```

This will produce a bunch of `.csv` files in the `output/` folder for each subcorpus.

```
- output
  - a1.csv
  ...
  - c1.csv
```

Every row of the tables contains result for one file in the corpus with relative frequencies of UPOS tags per 10000 words and number of unique named entities per category.

> Additionally the script will produce a csv file with the CO2 emissions of the substasks in the code (`emissions/`).
> This is necessary for Assignment 5, and is not directly relevant to this assignment.

> Note: The `emissions/emissions.csv` file should be ignored. This is due to the fact, that codecarbon can't track process and task emissions at the same time.
