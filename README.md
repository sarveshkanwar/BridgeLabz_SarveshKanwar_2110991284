
# BridgeLabz_SarveshKanwar_2110991284

11th December
# Topics Covered: REBASE, MERGE, ORPHAN BRANCH, PRUNE.

## Git Commands

**Rebase Commands**:
- `git rebase` - Reapply commits on top of another base tip.
- `git rebase --continue` - Continue rebasing after resolving conflicts.
- `git rebase --abort` - Abort the rebase process.
- `git rebase <branch-name>` - Rebase the current branch onto `<branch-name>`.

**Merge vs Rebase**:
- `git merge` vs `git rebase`: `git merge` combines the histories of two branches, while `git rebase` rewrites the history by placing your changes on top of another branch.

**Orphan Branch**:
- `git checkout --orphan <branch-name>` - Create a new branch with no commit history.
- `git reset --hard` - Reset the working directory and staging area to match the most recent commit.

**Git Add and Commit**:
- `git add <file>` - Stage a file for commit.
- `git commit -m "<message>"` - Commit the staged files with a message.
- `git push origin <branch-name>` - Push the changes to the remote branch.

**Git Merge with Orphan Branch**:
- `git merge <orphan-branch> --allow-unrelated-histories` - Merge an orphan branch with a different history into your current branch.

**Prune**:
- `git prune` - Remove unreachable objects from the repository.
- `git prune --dry-run` - Preview what would be pruned without actually performing the action.

> **Note:** Git automatically runs prune during garbage collection (`git gc`).
