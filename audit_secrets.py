import os
import re

PATTERNS = {
    "OpenAI Key": r"sk-[a-zA-Z0-9]{20,}",
    "GitHub Token": r"ghp_[a-zA-Z0-9]{20,}",
    "AWS Key": r"AKIA[0-9A-Z]{16}",
    "Generic Private Key": r"-----BEGIN PRIVATE KEY-----",
    "Supabase Key": r"eyJ[a-zA-Z0-9._-]{20,}",  # JWT pattern commonly used by Supabase
}

def scan_file(filepath):
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            for name, pattern in PATTERNS.items():
                if re.search(pattern, content):
                    issues.append(f"Found {name}")
    except Exception as e:
        issues.append(f"Could not read file: {e}")
    return issues

def audit():
    print("Starting Security Audit...")
    root_dir = os.getcwd()
    clean = True
    
    for root, dirs, files in os.walk(root_dir):
        if ".git" in root: continue # Skip git history
        
        for file in files:
            if file == "audit_secrets.py": continue
            path = os.path.join(root, file)
            issues = scan_file(path)
            if issues:
                clean = False
                print(f"⚠️  {file}: {', '.join(issues)}")
    
    if clean:
        print("✅ No obvious secrets found in any files.")
    else:
        print("❌ Secrets detected! See above.")

if __name__ == "__main__":
    audit()
