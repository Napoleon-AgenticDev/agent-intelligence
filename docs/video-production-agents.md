# Video Production Agents

This document catalogs AI agents and skills focused on video production, including script generation, video creation, editing, voice-over, and publishing automation.

## Top Agent Systems

### AgentCut

**Repository**: https://github.com/calderbuild/agentcut
**Stars**: 35
**Primary Language**: HTML, Python

**Description**: Multi-Agent AI Video Production Pipeline. 6 specialized agents collaborate to produce videos from a single prompt.

**Agent Pipeline**:

```
User Prompt
    ↓
[Director Agent] - Analyzes creative vision, plans shots
    ↓
[Script Agent] - Writes production script with prompts, narration, subtitles
    ↓
[Visual Agent] ─┬─ Hailuo Video
[Voice Agent] ──┼─ Speech TTS (emotion)
[Music Agent] ──┴─ Music Gen
    ↓
[Editor Agent] - ffmpeg: concat, mix audio, burn subtitles
    ↓
Final MP4 Output
```

**Key Features**:
- 6 specialized agents with single responsibility
- Parallel execution (video, voice, music concurrent)
- Real-time SSE streaming progress
- One prompt → full video with narration, subtitles, music
- Cost: ~$0.50 per 3-shot video

**Tech Stack**:
- LLM: MiniMax M1
- Video: MiniMax Hailuo 2.3 (1080P, 6s clips)
- Voice: MiniMax Speech-2.6-HD (TTS with emotion)
- Music: MiniMax Music-2.0
- Composition: ffmpeg

---

### OpenMontage

**Repository**: https://github.com/calesthio/OpenMontage
**Stars**: 732
**Primary Language**: Python

**Description**: World's first open-source, agentic video production system. 11 pipelines, 49 tools, 400+ agent skills.

**Architecture**:
```
Agent reads pipeline manifest (YAML)
    ↓
reads stage director skill (MD)
    ↓
uses tools (Python BaseTool subclasses)
    ↓
self-reviews (meta skill)
    ↓
presents to human for approval
```

**Pipeline Stages**:
`research → proposal → script → scene_plan → assets → edit → compose`

**Available Pipelines**:

| Pipeline | Best For | Stability |
|----------|----------|-----------|
| animated-explainer | Topic to fully generated explainer | production |
| (10 more...) | | |

**Layer Map**:
- Layer 1: Pipeline definitions (what to do)
- Layer 2: Stage directors (when to do it)
- Layer 3: Provider skills (how to do it)

**Key Features**:
- 11 production pipelines
- 49 tools
- 400+ agent skills
- Checkpoint system for state management
- Cost tracking and budget governance
- Human approval gates
- Model-agnostic routing

---

### AITuber Skill

**Repository**: https://github.com/aituberapp/ai-video-skill
**Last Push**: April 2026

**Description**: AI video creation skill for Claude Code, Cursor, and AI coding agents. Create YouTube Shorts, TikTok, Instagram Reels.

**Capabilities**:
- 1,300+ AI voices (filter by gender, accent, age, language)
- Generate videos from script or idea
- AI narration, visuals, synced captions
- MP4 exports
- Direct publishing to YouTube/Instagram

**API Endpoints**:
| Endpoint | Description |
|----------|-------------|
| GET /voices | Browse 1,300+ AI voices |
| POST /videos/generate | Create video from script |
| GET /videos | List all videos |
| POST /publications | Publish to connected channels |

---

### VideoDB Skills

**Repository**: https://github.com/video-db/skills
**Stars**: 48

**Description**: Server-side video workflows for agents: ingest, understand, search, edit, stream.

**Capabilities**:
- **See**: Realtime desktop screen, mic, system audio, RTSP streams, files, URLs, YouTube
- **Understand**: Index/search spoken words and visual scenes
- **Act**: Generate transcripts, subtitles, AI media, edit clips, overlays, exports

**Key Features**:
- Single consistent interface for video
- Server-side processing (no ffmpeg on client)
- Realtime and batch workflows
- Playable HLS links for outputs

**Supported Platforms**: macOS, Linux, Windows

---

### AI Video Producer Skills

**Repository**: https://github.com/zysilm-ai/ai-video-producer-skill

**Description**: LLM Agent skill to create videos via local diffusion models using WAN 2.2 video generation and Qwen Image Edit keyframe generation via ComfyUI.

**Key Features**:
- 100% Local (no cloud APIs needed)
- Fast generation (~36 sec/image, ~2 min/5-sec video)
- Low VRAM (works on 10GB GPUs with GGUF quantization)
- Video-First or Keyframe-First pipeline modes

---

### Flow Video Producer Skill

**Repository**: https://github.com/zysilm-ai/video-producer-skill

**Description**: Claude Code skill for AI video production using Google Flow via MCP Playwright browser automation.

**Key Features**:
- Cloud-based (no GPU required)
- Uses Veo 3.1 Fast for video, Nano Banana Pro for images
- MCP Playwright automation
- Self-healing (adapts to UI changes)
- Video-first pipeline for continuity

---

## Video Production Skills by Category

### Pre-Production

| Skill | Description |
|-------|-------------|
| story-architect | Story structure, character arcs |
| script-breakdown | Scene-by-script analysis |
| character-psychology | Character motivation, arcs |
| research-agent | Research and plausibility validation |

### Production

| Skill | Description |
|-------|-------------|
| shot-planner | Shot planning and storyboarding |
| prompt-packager | Provider-specific prompt engineering |
| storyboard-generator | Visual storyboard creation |
| qc-grader | Quality control scoring |

### Post-Production

| Skill | Description |
|-------|-------------|
| video-editor | ffmpeg editing, concatenation |
| audio-mixer | Voice and music mixing |
| subtitle-generator | Burn-in subtitles |
| export-manager | Format optimization, export |

### Distribution

| Skill | Description |
|-------|-------------|
| youtube-publisher | YouTube upload, metadata |
| tiktok-publisher | TikTok/Reels formatting |
| thumbnail-generator | Auto-thumbnail creation |

---

## Technical Patterns

### Multi-Agent Video Pipeline

```python
# Parallel execution pattern
async def produce_video(prompt):
    # Stage 1: Sequential
    director = await director_agent.analyze(prompt)
    script = await script_agent.write(director)
    
    # Stage 2: Parallel
    visual_future = visual_agent.generate(script.visuals)
    voice_future = voice_agent.generate(script.narration)
    music_future = music_agent.generate(script.mood)
    
    visual, voice, music = await gather(visual_future, voice_future, music_future)
    
    # Stage 3: Sequential
    final = await editor_agent.compose(visual, voice, music)
    return final
```

### Provider Routing

```yaml
model_policy:
  - tier: 1  # Cheapest
    models: [gpt-4o-mini, claude-haiku]
    use_for: [outline, structure]
    gates:
      - quality_score: 7
      
  - tier: 2  # Mid-tier
    models: [gpt-4o, claude-sonnet]
    use_for: [script, detailed_prompts]
    
  - tier: 3  # Premium
    models: [gpt-4-turbo, claude-opus]
    use_for: [final_generation, complex_shots]
```

### Skill Structure for Video

```
video-skill/
├── SKILL.md              # Stage director instructions
├── providers/
│   ├── hailo.yaml        # Model-specific settings
│   ├── minimax.yaml
│   └── runware.yaml
├── prompts/
│   ├── shot_composition.md
│   ├── style_guide.md
│   └── narrative_flow.md
└── scripts/
    ├── ffmpeg_compose.py
    └── quality_check.py
```

---

## Cost Comparison

| System | Cost per Video | GPU Required |
|--------|----------------|--------------|
| AgentCut | ~$0.50 (3-shot) | No |
| OpenMontage | Variable (model routing) | Optional |
| AITuber | API-based | No |
| VideoDB | API-based | No |
| AI Video Producer | Local compute | Yes (10GB+ VRAM) |
| Flow Video | API-based | No |

---

## References

- AgentCut: https://github.com/calderbuild/agentcut
- OpenMontage: https://github.com/calesthio/OpenMontage
- AITuber: https://github.com/aituberapp/ai-video-skill
- VideoDB: https://github.com/video-db/skills
- AI Video Producer: https://github.com/zysilm-ai/ai-video-producer-skill