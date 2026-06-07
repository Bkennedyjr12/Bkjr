# Jarvis / ADA Research Findings

## Primary video

The provided YouTube video is titled **“I Created the AI Assistant We All Dreamed Of (Iron Man Jarvis)”** and appears on the **Naz Louis** YouTube channel, according to public search results for the video ID `MeEZpjGrpm0`.

## Primary code source

The creator’s public repository is **nazirlouis/ada_v2** at https://github.com/nazirlouis/ada_v2. The repository describes **A.D.A. = Advanced Design Assistant**, an Electron desktop application combining Google Gemini 2.5 Native Audio, computer vision, gesture control, web automation, smart home control, CAD generation, and 3D-printing workflows.

## Confirmed tools from video analysis and repository README

The confirmed stack includes: Google Gemini 2.5 Native Audio / Gemini Live API, Gemini Computer Use, Gemini 3.0 or a Gemini CAD-generation model as referenced in the video, Python 3.11, FastAPI, Socket.IO, Electron, React, Three.js, MediaPipe Hand Tracking, MediaPipe Face Landmarker, Playwright, Chromium, build123d, OrcaSlicer, Moonraker, OctoPrint, PrusaLink, python-kasa, TP-Link Kasa smart bulbs, Insta360 Link webcam, Creality K1 / K1 SE, file-based JSON memory, Visual Studio Code, Conda/Miniconda, Git, Node.js 18+, npm, and Google AI Studio for API key creation.

## Creator platform links discovered

The GitHub repository is public. A Patreon post by Naz Louis links to another repository, **nazirlouis/OmniBot**, and a Discord invite at https://discord.gg/MxcjC2rjxF. These should be checked as adjacent creator materials for additional tools or evolution of the assistant project.

## Official Gemini Live documentation notes

Google’s Gemini Live API documentation confirms it is intended for low-latency realtime voice and vision interaction. It supports continuous streams of audio, images, and text; produces natural audio responses; supports interruption, tool use/function calling, Google Search, and audio transcription. Its technical specifications list raw 16-bit PCM 16 kHz audio input and raw 16-bit PCM 24 kHz audio output over a stateful WebSocket. The capabilities guide also confirms configurable automatic VAD, audio input/output transcription, session/context handling, and audio/video streaming patterns.

## Video-observed tools and behaviors

The YouTube video analysis identified the custom assistant as A.D.A. / Advanced Design Assistant. The visible and spoken stack includes Gemini native audio as the core low-latency voice layer, tool calling, multimodal audio/text/video input, a browser/web agent, file/project memory, hand-tracking gesture control, smart-home control through Kasa bulbs, AI CAD generation, Creality K1/K1 SE 3D printers, and Creality Print in the demonstrated print workflow. The creator explicitly contrasts the old STT → LLM → TTS pipeline with native audio and emphasizes interruption: the user can interrupt the assistant mid-sentence and the assistant immediately stops speaking and listens.

## Creator platform verification

Public platform extraction confirms the creator/channel is **Naz Louis** (`@NazLouis`) and the linked ecosystem includes YouTube, Patreon, Discord, Instagram `nazlouis_yt`, X `nazlouis_yt`, GitHub `nazirlouis`, and member/channel support links. The public YouTube channel page lists the provided video as **“I Created the AI Assistant We All Dreamed Of (Iron Man Jarvis)”** and shows adjacent creator projects including Pixel, a local AI assistant, a Raspberry Pi assistant, robot arm work, and a one-hour Jarvis tutorial. The YouTube channel description for a newer Pixel video also exposes connected tools and links: Patreon support/code posts, an ElevenLabs discount link, Discord, Instagram, X, Seeed Studio XIAO ESP32-S3 Sense, and Seeed Studio 1.28-inch Round Touch Display. GitHub confirms the `nazirlouis/ada_v2` project describes A.D.A. as an Advanced Design Assistant using Gemini Native Audio, computer vision, gesture control, 3D CAD generation, Electron, React, FastAPI, Playwright, build123d, OrcaSlicer, Moonraker/OctoPrint, MediaPipe, TP-Link Kasa, Socket.IO, and file-based project memory.
