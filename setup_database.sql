-- 1. Skapa tabellen för stämmor
CREATE TABLE IF NOT EXISTS stammor (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  song_title TEXT NOT NULL,
  voice_part TEXT NOT NULL,
  pitch_data JSONB NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, now()) NOT NULL
);

-- 2. Aktivera säkerhet (RLS)
ALTER TABLE stammor ENABLE ROW LEVEL SECURITY;

-- 3. Skapa en regel så att din hemsida på Cloudflare kan LÄSA data utan lösenord
CREATE POLICY "Allow public read access"
  ON stammor FOR SELECT
  USING (true);

-- 4. Lägg in en test-rad så vi ser att det funkar
INSERT INTO stammor (song_title, voice_part, pitch_data)
VALUES (
  'Test-låt', 
  'Sopran', 
  '[
    {"time": 1.0, "pitch": 60, "text": "Väl-"},
    {"time": 1.5, "pitch": 62, "text": "kom-"},
    {"time": 2.0, "pitch": 64, "text": "men!"}
  ]'::jsonb
);