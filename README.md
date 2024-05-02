# language-analytics-assignment1
First assignment for language analytics course.

## Setup:

The corpus needs to be in the `data/` folder, where the USEcorpus folder should contain all the subcorpora in its subfolders:

Sort of like this:

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

The script needs tqdm, pandas and spacy:

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
