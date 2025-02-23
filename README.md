# BugPracticeLab

## 🎯 Purpose
Welcome to the **Bug Practice Repo**! This repository is designed for beginners to practice **reporting and fixing bugs** in a real-world GitHub workflow. If you are new to open-source contributions or software debugging, this is the perfect place to start!

## 📝 How to Report a Bug
1. Navigate to the **[Issues](../../issues)** tab.
2. Click **[New Issue](../../issues/new)**.
3. Provide a clear **title** and **description** of the bug.
4. Include:
   - 🛠 **Steps to reproduce**
   - ✅ **Expected behavior** vs. ❌ **Actual behavior**
   - 📷 Screenshots or logs (if applicable)
5. Submit the issue.

## ⚠️ Important Note
❗ **Do not create a pull request without first reporting an issue.**
Every PR should be linked to a reported issue for proper tracking and organization.

## 🐞 How to Report a Bug
To report a bug, go to the **Issues** tab and click **New Issue**. Use the following template:

### Bug Report Template
```markdown
### 🐞 Problem
<!--- Provide a detailed description of the issue -->

### 🔍 Steps to Reproduce
1. Describe step-by-step how to reproduce the bug.
2. Include screenshots or logs if possible.

### 🎯 Expected vs. Actual Behavior
**Expected:** [What should happen?]
**Actual:** [What is happening instead?]

### 🛠 Possible Solution (Optional)
<!--- If you have an idea for a fix, mention it here -->

### 📋 Environment Details
- OS: [e.g., Windows 10, macOS 12]
- Browser/Version (if applicable): [e.g., Chrome 108]
- Any other relevant info
```

## 🔧 How to Fix a Bug
1. **Comment on the issue**: Mention that you’re working on it.
2. **Fork the repository**: Click the **Fork** button on the top right.
3. **Clone your fork**:
   ```sh
   git clone https://github.com/your-username/BugPracticeRepo.git
   cd BugPracticeRepo
   ```
4. **Create a branch**:
   ```sh
   git checkout -b fix-issue-<issue-number>
   ```
5. **Fix the bug and commit**:
   ```sh
   git add .
   git commit -m "Fix: <short description>"
   git push origin fix-issue-<issue-number>
   ```
6. **Submit a Pull Request (PR)**:
   - Go to your forked repo on GitHub and click "Compare & pull request".
   - Mention "Addresses #<issue-number>" in the PR description.
   - Request a review.
7. **Celebrate your contribution! 🎉**

## 👥 Community & Support
- Join the discussion in **Issues** and **Pull Requests**.
- Ask questions and help others.
- Follow proper GitHub etiquette and be respectful.

Happy debugging! 🐛🚀

