# Workflow Visualization

This document provides visual representations of the SGR-1 branching workflow.

## Branch Structure Diagram

```
main (production-ready)
  │
  ├── prototype/user-authentication (Team Member 1)
  │   ├── commit: Add login form
  │   ├── commit: Add password validation
  │   └── commit: Add session management
  │       └── [Merge to main via PR]
  │
  ├── prototype/data-visualization (Team Member 2)
  │   ├── commit: Setup chart library
  │   ├── commit: Create dashboard layout
  │   └── commit: Add interactive charts
  │       └── [Merge to main via PR]
  │
  └── prototype/api-integration (Team Member 3)
      ├── commit: Setup API client
      ├── commit: Add error handling
      └── commit: Implement caching
          └── [Merge to main via PR]
```

## Typical Development Flow

```
Day 1
─────────────────────────────────────────────────────────
main:        A────────────────────────────────────────→
                    │
prototype:          └─B─C──────────────────────────────→
                      │ │
                      │ └─ "feat: add basic UI"
                      └─── "feat: initialize project"


Day 2
─────────────────────────────────────────────────────────
main:        A────────D──────────────────────────────────→
                    │  │
                    │  └─ (another team member's merge)
                    │
prototype:          └─B─C─M─E─F────────────────────────→
                          │ │ │
                          │ │ └─ "feat: add validation"
                          │ └─── "feat: add form"
                          └───── merge main (includes D)


Day 3 (Ready to merge)
─────────────────────────────────────────────────────────
main:        A────────D──────M─G──────────────────────────→
                    │        │ │
                    │        │ └─ (merge prototype via PR)
                    │        │
prototype:          └─B─C─M─E─F─M─H────[PR]
                              │ │
                              │ └─ "docs: update README"
                              └─── merge main (final sync)
```

## Merge Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    MERGE WORKFLOW                            │
└─────────────────────────────────────────────────────────────┘

1. WORK ON PROTOTYPE
   ┌──────────────────┐
   │ prototype/       │
   │ your-feature     │──→ commit, commit, commit...
   └──────────────────┘

2. SYNC WITH MAIN (regularly)
   ┌──────────────────┐
   │      main        │──┐
   └──────────────────┘  │
                         ↓ merge
   ┌──────────────────┐  │
   │ prototype/       │←─┘
   │ your-feature     │
   └──────────────────┘

3. PREPARE FOR MERGE
   ┌──────────────────┐
   │ prototype/       │
   │ your-feature     │──→ final sync with main
   └──────────────────┘    resolve conflicts
                           test thoroughly

4. CREATE PULL REQUEST
   ┌──────────────────┐
   │   GitHub PR      │
   │                  │──→ Review by team
   │ prototype → main │──→ Discuss changes
   └──────────────────┘    Request changes

5. MERGE TO MAIN
   ┌──────────────────┐
   │      main        │←── merge prototype
   │   (updated)      │
   └──────────────────┘

6. CLEANUP (optional)
   ┌──────────────────┐
   │ prototype/       │
   │ your-feature     │──→ delete branch
   └──────────────────┘
```

## Multiple Team Members Working in Parallel

```
Time ──────────────────────────────────────────────────→

main:    A───────D─────────G───────J──────────→
         │       │         │       │
         │       │         │       │
Member1: └─B─C──[PR]       │       │
         (user-auth)       │       │
                           │       │
Member2:       └─E─F──────[PR]     │
               (dashboard)         │
                                   │
Member3:             └─H─I────────[PR]
                     (api-client)

Legend:
  A, D, G, J = commits on main
  B, C, E... = commits on prototype branches
  [PR]       = Pull Request & Merge
```

## Conflict Resolution Process

```
Step 1: Attempt Merge
┌────────────────┐
│ git merge main │
└────────────────┘
        │
        ├─→ No conflicts? ──→ ✓ Success! Continue work
        │
        └─→ Conflicts? ──→ Continue to Step 2

Step 2: Identify Conflicts
┌──────────────────────────┐
│ Git marks conflicted     │
│ files with:              │
│ <<<<<<< HEAD             │
│ your changes             │
│ =======                  │
│ changes from main        │
│ >>>>>>> main             │
└──────────────────────────┘

Step 3: Resolve
┌──────────────────────────┐
│ 1. Open each file        │
│ 2. Decide what to keep   │
│ 3. Remove markers        │
│ 4. Save file             │
└──────────────────────────┘

Step 4: Complete Merge
┌──────────────────────────┐
│ git add <resolved-files> │
│ git commit               │
│ git push                 │
└──────────────────────────┘
        │
        └─→ ✓ Merge complete!
```

## Pull Request Review Process

```
┌───────────────────────────────────────────────────────┐
│                    PR LIFECYCLE                        │
└───────────────────────────────────────────────────────┘

1. Create PR
   ┌─────────────────┐
   │ prototype/      │
   │ feature         │──→ GitHub
   └─────────────────┘

2. Automated Checks
   ┌─────────────────┐
   │ Run tests       │
   │ Check style     │──→ Pass? Continue
   │ Build project   │──→ Fail? Fix issues
   └─────────────────┘

3. Team Review
   ┌─────────────────┐
   │ Code review     │──→ Approve?  ──→ Continue
   │ by team         │──→ Changes requested? ──→ Update PR
   └─────────────────┘

4. Merge
   ┌─────────────────┐
   │ Approved +      │
   │ Checks pass     │──→ Merge to main
   └─────────────────┘

5. Cleanup
   ┌─────────────────┐
   │ Delete branch   │
   │ Update local    │
   └─────────────────┘
```

## Branch Naming Visual Guide

```
✓ GOOD BRANCH NAMES:
───────────────────────────────────────
prototype/user-authentication
prototype/dark-mode-theme
prototype/api-v2-client
prototype/mobile-responsive
prototype/payment-integration

✗ BAD BRANCH NAMES:
───────────────────────────────────────
mywork              (not descriptive)
USER_AUTH           (uses uppercase, missing prefix)
prototype/my-stuff  (too vague)
testing             (missing prefix)
new-feature         (missing prefix, vague)
```

## Commit Message Visual Guide

```
✓ GOOD COMMIT MESSAGES:
───────────────────────────────────────
feat: add user login form
fix: resolve navbar overlap on mobile
docs: update API documentation
refactor: simplify authentication logic
test: add unit tests for user service

✗ BAD COMMIT MESSAGES:
───────────────────────────────────────
fixed stuff         (too vague)
updates             (not descriptive)
WIP                 (work in progress, not final)
asdf                (meaningless)
changes             (what changes?)
```

## Git Status Examples

```
Example 1: Clean Working Tree
───────────────────────────────────────
$ git status
On branch prototype/user-auth
nothing to commit, working tree clean

→ You have no uncommitted changes


Example 2: Modified Files
───────────────────────────────────────
$ git status
On branch prototype/user-auth
Changes not staged for commit:
  modified:   src/auth.js
  modified:   README.md

→ You have changes that need to be committed


Example 3: Untracked Files
───────────────────────────────────────
$ git status
On branch prototype/user-auth
Untracked files:
  src/new-feature.js
  test/new-test.js

→ You have new files that Git doesn't track yet


Example 4: Staged Changes
───────────────────────────────────────
$ git status
On branch prototype/user-auth
Changes to be committed:
  modified:   src/auth.js
  new file:   src/new-feature.js

→ You have changes ready to commit
```

## Timeline Example: Complete Feature Development

```
Week 1
───────────────────────────────────────────────────
Mon: Create branch prototype/user-auth
Tue: Implement login form (commit)
Wed: Add validation (commit)
Thu: Add password hashing (commit)
Fri: Merge main, resolve conflicts (commit)

Week 2
───────────────────────────────────────────────────
Mon: Add session management (commit)
Tue: Write tests (commit)
Wed: Update documentation (commit)
Thu: Final sync with main (merge)
Fri: Create Pull Request

Week 3
───────────────────────────────────────────────────
Mon: Address review feedback (commit, push)
Tue: Get approval
Wed: Merge to main ✓
Thu: Delete branch, start new prototype
```

## Visualization of Parallel Development

```
         Day 1       Day 2       Day 3       Day 4
         ────────────────────────────────────────────→

main:    ●───────────●───────────●───────────●

Alice:   └─●─●───┐  (merge)
         (login)  ↓

Bob:         └─●─●─────┐  (merge)
             (dashboard) ↓

Carol:           └─●─●─●─────┐  (merge)
                 (API client) ↓

Result: All three features integrated into main!
```

## Summary

This visualization guide shows:
- How branches relate to main
- The flow of commits and merges
- How multiple team members work in parallel
- The pull request and review process
- Common scenarios and how to handle them

For more details, see:
- [BRANCHING_GUIDE.md](BRANCHING_GUIDE.md) - Detailed workflow
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Command reference
- [ONBOARDING.md](ONBOARDING.md) - Getting started guide
