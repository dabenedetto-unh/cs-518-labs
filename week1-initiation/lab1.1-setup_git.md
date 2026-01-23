
---

## Phase 1: Individual Environment Setup

Every team member must complete these steps to communicate securely with GitLab.

### 1. Configure Git & Generate SSH Keys

* **Configure Identity:** Open your terminal and set your global credentials:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@unh.edu"
```

* **Generate Key:** Run `ssh-keygen -t rsa -b 2048`.
* **Locate Public Key:** Open the generated `.pub` file (e.g., `C:\Users\Name\.ssh\id_rsa.pub`) in a text editor or use `cat` to view and copy the entire contents.

### 2. Add Key to GitLab

* Log in to [GitLab](https://gitlab.cs.unh.edu/) using your USNH username (e.g., abc1234).
* Navigate to **User Icon (top-right) > Preferences > SSH Keys**.
* Paste your public key into the field and save.

---

## Phase 2: Project Owner Tasks (One Person)

Ideally, the person most familiar with Git should serve as the Owner.

### 1. Create GitLab Project

* Create a **Blank Project**.
<!-- * **Uncheck** "Initialize project with a README". -->

### 2. Manage Members

Go to **Manage -> Members** in the left sidebar to add the following:

* **Maintainers:** Add the Professor and TA (Maeve Burwell: `mmb1177` and David Benedetto: `dabenedetto`).
* **Developers:** Add all other team members.

<!-- ### 3. Initialize Repository Structure

Initialize the local folder and push it to GitLab following the "Push an existing folder" instructions on the empty project page. -->

---

## Phase 3: Team Workflow & Testing

Once the Owner has pushed the structure, everyone must perform these actions to verify the setup.

### 1. Clone the Project

* In GitLab, click the blue **Code** button and copy the **SSH link**.
* In your terminal, navigate to your coursework directory and run:
```bash
git clone <url>
```

### 2. Edit and Sync Changes

* **Modify:** Open the directory in VS Code and modify `README.md` or create a new file.
* **Commit and Push:** Update the remote repository:
```bash
git add .
git commit -m "my first commit"
git push
```

* **Pull:** Retrieve updates from your teammates:
```bash
git pull
```

### 3. Conflict Resolution

* Coordinate with your team to intentionally trigger a merge conflict (two people editing the same line).
* Practice resolving the conflict, staging the fix, and pushing the result.
