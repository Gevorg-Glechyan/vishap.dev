# vishap.dev

The vishap site: a static hub of small tools. Brand rules, tokens and assets live
in `brand/project/` (start with `brand/project/README.md`). `brand/gen.py`
generates every logo, product icon and illustration; change the script and
regenerate, don't edit the SVGs by hand.

## Branch Safety

- `main` is production: Vercel deploys it to vishap.dev. `dev` is where changes are
  combined, checked and tested before they reach `main`. Both are protected on
  GitHub: changes arrive through pull requests, and force pushes and deletion are
  blocked.
- Only the repository owner pushes directly to `main` or `dev`. An agent never
  does, even though the owner's credentials would allow it.
- Question-only and read-only investigation do not require a new branch.
- Before modifying repository files, check the current branch. If it is `main` or
  `dev`, update `dev` from its remote using a fast-forward-only pull, then create and
  switch to a new task branch from `dev` before making any changes.
- Open pull requests from task branches against `dev`. Use a different target only
  when the user explicitly requests it.
- Release flow: task branch → pull request into `dev` → check and test `dev` →
  pull request from `dev` into `main`.
- Never merge changes into `main` or `dev` unless the user explicitly asks for the
  merge.
