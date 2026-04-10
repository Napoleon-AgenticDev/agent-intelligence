# 🎬 How We Made an Agent Alchemy Promo Video

> **A Step-by-Step Guide** (written like you're a 5th grader!)

---

## 🍿 What Are We Making?

We wanted to make a **1-minute video** that tells people about **Agent Alchemy** - a cool tool that helps computers write code better.

The video has:
- Someone **talking** (like a robot narrator)
- **Pictures** that change while they talk
- **Text on screen** that appears at the right time

---

## 🧰 The Tools We Used

| Tool | What It Does | Why We Used It |
|------|--------------|---------------|
| **ElevenLabs** | Turns text into robot voice | To create the narration audio |
| **GitHub** | Stores files online | To save and share our work |
| **Python** | A programming language | To tell the computer what to do |
| **FFmpeg** | Makes videos | To combine pictures + audio |
| **PIL (Pillow)** | Draws pictures with code | To create each frame |

---

## 📍 Step 1: Find Cool Stuff About Agent Alchemy

### What I Did:
1. I searched GitHub for "agent alchemy"
2. Found a repo called `sequenzia/agent-alchemy`
3. Read what it does → It has 28 skills and 16 agents!

### What You Would Do:
```bash
# Just search on GitHub!
# Go to: https://github.com
# Type in search bar: "agent alchemy AI"
```

---

## 📍 Step 2: Get API Keys

### 🔑 What's an API Key?
Think of it like a ** password ** that lets your computer use a service. Like how you need a library card to borrow books!

### Getting ElevenLabs Key:
1. Go to: https://elevenlabs.io
2. Click "Login" or "Sign Up"
3. Go to Settings → API Keys
4. Click "Create new secret key"
5. Copy the key (looks like: `8d8f6fa7decc0...`)

⚠️ **Important**: Never share your key! It's like your password.

### Saving It:
We saved it in a file called `.env`:
```
ELEVENLABS_API_KEY=8d8f6fa7decc0391a86496573883742368d86fbda6ba1ee94f8022a312933c3d
```

---

## 📍 Step 3: Write the Script (What to Say)

### The Voiceover Script:
```
Agent Alchemy: Where AI Meets Structured Development

What if your AI coding assistant could do more than just write code? 
What if it could manage your entire development workflow?

Welcome to Agent Alchemy. It's not just another AI tool. 
It's a complete toolkit that transforms how you build software.

Agent Alchemy provides twenty-eight skills and sixteen specialized agents. 
From specification writing to code validation, 
from research to task orchestration, it turns your AI into a structured development partner.

The magic? It's all markdown. Plain text files that define 
how your AI thinks, works, and evolves. 
No locked-in frameworks. No proprietary walls. Just pure, editable workflow power.

Whether you're using Claude Code, OpenCode, or building your own agentic system, 
Agent Alchemy meets you where you are.

The future of software development isn't about AI replacing developers. 
It's about AI empowering them. 
And Agent Alchemy is the catalyst for that transformation.

Welcome to the age of Agent Alchemy. 
Build smarter. Ship faster. Alchemize your workflow.
```

---

## 📍 Step 4: Create the Voiceover (Robot Voice)

### The Code:
```python
#!/usr/bin/env python3
"""Turns text into robot voice"""

import os
import requests
from dotenv import load_dotenv

# Load our secret key
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Settings
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # "George" - a clear, professional voice
MODEL_ID = "eleven_flash_v2_5"   # Fast and good quality

def generate_speech(text, output_path):
    # Where to send the request
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    # The "ID card" - proves we can use the service
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    
    # What we want the robot to say
    data = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.5,        # How steady the voice is
            "similarity_boost": 0.8,  # How much it sounds like the original voice
        }
    }
    
    # Send request and save the audio
    response = requests.post(url, json=data, headers=headers)
    with open(output_path, "wb") as f:
        f.write(response.content)
```

### How to Run:
```bash
python3 generate_voiceover.py
```

### What Happens:
- Computer sends the text to ElevenLabs
- ElevenLabs reads the text in "George's" voice
- Returns an audio file (MP3)
- Saved as `voiceover.mp3` 🎵

---

## 📍 Step 5: Create the Video Pictures

### The Idea:
A video is just lots of pictures shown really fast! (30 pictures = 1 second)

We created **11 scenes** that change throughout the video:

| Time | What Shows On Screen |
|------|---------------------|
| 0-4s | AGENT ALCHEMY |
| 5-9s | THE CHALLENGE |
| 10-15s | THE SOLUTION |
| 16-21s | 28 SKILLS |
| 22-27s | 16 SPECIALIZED AGENTS |
| 28-33s | PURE MARKDOWN |
| 34-39s | WORKS WITH |
| 40-45s | THE FUTURE |
| 46-51s | BUILD SMARTER |
| 52-57s | SHIP FASTER |
| 58-68s | ALCHEMIZE YOUR WORKFLOW |

### Code (Simplified):
```python
from PIL import Image, ImageDraw, ImageFont

# The screen size (like HD TV)
WIDTH = 1920
HEIGHT = 1080

def create_frame(scene_text1, scene_text2):
    # 1. Make a colored background
    img = Image.new('RGB', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    
    # 2. Draw gradient (sky effect)
    for y in range(HEIGHT):
        # Fade from dark purple to lighter purple
        draw.line([(0, y), (WIDTH, y)], fill=(15, 10, 35))
    
    # 3. Add text
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    except:
        font = ImageFont.load_default()
    
    # Draw main title (with shadow for contrast)
    draw.text((WIDTH//2 + 4, HEIGHT//2 + 4), scene_text1, 
             font=font, fill=(0, 0, 0), anchor="mm")
    draw.text((WIDTH//2, HEIGHT//2), scene_text1, 
             font=font, fill=(255, 255, 255), anchor="mm")
    
    return img

# Create 2100 frames (70 seconds × 30 frames per second)
for frame_num in range(2100):
    frame = create_frame("AGENT ALCHEMY", "Where AI Meets...")
    frame.save(f"frames/frame_{frame_num:05d}.jpg")
```

---

## 📍 Step 6: Combine Pictures + Audio = Video

### The Magic Command:
```bash
ffmpeg -y \
  -framerate 30 \
  -i frames/frame_%05d.jpg \
  -i voiceover.mp3 \
  -c:v libx264 -crf 21 \
  -c:a aac -b:a 192k \
  -pix_fmt yuv420p \
  -shortest \
  agent-alchemy-video-final.mp4
```

### What FFmpeg Does:
1. Reads all 2100 pictures (frames)
2. Reads the audio (voiceover.mp3)
3. Stitches them together at 30 frames per second
4. Converts to video format (MP4)
5. Adds nice audio quality (192k AAC)

---

## 📍 Step 7: Save to GitHub

### The Steps:
```bash
# 1. Make a folder for the project
mkdir agent-alchemy-video
cd agent-alchemy-video

# 2. Tell git this is our project
git init

# 3. Add our files
git add .

# 4. Save our changes (like a save point in a game)
git commit -m "feat: Add 1-minute video about Agent Alchemy"

# 5. Send to GitHub (like uploading your game save)
git remote add origin https://github.com/YOUR_NAME/agent-intelligence.git
git push -u origin main
```

---

## 🔄 How to Automate This

### Option 1: Run Everything at Once
```bash
# One command to rule them all!
./create_video.sh
```

### Example Automation Script:
```bash
#!/bin/bash
# create_video.sh

echo "🎬 Starting video creation..."

# Step 1: Generate voiceover
echo "1️⃣ Creating voiceover..."
python3 generate_voiceover.py

# Step 2: Create video
echo "2️⃣ Creating video frames..."
python3 create_final.py

# Step 3: Upload to GitHub
echo "3️⃣ Uploading to GitHub..."
git add .
git commit -m "feat: Video update $(date)"
git push origin main

echo "✅ Done! Video is live!"
```

### Option 2: Schedule It (Run Every Week)
```bash
# Add to cron (automatic scheduler)
crontab -e

# Add this line to run every Monday at 9am:
# 0 9 * * 1 cd /path/to/project && ./create_video.sh
```

---

## 💡 Suggestions for Automation

### 1. Webhook Trigger
When you update a file → automatically make the video!

```yaml
# .github/workflows/video.yml
name: Create Video
on:
  push:
    paths:
      - 'script.md'
jobs:
  video:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate Video
        run: |
          pip install -r requirements.txt
          python3 generate_voiceover.py
          python3 create_final.py
      - name: Upload
        uses: actions/upload-artifact@v3
        with:
          name: video
          path: agent-alchemy-video-final.mp4
```

### 2. GitHub Actions
Automatically rebuild video when you change the script!

### 3. Different Voices
Try different voices for different videos:
- **Rachel** - Friendly, warm
- **George** - Professional, clear
- **Arnold** - Authoritative

### 4. Different Languages
ElevenLabs supports 70+ languages!

```python
# For Spanish voiceover:
data = {
    "text": "¡Bienvenido a Agent Alchemy!",
    "model_id": "eleven_multilingual_v2"  # Multi-language model
}
```

---

## 📊 Files We Created

| File | What It Is | Size |
|------|----------|------|
| `generate_voiceover.py` | Makes robot voice | 2.8 KB |
| `create_final.py` | Makes video frames | 6.5 KB |
| `voiceover.mp3` | Just the audio | 1.1 MB |
| `agent-alchemy-video-final.mp4` | The final video | 4.9 MB |

---

## 🎓 Glossary (Big Words Explained)

| Word | Simple Meaning |
|------|--------------|
| **API** | A way for programs to talk to each other |
| **API Key** | A password for computer services |
| **FFmpeg** | A tool that makes videos |
| **Frame** | One single picture in a video |
| **FPS** | Frames Per Second (how fast pictures change) |
| **Gradient** | A fade from one color to another |
| **MP3** | A music/sound file |
| **MP4** | A video file |
| **PIL/Pillow** | A library for making pictures with code |
| **Python** | A programming language |
| **Rendering** | Creating the final video |
| **TTS** | Text To Speech (robot voice) |

---

## 🔗 Links

- **ElevenLabs**: https://elevenlabs.io
- **Agent Alchemy**: https://github.com/sequenzia/agent-alchemy
- **Our Video Repo**: https://github.com/Napoleon-AgenticDev/agent-intelligence

---

## ✅ What Did We Learn?

1. **Find content** - Search GitHub for cool stuff
2. **Get API keys** - Sign up for services
3. **Write script** - What to say
4. **Make audio** - Text to speech
5. **Make pictures** - Frame by frame
6. **Combine** - FFmpeg stitches it together
7. **Share** - Upload to GitHub

You could make this for ANY topic! Just change the script! 🎉