# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="EleutherAI/llemma_7b")
res = pipe("Why is 6 afraid of 7?")
print(res)
