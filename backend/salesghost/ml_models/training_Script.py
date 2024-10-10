import spacy
from spacy.util import minibatch, compounding
from spacy.training import Example
from .training_data import TRAIN_DATA

# Load a blank spaCy model
nlp = spacy.blank("en")

# Create a new NER pipeline
ner = nlp.add_pipe("ner")

# Add the new labels to the pipeline
for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

# Disable other pipes (if any)
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    
    for i in range(30):  # You can increase the number of iterations for better results
        losses = {}
        batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
        for batch in batches:
            for text, annotations in batch:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], losses=losses, drop=0.5, sgd=optimizer)
        print(f"Losses at iteration {i}: {losses}")

# Save the trained model
nlp.to_disk("ner_model")
