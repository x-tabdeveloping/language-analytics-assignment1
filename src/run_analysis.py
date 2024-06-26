import re
from collections import Counter
from glob import glob
from pathlib import Path

import pandas as pd
import spacy
from codecarbon import EmissionsTracker
from spacy.tokens import Doc
from tqdm import tqdm


def remove_carets(text: str) -> str:
    pattern = re.compile("<.*?>")
    return re.sub(pattern, "", text)


def postag_freqs(doc: Doc) -> dict:
    postags = [token.pos_ for token in doc]
    counts = Counter(postags)
    total = counts.total()
    return {f"RelFreq {tag}": (count / total) * 10_000 for tag, count in counts.items()}


def unique_named_entities(doc: Doc) -> dict:
    people = [ent.text.lower() for ent in doc.ents if ent.label_ == "PER"]
    locations = [ent.text.lower() for ent in doc.ents if ent.label_ == "LOC"]
    organizations = [ent.text.lower() for ent in doc.ents if ent.label_ == "ORG"]
    return {
        "No. Unique PER": len(set(people)),
        "No. Unique LOC": len(set(locations)),
        "No. Unique ORG": len(set(organizations)),
    }


def main():
    out_dir = Path("output/")
    out_dir.mkdir(exist_ok=True)
    emissions_dir = Path("emissions/")
    emissions_dir.mkdir(exist_ok=True)
    with EmissionsTracker(
        project_name="pos_ner_spacy",
        save_to_file=True,
        output_file="emissions.csv",
        output_dir=emissions_dir,
    ) as tracker:
        subdirs = glob("data/USEcorpus/*")
        subdirs = map(Path, subdirs)
        subdirs = [dir for dir in subdirs if dir.is_dir()]

        tracker.start_task("load_model")
        nlp = spacy.load("en_core_web_sm")
        tracker.stop_task()
        tracker.start_task("processing")
        for subdir in tqdm(subdirs, desc="Going through subdirectories."):
            dir_name = subdir.stem
            records = []
            for file in subdir.glob("*.txt"):
                with open(file, encoding="ISO-8859-1") as in_file:
                    text = in_file.read()
                doc = nlp(text)
                entry = {
                    "Filename": file.name,
                    **postag_freqs(doc),
                    **unique_named_entities(doc),
                }
                records.append(entry)
            dir_table = pd.DataFrame.from_records(records)
            dir_table.to_csv(out_dir.joinpath(f"{dir_name}.csv"))
        tracker.stop_task()


if __name__ == "__main__":
    main()
