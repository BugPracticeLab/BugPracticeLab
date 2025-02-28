# BugPracticeLab

## 🎯 Purpose
Welcome to the **Bug Practice Repo**! This repository is designed for beginners to practice **reporting and fixing bugs** in a real-world GitHub workflow. If you are new to open-source contributions or software debugging, this is the perfect place to start!

## How to Use This Repository for Practicing Issue Creation
1. Navigate to the **[Issues](../../issues)** tab.
2. Click **[New Issue](../../issues/new)**.
3. Provide a clear **title** and **description** of the bug.
4. Include:
   - 🛠 **Steps to reproduce**
   - ✅ **Expected behavior** vs. ❌ **Actual behavior**
   - 📷 Screenshots or logs (if applicable)
5. Submit the issue.

# How to Use This Repository for Fixing Bugs  

## 📌 Step 1: Finding and Understanding Issues  
1. Navigate to the **Issues** tab in this repository.  
2. Browse open issues and select one you want to work on.  
3. Read the issue description carefully to understand the problem.  
4. If additional details are needed, ask for clarification in the comments.  

---

## 🛠️ Step 2: Assigning the Issue (If Required)  
- If contributors need assignment before working on an issue, comment on the issue requesting assignment.  
---

## 🔄 Step 3: Fork and Clone the Repository  
Click [![Fork-This-Repo](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=skills&template_name=BugPracticeLab&owner=%40me&name=BugFixPractice&description=My+clone+repository&visibility=private) to fork this repo. (or)
1. Click the **Fork** button in the top-right corner of the repository.  
2. Clone the forked repository to your local machine:  
   ```sh  
   git clone https://github.com/your-username/repository-name.git  
   ```  
3. Navigate into the project directory:  
   ```sh  
   cd repository-name  
   ```  

---

## 🌿 Step 4: Create a New Branch  
Before making any changes, create a new branch for the issue:  
```sh  
git checkout -b fix-issue-name  
```  

---

## 📝 Step 5: Fix the Issue or Bug  
- Open the project in your preferred code editor.  
- Make the necessary changes to fix the issue.  
- Test your changes to ensure the issue is resolved.  

---

## 💾 Step 6: Commit and Push Changes  
1. Stage the modified files:  
   ```sh  
   git add .  
   ```  
2. Commit the changes with a Fix: [Issue Name], this map to the issue report and helps to close the issue:  
   ```sh  
   git commit -m "Fix: [Issue Name] - Short description of fix"  
   ```  
3. Push your changes to your forked repository:  
   ```sh  
   git push origin fix-issue-name  
   ```  

---

## 🔁 Step 7: Create a Pull Request (PR)  
1. Navigate to your forked repository on GitHub.  
2. Click **Compare & pull request**.  
3. Provide a clear description of your fix and link it to the original issue.  
4. Submit the pull request for review.  

---

## 📢 Step 8: Address Review Comments (If Any)  
- If maintainers request changes, update your branch accordingly.  
- Push the changes again using:  
   ```sh  
   git push origin fix-issue-name  
   ```  
- Once approved, your changes will be merged into the main repository. 🎉  

---

## 🔒 Step 9: Close the Issue

- Once your pull request is merged, navigate back to the Issues tab.
- Locate the issue you worked on and close it by clicking Close Issue.
- Confirm that the issue is resolved.

**Happy Coding!** 💻✨  


## ⚠️ Important Note
   - ❗ **Always fork the repository before working on it.**
   - ❗ **Do not create a pull request without first reporting an issue.**
Every PR should be linked to a reported issue for proper tracking and organization.

## 👥 Community & Support
- Join the discussion in **Issues** and **Pull Requests**.
- Ask questions and help others.
- Follow proper GitHub etiquette and be respectful.

Happy debugging! 🐛🚀

