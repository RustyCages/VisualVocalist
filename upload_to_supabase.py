import os
from supabase import create_client, Client
from extract_pitch import process_video # Vi importerar funktionen från förra steget

# Dina Supabase-uppgifter (Hämta från Dashboard)
url: str = "https://pqfrzamdhdicefgbwruo.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBxZnJ6YW1kaGRpY2VmZ2J3cnVvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQyNjc1NzgsImV4cCI6MjA4OTg0MzU3OH0.b3nM0icWc0ViSjJ3pZk-ajE7l0BK8mE803E1TSauqtc"
supabase: Client = create_client(url, key)

def upload_stamma(video_file, title, part):
    # 1. Kör analysen
    raw_data = process_video(video_file)
    
    # 2. Skicka till Supabase
    data, count = supabase.table("stammor").insert({
        "song_title": title,
        "voice_part": part,
        "pitch_data": raw_data
    }).execute()
    
    print(f"✅ Uppladdning klar för {title} ({part})!")

# TESTKÖRNING:
# upload_stamma("sopran_stamma.mp4", "Härlig är jorden", "Sopran")