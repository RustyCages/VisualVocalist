import moviepy.editor as mp
import librosa
import numpy as np

def process_video(video_path):
    print(f"--- Startar analys av: {video_path} ---")
    
    # 1. Extrahera ljudet från filmen till en temporär fil
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')

    # 2. Ladda ljudet med Librosa (vårt ljud-bibliotek)
    y, sr = librosa.load(audio_path)
    
    # 3. Pitch Detection (hitta grundtonen)
    # pi = pitch, voiced_flag = är det en ton eller bara brus?
    pitches, voiced_flags, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C6'))

    # 4. Omvandla Hz till MIDI-noter och tidsstämplar
    extracted_data = []
    times = librosa.times_like(pitches)

    for i in range(len(pitches)):
        if voiced_flags[i]: # Om det faktiskt är en ton som spelas
            midi_note = librosa.hz_to_midi(pitches[i])
            extracted_data.append({
                "time": round(float(times[i]), 3),
                "pitch": int(round(midi_note))
            })

    print(f"Klar! Hittade {len(extracted_data)} datapunkter.")
    return extracted_data

# Kör scriptet (byt ut 'min_film.mp4' mot ditt filnamn)
# data = process_video("min_film.mp4")
# print(data[:10]) # Visa de första 10 träffarna