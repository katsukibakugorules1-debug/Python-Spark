from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np

# Load your audio file
wav = preprocess_wav(Path("Noah_master.wav"))

# Create encoder
encoder = VoiceEncoder()

# Generate embedding
embedding = encoder.embed_utterance(wav)

print("Embedding shape:", embedding.shape)
print("First 10 numbers:", embedding[:10])
