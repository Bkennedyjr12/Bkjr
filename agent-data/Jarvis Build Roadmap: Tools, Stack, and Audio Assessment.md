# Jarvis Build Roadmap: Tools, Stack, and Audio Assessment

Prepared by **Manus AI**  
Date: **June 7, 2026**

## Executive summary

The creator behind the referenced video is **Naz Louis**, and the project shown in the video is best understood as a practical **A.D.A. / Jarvis-style multimodal desktop assistant** rather than a single off-the-shelf app. The public project ecosystem points to two closely related codebases: **A.D.A. V2**, which is the desktop “Advanced Design Assistant,” and **OmniBot / Pixel**, which extends the same direction into a more persistent robot/desk-assistant hub. The strongest confirmed stack is centered on **Google Gemini Live / Native Audio**, **Python FastAPI**, **WebSockets / Socket.IO**, **Electron + React**, **Playwright browser automation**, **MediaPipe vision/gesture tracking**, **build123d CAD generation**, **OrcaSlicer plus Moonraker/OctoPrint-style 3D printing**, **TP-Link Kasa smart-home control**, **openWakeWord**, **WebRTC VAD**, and optional **ElevenLabs realtime streaming TTS**.[^1] [^2] [^3]

For your project, I would not try to copy every capability at once. The correct path is to build **audio-first Jarvis core**, then add tools in layers. The audio functionality is the most important part because it creates the illusion of a living assistant. Based on the creator’s public repositories and official API documentation, the audio layer is genuinely strong for an MVP: it supports **low-latency streaming conversation**, **barge-in interruption**, **wake-word activation**, **post-reply follow-up listening**, **voice activity detection**, **native audio output**, and an optional **ElevenLabs voice upgrade** for higher personality and voice quality.[^4] [^5] [^6]

> **Bottom line:** The audio stack is good enough to build a convincing personal Jarvis today, especially on a desktop or local-device setup. The remaining work is not “can it talk?” but **how reliably it listens, when it should stay quiet, how it handles noise, and how safely it controls tools.**

## Confirmed creator platforms and source ecosystem

The creator’s public platform footprint includes the YouTube channel **Naz Louis**, GitHub account **nazirlouis**, Patreon support/code posts, Discord, Instagram `nazlouis_yt`, and X/Twitter `nazlouis_yt`. The YouTube channel page lists the referenced video as **“I Created the AI Assistant We All Dreamed Of (Iron Man Jarvis)”** and shows adjacent projects such as a local AI assistant, a Raspberry Pi assistant, an AI robot arm, and a Pixel desk assistant that can rewrite its own code.[^2]

| Source | What it contributed to this roadmap | Confidence |
|---|---|---:|
| **YouTube video: “I Created the AI Assistant We All Dreamed Of (Iron Man Jarvis)”** | Demonstrated Jarvis/A.D.A. concept, native voice interaction, interruptibility, multimodal tools, CAD, browser control, and smart-home style actions. | High |
| **GitHub: `nazirlouis/ada_v2`** | Primary public implementation for A.D.A. V2, including architecture, dependencies, setup, frontend/backend split, and tool categories. | High |
| **GitHub: `nazirlouis/OmniBot`** | More advanced assistant hub direction, including wake word, WebRTC VAD, Gemini Live defaults, Pixel voice settings, and optional ElevenLabs streaming TTS. | High |
| **Patreon** | Confirms creator distributes or references code through creator-support posts. | Medium |
| **Discord / Instagram / X** | Community and update channels, useful for tracking future releases, but not primary technical sources. | Medium |
| **Official Gemini Live, openWakeWord, and ElevenLabs docs** | Verified the feasibility and specifications of the voice architecture. | High |

## Tool inventory from the video and creator ecosystem

The following table consolidates the tools that should matter for your Jarvis project. I am separating **confirmed implementation tools** from **project-adjacent creator-platform tools** so the roadmap stays practical.

| Category | Tool / technology | Role in the Jarvis system | Recommended for your build? |
|---|---|---|---|
| Core AI model | **Google Gemini Live / Gemini Native Audio** | Realtime speech conversation, multimodal input, interruption handling, audio output, function/tool calling, and transcripts. | **Yes. Use as the first audio brain.** |
| AI SDK | **google-genai** | Python SDK used to connect backend services to Gemini models and Live sessions. | **Yes.** |
| Backend API | **FastAPI** | Local/web backend for assistant state, tools, UI communication, settings, and device control. | **Yes.** |
| Server runtime | **Uvicorn** | ASGI server for FastAPI. | **Yes.** |
| Realtime transport | **WebSockets** | Low-latency streaming channel for audio, events, and assistant responses. | **Yes.** |
| Realtime app events | **Socket.IO / python-socketio / socket.io-client** | UI-to-backend events for desktop state, tools, project files, and status updates. | **Yes, if using an Electron/React UI.** |
| Desktop app shell | **Electron** | Native-feeling desktop wrapper for the assistant UI. | **Yes, for a desktop Jarvis.** |
| Frontend framework | **React** | Assistant dashboard, chat state, settings, model viewer, tool panels, and transcript UI. | **Yes.** |
| Frontend build | **Vite** | Fast React development/build system. | **Yes.** |
| Styling | **Tailwind CSS** | UI styling system for fast dashboard development. | **Yes.** |
| Animation | **Framer Motion** | Smooth transitions and “alive” assistant UI behavior. | Optional but useful. |
| Icons | **Lucide React** | Clean dashboard icon set. | Optional. |
| 3D UI | **Three.js**, **@react-three/fiber**, **@react-three/drei** | 3D model display, CAD preview, avatar/visualization layer. | Yes, if you want 3D/robotic presence. |
| Audio capture/playback | **PyAudio** | Microphone input and speaker output in the Python desktop stack. | Yes for local desktop; consider alternatives later. |
| Wake word | **openWakeWord** | Local wake phrase detection such as “Pixel” or “Hey Jarvis.” | **Yes, phase two.** |
| Wake model runtime | **ONNX Runtime** | Runs custom `.onnx` wake-word model locally. | **Yes.** |
| Voice activity detection | **WebRTC VAD** | Detects when the user stopped speaking after wake or during a turn. | **Yes. Critical.** |
| Optional TTS | **ElevenLabs streaming TTS** | More characterful, polished synthetic voice output; creator uses realtime WebSocket-style TTS with PCM output. | **Yes as premium voice mode.** |
| ElevenLabs model | **eleven_flash_v2_5** | Low-latency ElevenLabs voice model in the creator’s OmniBot bridge. | Optional premium mode. |
| Browser automation | **Playwright + Chromium** | Browser agent for opening websites, clicking, scrolling, typing, and retrieving web information. | **Yes, with permissions.** |
| Computer vision | **OpenCV** | Camera frames, image processing, and vision support. | Yes. |
| Screen capture | **mss** | Desktop screenshot capture for computer-use or visual context. | Yes if local-control features are needed. |
| Image processing | **Pillow** | Image handling for UI, vision, and file workflows. | Yes. |
| Face/hand tracking | **MediaPipe** | Hand gestures, face landmarking, local face authentication, gesture interface. | Optional after MVP. |
| Face identity | **InsightFace** | Face embedding / recognition layer in OmniBot-style stack. | Optional; useful for local-personal assistant. |
| CAD generation | **build123d** | Parametric CAD generation and modification from assistant instructions. | Optional unless your Jarvis will design objects. |
| 3D model output | **STL** | Generated CAD model format for printing and preview. | Optional. |
| Slicing | **OrcaSlicer** | Converts STL into printable G-code. | Optional for 3D-print workflow. |
| Printer APIs | **Moonraker / OctoPrint / PrusaLink** | Wireless printer discovery/control and print job submission. | Optional. |
| Network discovery | **Zeroconf / mDNS** | Finds printers and devices on the local network. | Useful for smart devices and printers. |
| Smart home | **python-kasa** | TP-Link Kasa bulb/device control. | Yes if you use Kasa devices. |
| Bluetooth / hardware | **bleak** | BLE device communication in OmniBot. | Optional hardware phase. |
| Video/image IO | **imageio / imageio-ffmpeg** | Video and frame processing for camera/robot workflows. | Optional. |
| Environment config | **python-dotenv** | Local API-key and environment-variable management. | Yes. |
| Project memory | **File-based JSON storage** | Persists projects, settings, and assistant context locally. | Yes for MVP; upgrade later to SQLite/Postgres. |
| Creator platform | **Patreon** | Code/support distribution channel. | Track only; not part of build. |
| Creator community | **Discord** | Support/community channel. | Track only. |
| Creator socials | **Instagram and X/Twitter** | Updates and demos. | Track only. |
| Hardware platform | **Seeed Studio XIAO ESP32-S3 Sense** | Used in creator’s Pixel direction for low-cost robot/desk companion hardware. | Optional future physical Jarvis. |
| Display hardware | **Seeed Studio 1.28-inch round touch display** | Used in Pixel-style expressive desk assistant. | Optional future physical Jarvis. |

## Audio functionality assessment

The creator’s audio architecture is not a basic “speech-to-text, then chatbot, then text-to-speech” chain. It is much closer to a realtime voice-agent stack. Official Gemini Live documentation describes support for **low-latency realtime voice and vision interactions**, continuous streams of audio, images, and text, and natural voice responses.[^4] It also lists important agent features such as **interruption**, **tool use**, **audio transcription**, proactive audio behavior, and affective dialogue support depending on model/version.[^4] The capabilities page confirms raw PCM audio input/output, 24 kHz audio output, WebSocket connections, audio transcriptions, video frames, and configurable automatic VAD parameters.[^5]

| Audio component | What the creator appears to use | Why it matters | Quality assessment |
|---|---|---|---|
| Realtime conversation | **Gemini Live / Native Audio** | Avoids the slow STT → LLM → TTS loop and enables natural turn-taking. | **Very strong for MVP.** |
| Interruptibility | Gemini Live-style barge-in behavior | User can cut the assistant off while it is speaking. | **Essential and strong.** |
| Wake activation | **openWakeWord**, custom `pixel.onnx`, fallback `hey_jarvis` | Lets Jarvis stay idle until called. | **Good, but must be tuned in your room.** |
| End-of-speech detection | **WebRTC VAD** | Prevents awkward pauses and determines when your command is complete. | **Critical and mature.** |
| Post-reply follow-up | 10-second post-reply listen window in OmniBot defaults | Makes the assistant feel conversational after it answers. | **Excellent UX feature.** |
| Native voice output | Gemini audio output | Lowest-complexity default voice path. | **Good latency, voice character depends on model voices.** |
| Premium voice output | **ElevenLabs realtime streaming TTS** | More expressive branded voice; creator code uses PCM streaming and chunk scheduling. | **Best personality layer, but adds cost and latency risk.** |
| Transcript layer | Gemini input/output transcription | Enables logs, memory, summaries, and debugging. | **Very useful.** |
| Noise resilience | openWakeWord thresholding and optional VAD/noise suppression ecosystem | Reduces false wakeups and missed commands. | **Needs real-world testing.** |

### How good is the audio, really?

I would rate the current audio design as **8.5/10 for a personal desktop Jarvis MVP**, **7/10 for a household always-on assistant**, and **5.5/10 for production-grade commercial deployment without further hardening**. The reason is that the realtime model architecture is legitimately good, but real-world voice assistants are won or lost on microphone quality, echo cancellation, room noise, wake-word tuning, privacy controls, and failure recovery.

| Use case | Audio readiness | Explanation |
|---|---:|---|
| Desktop Jarvis at your workstation | **8.5/10** | Strong because the user is close to the microphone, the environment is predictable, and interruption/realtime responses matter most. |
| Home office / studio assistant | **8/10** | Very viable if you use a good mic, speaker separation/headphones, and tune wake thresholds. |
| Living-room always-on assistant | **7/10** | Works, but false wakes, background TV/music, and multiple speakers become harder. |
| Mobile assistant | **6.5/10** | Possible, but needs mobile-specific audio routing, battery handling, and OS permissions. |
| Commercial customer-support voice agent | **5.5/10** | Needs telephony, monitoring, consent logging, red-team safety, fallback flows, and strict latency SLAs. |

The best part of the creator’s implementation is the **turn-taking experience**. Gemini Live’s realtime stream, interruption support, audio transcription, and tool-calling capabilities are exactly what a Jarvis-style assistant needs.[^4] [^5] The OmniBot direction improves this with a more practical product layer: wake word on by default, post-reply listening, Gemini Live enabled by default, and a switch between Gemini-native TTS and ElevenLabs voice modes.[^3] The ElevenLabs bridge is especially valuable because it streams 24 kHz PCM chunks and uses a tunable chunk schedule, which gives you a real latency-versus-quality control surface.[^6]

The weak point is not the model; it is **acoustic robustness**. openWakeWord is strong for local wake detection and includes pretrained models such as “hey jarvis,” but the documentation itself emphasizes threshold tuning, false accepts, false rejects, and local testing for reliable deployment.[^7] For your build, the first serious technical milestone should be a voice test harness that logs wake detection, command start/end, response start, barge-in success, and total round-trip latency.

## Recommended architecture for your Jarvis

Your Jarvis should be built as a **local-first, cloud-brained assistant**. The local machine handles microphone capture, speaker output, wake word, VAD, UI, permissions, and tool execution. Gemini Live handles realtime conversation and reasoning. ElevenLabs can be added as a premium voice path when you want more personality than the native model voice. Tools should be exposed through a permissioned backend so Jarvis cannot click, buy, email, post, or delete files without clear confirmation rules.

| Layer | Recommended choice | Reason |
|---|---|---|
| Voice brain | **Gemini Live first** | Best balance of realtime audio, multimodal input, interruption, and tool use. |
| Premium voice | **ElevenLabs streaming TTS optional** | Better character voice; add after native audio works. |
| Wake layer | **openWakeWord + WebRTC VAD** | Local, fast, customizable wake phrase and speech-end detection. |
| Backend | **Python FastAPI + WebSockets** | Matches creator stack and is easy to extend with tools. |
| Desktop UI | **Electron + React + Vite** | Best match for a local Jarvis dashboard. |
| Tool bus | **Function registry with permission gates** | Keeps web, files, email, smart home, and automations safe. |
| Memory | **SQLite + files to start** | More durable than pure JSON but still simple. |
| Browser control | **Playwright** | Strong browser agent foundation. |
| Vision | **OpenCV + MediaPipe** | Camera, hand tracking, face auth, and presence detection. |
| Scheduling | **Background worker / cron-style scheduler** | Needed for reminders, daily briefings, and recurring automations. |
| Hardware expansion | **ESP32-S3 / robot display later** | Defer until the software Jarvis is stable. |

## Roadmap for building your Jarvis

### Phase 1: Audio-first MVP

The first milestone should be a voice assistant that you can speak to naturally from your desk. It should wake, listen, respond, and allow interruption. Do not begin with CAD, robot hardware, or complex automations. Those features will feel impressive only if the audio core is already smooth.

| Workstream | Build target | Acceptance test |
|---|---|---|
| Realtime session | Connect microphone input to Gemini Live and play audio output. | You can hold a 5-minute conversation without restarting. |
| Barge-in | Stop assistant speech when you interrupt. | Say “wait” mid-answer; Jarvis stops within roughly one second. |
| Transcripts | Store user and assistant transcripts. | Every turn appears in a local session log. |
| UI | Minimal Electron/React dashboard. | Shows connection state, transcript, mute, stop, and latency. |
| Safety | Global kill switch and push-to-talk fallback. | You can disable mic and tools instantly. |

### Phase 2: Wake word, VAD, and audio polish

Once the native audio path works, add **openWakeWord** and **WebRTC VAD**. The wake phrase can start as “Hey Jarvis,” because openWakeWord includes a pretrained model, and later move to a custom phrase. The creator’s Pixel-style setup uses a custom ONNX wake model with a fallback to `hey_jarvis`, adjustable wake threshold, and silence timing.[^3]

| Workstream | Build target | Acceptance test |
|---|---|---|
| Wake phrase | “Hey Jarvis” local wake detection. | Wake succeeds at least 19 out of 20 times in your normal desk setup. |
| VAD | Detect end of user speech. | Jarvis does not cut you off during normal pauses. |
| Post-reply listen | Keep listening briefly after responses. | Follow-up questions work without repeating the wake word. |
| Latency telemetry | Record wake-to-listen, listen-to-response, response-to-audio times. | A daily log shows median and worst-case latency. |
| Noise testing | Test music, TV, fan, and multiple-speaker scenarios. | False wake rate is low enough to leave the assistant running. |

### Phase 3: Tool registry and permissions

After the voice loop is reliable, add a tool registry. This is where Jarvis becomes useful. The creator’s ADA project exposes tools for web automation, CAD, smart home, project memory, and file actions.[^1] Your version should start with productivity and personal-life tools before advanced hardware.

| Priority | Tool | Implementation approach | Confirmation required? |
|---:|---|---|---|
| 1 | Notes and memory | SQLite plus Markdown files. | No for notes; yes for deletion. |
| 2 | Browser research | Playwright browser agent. | Yes before purchases, posts, logins, or forms. |
| 3 | Files/projects | Permissioned file read/write workspace. | Yes before overwriting or deleting. |
| 4 | Calendar/reminders | Calendar API or local scheduler. | Yes for external calendar edits. |
| 5 | Email drafts | Outlook/Gmail connector or API. | Always confirm before sending. |
| 6 | Smart home | Kasa or your actual device ecosystem. | Confirm for security-sensitive devices. |
| 7 | Personal-development planner | Custom routines for reflection, family time, travel, rest, and growth. | No for suggestions; yes for bookings/messages. |

Because your broader preferences include holistic development, the assistant should not be only a productivity machine. It should also schedule **family moments, retreats, comedy/night-out ideas, reflection blocks, healing routines, and personal-development check-ins**. This makes the Jarvis system personally useful instead of becoming another task manager.

### Phase 4: Memory and personality

A Jarvis assistant becomes valuable when it remembers context. Start with local project memory, user preferences, recurring goals, and long-term notes. Use a strict memory policy: the assistant should tell you when it saves important information, and you should have an interface for reviewing or deleting memory.

| Memory type | Examples | Storage recommendation |
|---|---|---|
| User profile | Name, voice preferences, time zone, preferred tone. | SQLite settings table. |
| Project memory | Current projects, goals, next actions, files. | SQLite plus project folders. |
| Personal routines | Fitness, family, reflection, retreat planning, learning. | Structured tables plus Markdown summaries. |
| Conversation summaries | Daily or weekly assistant summaries. | Markdown and embeddings later. |
| Safety preferences | Tools requiring confirmation, blocked sites/actions. | SQLite policy table. |

### Phase 5: Vision and local computer awareness

Only after the audio and memory core is stable should you add camera and screen awareness. This can include MediaPipe hand tracking, OpenCV camera frames, mss screen capture, and optional face authentication. The creator’s ADA README describes MediaPipe gesture controls, face authentication, and a “Minority Report” style interface.[^1]

| Feature | Why add it | Risk |
|---|---|---|
| Screen context | Jarvis can help with what is on your screen. | Privacy; must restrict screenshots. |
| Camera presence | Jarvis can know when you are present. | Privacy and false detections. |
| Face authentication | Blocks access unless you are recognized. | Reliability and setup burden. |
| Hand gestures | Fun, visual, futuristic control. | Not essential; can distract from core value. |

### Phase 6: Advanced builder tools

This is where you can add the impressive creator-style features: CAD, 3D printing, smart devices, hardware, and robot body. These should be modular plugins, not part of the core assistant. ADA V2’s public README identifies build123d for CAD, OrcaSlicer for slicing, and Moonraker/OctoPrint-style printer control.[^1]

| Advanced capability | Tool stack | When to add |
|---|---|---|
| CAD generation | build123d, STL export, Three.js preview. | After core Jarvis is reliable. |
| 3D printing | OrcaSlicer, Moonraker, OctoPrint, Zeroconf. | If you actively print objects. |
| Smart home | python-kasa or your actual device APIs. | After voice safety rules exist. |
| Robot/desk companion | ESP32-S3, display, BLE/Wi-Fi bridge. | Hardware phase, not MVP. |
| Local AI fallback | Local LLM plus local STT/TTS. | Later, for privacy/offline resilience. |

## Specific implementation sequence

The fastest credible build is a **six-week sprint**. This assumes we are building a desktop Jarvis first, then expanding.

| Week | Goal | Deliverable |
|---:|---|---|
| 1 | Core voice loop | Gemini Live microphone-to-speaker loop with transcript logging. |
| 2 | Desktop shell | Electron/React dashboard with mute, stop, connection state, and conversation history. |
| 3 | Wake and VAD | openWakeWord wake phrase, WebRTC VAD, post-reply listening, latency logs. |
| 4 | Tool registry | Notes, memory, browser research, file workspace, and confirmation gates. |
| 5 | Personal operating system | Daily briefings, calendar/reminders, personal-development and family/retreat planning workflows. |
| 6 | Premium polish | ElevenLabs voice mode, persona tuning, safety rules, reliability testing, and deployment packaging. |

## Tool choices I recommend for your version

| Decision | Recommendation | Why |
|---|---|---|
| Primary model | **Gemini Live** | Best match for the creator’s realtime voice-first approach. |
| Secondary model | Add another LLM later only for text-heavy reasoning. | Avoid complexity until voice loop works. |
| Voice output | Start with Gemini native audio; add ElevenLabs after. | Native audio is simpler; ElevenLabs improves personality. |
| Wake word | Start with openWakeWord `hey_jarvis`; later train custom phrase. | Fastest path to working wake. |
| VAD | WebRTC VAD now; evaluate Silero later. | Mature and simple. |
| UI | Electron + React + Vite. | Matches the public ADA direction and gives a native dashboard. |
| Tool execution | Python FastAPI tool registry. | Simple, inspectable, and safe. |
| Memory | SQLite + Markdown. | Better than raw JSON while still local-first. |
| Browser agent | Playwright. | Strong automation and testability. |
| Scheduling | Local worker first; hosted/persistent service later. | Keeps MVP simple. |
| Hardware | Defer ESP32/robot body. | Audio and tools matter more first. |

## Risks and guardrails

The main project risk is building too many flashy tools before the assistant is stable. The second risk is giving the assistant too much power too early. A personal Jarvis should have explicit permissions for sending messages, posting, purchasing, deleting files, controlling locks, or making irreversible changes.

| Risk | Mitigation |
|---|---|
| False wakeups | Tune threshold, require wake confirmation in noisy rooms, log false positives. |
| Assistant talks over user | Use VAD, barge-in handling, and short default responses. |
| Latency feels bad | Measure every stage; keep first response concise; use streaming audio. |
| Tool misuse | Add confirmation gates and per-tool permissions. |
| Privacy leakage | Local transcripts, explicit screenshot permissions, memory review panel. |
| Cost surprise | Track Gemini and ElevenLabs usage separately. |
| Internet failure | Add graceful offline mode and local fallback later. |

## Final recommendation

Build your Jarvis around **voice quality first**, because that is the feature that makes the assistant feel real. The creator’s most important lesson is not CAD or robot hardware; it is that a Jarvis-style assistant needs **native realtime audio, interruption, wake-word behavior, and persistent context**. Start with Gemini Live as the core. Add openWakeWord and WebRTC VAD next. Add a clean Electron dashboard and a permissioned tool registry. Then layer in browser automation, memory, calendar/reminders, personal-life planning, and smart home. Only after that should you add CAD, 3D printing, and robot hardware.

If we build this in the right order, your first useful version can be a **desktop Jarvis that listens, talks, remembers, researches, plans, and safely acts**. The more cinematic robot features can come later without compromising the foundation.

## References

[^1]: [GitHub — nazirlouis/ada_v2](https://github.com/nazirlouis/ada_v2), public README and dependency files for A.D.A. V2.
[^2]: [YouTube — Naz Louis channel](https://www.youtube.com/channel/UCDFNinEMZhfgm-5lQGI_dcA), public channel page listing the referenced Jarvis video and connected creator links.
[^3]: [GitHub — nazirlouis/OmniBot](https://github.com/nazirlouis/OmniBot), public OmniBot/Pixel repository inspected for wake-word, Gemini Live, and ElevenLabs voice architecture.
[^4]: [Google AI for Developers — Gemini Live API overview](https://ai.google.dev/gemini-api/docs/live-api), official overview describing realtime voice/vision interaction, interruption, tool use, and audio specifications.
[^5]: [Google AI for Developers — Live API capabilities](https://ai.google.dev/gemini-api/docs/live-api/capabilities), official capabilities guide for Live API modalities, PCM audio, transcriptions, VAD configuration, and model behavior.
[^6]: [ElevenLabs API Reference — WebSocket text-to-speech stream input](https://elevenlabs.io/docs/api-reference/text-to-speech/v-1-text-to-speech-voice-id-stream-input), official realtime TTS WebSocket endpoint documentation.
[^7]: [GitHub — dscripka/openWakeWord](https://github.com/dscripka/openWakeWord), open-source wake-word library documentation, pretrained models, thresholding, false-accept/false-reject discussion, and training guidance.
