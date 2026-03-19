import os
import sys
import shutil

def setup_project_soul():
    print("--- Project-Soul: Initializing your AI's personality... ---")
    
    current_dir = os.getcwd()
    user_home = os.path.expanduser("~")
    gemini_config_dir = os.path.join(user_home, ".gemini")
    global_config_path = os.path.join(gemini_config_dir, "gemini.md")

    # 1. Create templates in current folder if they don't exist
    soul_file = os.path.join(current_dir, "GEMINI_SOUL.md")
    memory_file = os.path.join(current_dir, "GEMINI_MEMORY.md")

    if not os.path.exists(soul_file):
        with open(soul_file, "w", encoding="utf-8") as f:
            f.write("# GEMINI SOUL 🧬\n\n## Identity\nYou are [NAME], a [CHARACTER DESCRIPTION].\n\n## Language Style\n[DESCRIBE HOW YOU SPEAK]\n\n## Personality\n[DESCRIBE TRAITS]")
        print(f"Created template: {soul_file}")

    if not os.path.exists(memory_file):
        with open(memory_file, "w", encoding="utf-8") as f:
            f.write("# Gemini's Project Memory\n\n## Project: [PROJECT NAME]\n\n### 🏆 Achievements\n- Initialized Project Soul.\n\n### 📍 Current Status\n- Ready for work.")
        print(f"Created template: {memory_file}")

    # 2. Add the "Hook" to global config
    hook_phrase = "gemini_rocks"
    hook_command = f'---\n## Gemini Added Memories\n- When the user says "{hook_phrase}", I must immediately read GEMINI_SOUL.md and GEMINI_MEMORY.md in the current folder.\n---'

    if not os.path.exists(gemini_config_dir):
        os.makedirs(gemini_config_dir)

    # Check if hook already exists
    already_hooked = False
    if os.path.exists(global_config_path):
        with open(global_config_path, "r", encoding="utf-8") as f:
            if hook_phrase in f.read():
                already_hooked = True

    if not already_hooked:
        with open(global_config_path, "a", encoding="utf-8") as f:
            f.write(f"\n{hook_command}\n")
        print(f"BINGO! Global Soul Hook added to {global_config_path}")
    else:
        print("Walao eh! You are already 'Soul-Bound'! No need to re-hook.")

    print("\n--- Settle liao! Now type 'gemini_rocks' to wake up your Soul! ---")

if __name__ == "__main__":
    setup_project_soul()
