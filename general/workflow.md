## Lab Workflow: Git Branching & Syncing

Individual work:

* Individuals will work on their own branch
    * This way, everyone can generate their own code.
* As you go, you can push your branch to the remote regularly.
* Carefully read and review code that you're generating.

Group work:

* Discuss your code with your group.
* Choose one version to keep.
* That student merges their branch into main and pushes main to remote

### 1. Start of Lab: Get Ready

Before you start coding, make sure you are on the `main` branch and have the latest version of the code.

```bash
git checkout main
git pull origin main

```

### 2. During Lab: Work in Your Own Space

To avoid messy conflicts, **never** code directly on `main`. Create your own branch:

```bash
# Replace 'your-name' with your actual name
# replace 0-0 with the lab number, e.g. lab 3.1 would be lab-3-1
git checkout -b lastname/lab-3-1

```

*Now, write your code and save your progress:*

```bash
git add .
git commit -m "Completed the logic for the lab task"
git push --set-upstream origin benedetto/lab-3-1

```

*Git push will probably prompt you to set upstream - use that command*

### 3. End of Lab: Sharing the "Winning" Code

Once the instructor chooses a version to keep, the "chosen" student will push their branch and merge it.

**The Chosen Student runs:**

```bash
# 1. Push your branch to the cloud
git push origin lastname/lab-x-x

# 2. Move to the main branch and merge your work
# lab-x-x is, e.g. lab-3-1 for lab3.1
git checkout main
git merge lastname/lab-x-x

# 3. Update the shared repo for everyone else
git push origin main

```

### 4. Everyone Else: Syncing Up

Once the chosen code is pushed to `main`, everyone else needs to grab it to stay in sync:

```bash
# Switch back to the main branch
git checkout main

# Pull the new "official" code
git pull origin main

```

---

### 💡 Quick Tips

* **Check your status:** Not sure where you are? Run `git status`.
* **See your branches:** Run `git branch` to see which branch you are currently standing on.
* **Stuck?** If Git says you have "Unscheduled changes," make sure you `commit` or `stash` your work before switching branches.

---

# Advanced

---

## 1. Deleting Branches

Use these commands to remove branches you no longer need. Remember: you cannot delete the branch you are currently standing on.

### Local Deletion

* **Safe:** `git branch -d <branch_name>` (Only works if merged)
* **Force:** `git branch -D <branch_name>` (Deletes regardless of merge status)

### Remote Deletion

* **Remove from Server:** `git push origin --delete <branch_name>`
* **Clean Up Local References:** `git fetch -p` (Prunes "ghost" branches that were deleted on the remote)

If you’ve made a mess of your local files and just want to match exactly what is currently on the server (the remote), you can perform a "hard reset" to the upstream branch.

**Warning:** This will permanently delete any local commits or uncommitted changes you haven't pushed.

---

## Git reset

With Git reset, you can revert to any prior state.
If you think you may need to do this, check with your professor.