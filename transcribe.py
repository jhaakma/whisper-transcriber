import sys
import whisper
model = whisper.load_model('base')

# Check if a file path is provided as a command-line argument
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    result_path = file_path + ".txt"
else:
    print("Usage: transcribe.py <file_path>")

print(f"Transcribing {file_path}...")
result = model.transcribe(file_path, language = "zh")
print("Transcription complete.")
# Write the result to a file
with open(result_path, "w", encoding="utf-8") as file:
    file.write(result["text"])

print(f"Transcription saved to {result_path}")
