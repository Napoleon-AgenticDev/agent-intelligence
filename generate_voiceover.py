#!/usr/bin/env python3
"""
Agent Alchemy Video - Voiceover Generator
Creates a 1-minute voiceover about Agent Alchemy using ElevenLabs TTS
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "JBFqnCBsd6RMkjVDRZzb"  # George - professional, clear voice
MODEL_ID = "eleven_flash_v2_5"  # Fast, high quality
OUTPUT_DIR = "/Users/napoleon/.openclaw/workspace/agent-alchemy-video"

SCRIPT = """
Agent Alchemy: Where AI Meets Structured Development

What if your AI coding assistant could do more than just write code? What if it could manage your entire development workflow?

Welcome to Agent Alchemy. It's not just another AI tool. It's a complete toolkit that transforms how you build software.

Agent Alchemy provides twenty-eight skills and sixteen specialized agents. From specification writing to code validation, from research to task orchestration, it turns your AI into a structured development partner.

The magic? It's all markdown. Plain text files that define how your AI thinks, works, and evolves. No locked-in frameworks. No proprietary walls. Just pure, editable workflow power.

Whether you're using Claude Code, OpenCode, or building your own agentic system, Agent Alchemy meets you where you are.

The future of software development isn't about AI replacing developers. It's about AI empowering them. And Agent Alchemy is the catalyst for that transformation.

Welcome to the age of Agent Alchemy. Build smarter. Ship faster. Alchemize your workflow.
"""

def generate_speech(text, output_path):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": API_KEY
    }
    
    data = {
        "text": text,
        "model_id": "eleven_flash_v2_5",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    print("Generating speech with ElevenLabs...")
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Audio saved to: {output_path}")
        return True
    else:
        print(f"❌ Error: {response.status_code} - {response.text}")
        return False

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, "voiceover.mp3")
    
    success = generate_speech(SCRIPT, output_file)
    
    if success:
        print(f"\n📁 Voiceover saved: {output_file}")
        print(f"📊 Duration: ~60 seconds (1 minute)")
        print("\nNext: Add visuals with video/images using ffmpeg or video editor")