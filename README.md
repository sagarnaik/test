# Hello World Project

A simple Python project that demonstrates basic Git workflow including branch creation and merge request preparation.

## 🚀 Quick Start

### Run the Python Script
```bash
python3 hello_world.py
```

### Automated Git Workflow
```bash
chmod +x git_workflow.sh
./git_workflow.sh
```

## 📁 Project Structure

- `hello_world.py` - Main Python script that prints "Hello World"
- `git_workflow.sh` - Automated Git workflow script
- `requirements.txt` - Python dependencies (none required for basic functionality)
- `README.md` - Project documentation

## 🔧 Prerequisites

- Python 3.x
- Git
- Remote Git repository (GitHub, GitLab, etc.)

## 📋 Git Workflow Steps

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git remote add origin <your-repository-url>
   ```

2. **Run the Workflow Script**:
   ```bash
   ./git_workflow.sh
   ```

3. **Follow the Prompts**:
   - Enter a branch name when prompted
   - The script will automatically:
     - Create and switch to the new branch
     - Add and commit your changes
     - Push the branch to remote
     - Provide next steps for creating a merge request

## 🎯 Manual Git Commands

If you prefer to run Git commands manually:

```bash
# Create and switch to new branch
git checkout -b feature/hello-world

# Add changes
git add .

# Commit changes
git commit -m "feat: add hello world script"

# Push to remote
git push -u origin feature/hello-world
```

## 🔄 Creating a Merge Request

After running the workflow script:

1. Go to your Git hosting platform (GitHub, GitLab, etc.)
2. Navigate to your repository
3. Click "New Pull Request" or "New Merge Request"
4. Select source branch (your new branch) and target branch (main/master)
5. Add description and assign reviewers
6. Submit the merge request

## 🧪 Testing

Test the Python script:
```bash
python3 hello_world.py
```

Expected output:
```
Hello World!
```

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the Git workflow script
5. Create a merge request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
