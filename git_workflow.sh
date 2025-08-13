#!/bin/bash

# Git Workflow Script
# This script helps create a new branch and prepare for a merge request

echo "🚀 Starting Git workflow..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not in a git repository. Please run 'git init' first."
    exit 1
fi

# Get current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📍 Current branch: $CURRENT_BRANCH"

# Ask for new branch name
echo -n "🌿 Enter new branch name: "
read NEW_BRANCH_NAME

if [ -z "$NEW_BRANCH_NAME" ]; then
    echo "❌ Error: Branch name cannot be empty"
    exit 1
fi

# Create and checkout new branch
echo "🔀 Creating and switching to new branch: $NEW_BRANCH_NAME"
git checkout -b "$NEW_BRANCH_NAME"

if [ $? -eq 0 ]; then
    echo "✅ Successfully created and switched to branch: $NEW_BRANCH_NAME"
else
    echo "❌ Failed to create branch"
    exit 1
fi

# Add all changes
echo "📝 Adding all changes..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "feat: add hello world script

- Added Python script to print 'Hello World'
- Added Git workflow automation script"

# Push the new branch to remote
echo "🚀 Pushing branch to remote..."
git push -u origin "$NEW_BRANCH_NAME"

if [ $? -eq 0 ]; then
    echo "✅ Successfully pushed branch to remote"
    echo ""
    echo "🎉 Next steps:"
    echo "1. Go to your Git hosting platform (GitHub, GitLab, etc.)"
    echo "2. Create a new Merge Request/Pull Request from branch '$NEW_BRANCH_NAME' to '$CURRENT_BRANCH'"
    echo "3. Add description and assign reviewers"
    echo "4. Submit the merge request"
else
    echo "❌ Failed to push branch to remote"
    echo "💡 Make sure you have a remote origin configured: git remote add origin <repository-url>"
fi
