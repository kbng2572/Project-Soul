# 🧠 Project-Soul: Persistent AI Identity & Memory for Gemini CLI

> **"Powered by the OpenClaw Philosophy: Sovereign Identity, Local Memory."**

Project-Soul is a lightweight, folder-based framework designed to empower the **Gemini CLI** with a persistent **Soul (Personality)** and **Memory (Contextual State)**. 


https://github.com/user-attachments/assets/c6b6cb2f-695c-4606-a99b-e319cd9db659


Directly inspired by the [OpenClaw](https://github.com/openclaw/openclaw) architecture, Project-Soul brings the "Sovereign AI" experience to your local development environment—ensuring your AI agent isn't just a generic tool, but a consistent, state-aware partner that evolves with your project.

## 🧬 The OpenClaw Connection

Project-Soul implements the core tenets of the **OpenClaw** philosophy:

1.  **Sovereign Identity (`SOUL.md`)**: Following the OpenClaw pattern, we separate the agent's personality from its underlying logic. By defining a `GEMINI_SOUL.md`, you grant the Gemini CLI a unique "vibe," values, and behavioral constraints that stay consistent across sessions.
2.  **Local Persistence (`MEMORY.md`)**: AI memory should be local and project-specific. Project-Soul uses a localized memory ledger to "claw back" project context, allowing the Gemini CLI to remember technical decisions, API keys, and progress without relying on centralized cloud storage.
3.  **Workspace Awareness**: Just like an OpenClaw agent, Project-Soul binds the AI to your current workspace. The agent's knowledge and personality are scoped to the folder, making it a true "Resident Expert" of your project.

## 🌟 Key Features

*   **Identity Modularity**: Swap "Souls" (e.g., Hacker, Specialist, or Reviewer) by simply editing the local `GEMINI_SOUL.md`.
*   **Stateful Engineering**: The Gemini CLI maintains a "Historical Awareness" of your project through the `GEMINI_MEMORY.md` ledger.
*   **100% Local & Portable**: Your AI's soul and memory live in your project folder. Move the folder, and the AI moves with it—no setup required.
*   **Gemini CLI Optimized**: Specifically tuned to leverage the massive context window and tool-use capabilities of the Gemini ecosystem.

## 🛠️ Implementation

*   **`GEMINI_SOUL.md`**: The behavioral blueprint and identity definition.
*   **`GEMINI_MEMORY.md`**: The structured project ledger (Achievements, Status, Next Steps).
*   **`setup_soul.py`**: The OpenClaw-style automation script that binds the local soul to the global Gemini CLI configuration.

## 🚀 Quick Start

1.  Clone this repository to your local machine.
2.  Run `python setup_soul.py` in your target project folder.
3.  Trigger the "Contextual Recall" by typing the keyword `gemini_rocks`.

---
*Conceptualized and Architected by kbng2572, implementing the OpenClaw philosophy for the Gemini CLI ecosystem.*
