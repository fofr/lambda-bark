import os
from datetime import datetime
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav

def read_prompts(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    prompts = content.split('---')
    return [prompt.strip() for prompt in prompts if prompt.strip()]

def process_and_save(prompt, output_dir):
    audio_array = generate_audio(prompt)
    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = now + '_' + prompt.strip()[:10].replace(' ', '_') + '.wav'
    file_path = os.path.join(output_dir, file_name)
    write_wav(file_path, SAMPLE_RATE, audio_array)

# download and load all models
preload_models()

# read prompts from text file
prompt_file_path = 'prompts.txt'
output_dir = 'generated_audio'
os.makedirs(output_dir, exist_ok=True)
prompts = read_prompts(prompt_file_path)

# process each prompt and save the output
for prompt in prompts:
    process_and_save(prompt, output_dir)
