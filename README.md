# 🧠 AI Coding Skills for Antigravity

[![Antigravity Compatible](https://img.shields.io/badge/Antigravity-Compatible-purple?style=flat-square)](https://github.com/tecnoclu/AiCodingSkillsAntigravity)
[![Lean Philosophy](https://img.shields.io/badge/Methodology-Lean_Development-blue?style=flat-square)](.agent/constitution/lean_philosophy.md)

Welcome to the **AiCodingSkillsAntigravity** repository. This is a collection of high-impact agentic skills designed specifically for the **Antigravity** coding agent framework.

These skills are built to empower AI agents to act as **Autonomous Senior Engineers**, following strict "Lean Development" principles and robust safety protocols.

## 🚀 Why Use These Skills?

*   **Antigravity Native**: Fully optimized for the Antigravity context window and toolset.
*   **Lean Core**: Enforces "Stop Starting, Start Finishing" workflows to prevent hallucination loops.
*   **Safety First**: Includes "Verify Schema" protocols to stop database corruption before it starts.
*   **Plug & Play**: Modular design allows you to mix and match skills for any project.

## 📦 The Skills Collection

| Skill | Description | Invocation |
| :--- | :--- | :--- |
| **Dev Launcher** | Analyzes the project and generates a tailored 'run-dev.bat' script with a DOS-like interactive menu to launch development servers. | `@dev_launcher` |
| **Do Notes** | Instructions to look for files in "To_do" folder, analyze them, create tasks/implementation plan, and start working. | `@do_notes` |
| **Project Deployer** | Analyzes the project and generates a tailored 'deploy.bat' script for standardized deployment with interactive commit messages. | `@project_deployer` |
| **Skill Creator** | A meta-skill that assists the agent in creating and scaffolding new skills by generating the standard directory structure and configuration files. | `@skill_creator` |
| **Skill Hub** | A skill to discover, load, and use remote skills from the 'antigravity-awesome-skills' repository without permanent installation. | `@skill_hub` |
| **Text Note Processor** | Scans the 'Text notes' folder for tasks, executes them, and deletes the processed files. | `@text_note_processor` |
| **project_framework** | Creates a comprehensive Lean project management framework (rules, workflows, constitution) | `@project_framework` |

## 🔧 Installation

clone this repository into your local skills directory (e.g., `Documents/Apps/skills`):

```bash
git clone https://github.com/tecnoclu/AiCodingSkillsAntigravity.git
```

Then use the `skill_hub` or `Skill_creator skill` or manually copy the folders you need into your active project's `.agent/skills/` directory.

## 🤝 Contributing

Contributions are welcome! Please ensure any new skill follows the **Lean Constitution**:
*   **Atomic**: One skill, one clear purpose.
*   **Documented**: Must include a `SKILL.md` with clear instructions.
*   **Safe**: Must include safety checks (e.g., "Verify Schema").

---
*Built with ❤️ by [Tecnoclub](https://github.com/tecnoclu) for the Antigravity Community.*
