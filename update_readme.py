import os
import re

# Directory containing the skills
SKILLS_DIR = os.getcwd()
README_FILE = os.path.join(SKILLS_DIR, "README.md")

def get_skill_info(folder_path, skill_name_dir):
    skill_md = os.path.join(folder_path, "SKILL.md")
    if not os.path.exists(skill_md):
        return None

    try:
        with open(skill_md, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Simple regex to extract name and description from frontmatter or first lines
            name_match = re.search(r"^name:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
            desc_match = re.search(r"^description:\s*(.+)$", content, re.MULTILINE | re.IGNORECASE)
            
            # Fallback for name: Use directory name if not found, capitalize
            name = name_match.group(1).strip() if name_match else skill_name_dir.replace("_", " ").title()
            
            # Fallback for description
            desc = desc_match.group(1).strip() if desc_match else "No description provided."
            
            # Clean up description (remove markdown bolding or excessive whitespace)
            desc = desc.replace("**", "").replace("`", "")
            
            # Invocation example (e.g. @skill_name)
            invocation = f"`@{skill_name_dir}`"

            return {
                "name": name,
                "desc": desc,
                "invocation": invocation
            }
    except Exception as e:
        print(f"Error reading {skill_md}: {e}")
        return None

def update_readme():
    print("Updating README.md with skills...")
    skills = []
    
    # scan directories
    for item in os.listdir(SKILLS_DIR):
        item_path = os.path.join(SKILLS_DIR, item)
        if os.path.isdir(item_path) and not item.startswith("."): # Skip hidden folders
             info = get_skill_info(item_path, item)
             if info:
                 skills.append(info)
    
    skills.sort(key=lambda x: x['name']) # Sort by name

    if not skills:
        print("No skills found!")
        return

    # Check if README exists
    if not os.path.exists(README_FILE):
        print("README.md not found!")
        return

    with open(README_FILE, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Find the section to update. We assume there's a header "## 📦 The Skills Collection" 
    # and we will replace everything until "## 🔧 Installation" or EOF
    
    table_rows = []
    table_rows.append("| Skill | Description | Invocation |")
    table_rows.append("| :--- | :--- | :--- |")
    
    for s in skills:
        row = f"| **{s['name']}** | {s['desc']} | {s['invocation']} |"
        table_rows.append(row)
    
    new_table_content = "\n".join(table_rows)

    # Regex to find the block to replace
    # It looks for "## 📦 The Skills Collection" followed by anything, until the next H2 header.
    pattern = r"(## 📦 The Skills Collection\n\n)([\s\S]*?)(?=\n## |$)"
    
    replacement = f"\\1{new_table_content}\n"
    
    if re.search(pattern, readme_content):
        updated_content = re.sub(pattern, replacement, readme_content)
        
        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("README.md updated successfully.")
    else:
        print("Could not find '## 📦 The Skills Collection' section in README.md. Please add it manually.")

if __name__ == "__main__":
    update_readme()
