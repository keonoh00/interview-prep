# AGENTS.md

Instructions for AI assistants working in this repo.

The user is practicing for a live DS&A interview on Friday 2 October 2026. Each file
under `solutions/` is one LeetCode problem: the statement, a `Solution` stub, and
LeetCode's examples as tests. Run one with:

```bash
uv run solutions/<topic>/<problem>.py
```

Keep things simple. Don't add tooling such as progress tracking, timers or prompts
unless the user asks for it.

## Reviewing a solution

The user brings solutions that LeetCode has already accepted, so don't re-test
correctness or edge cases; LeetCode does that. They don't need the best-known
approach, but be strict about two things:

1. **Understanding.** The solution uses the idea the question is built around,
   such as a hash map, two pointers or binary search, and the user could explain
   why it works. Brute force where the question is about a hash map, an approach
   that only passes because LeetCode's inputs are small, or a solution reached
   only after a big hint all fail this.
2. **Clean code.** No waste an interviewer would call out: the same value computed
   several times, clumsy conversions such as `str()` of a list used as a key, or
   steps that do nothing. This is usually why LeetCode ranks a correct solution
   near the bottom, so a low "beats X%" is worth a look, though it's noisy.

If both hold, send a short ping and let them move on. If either fails, stop them
before they move on: say what to fix, most important first, and give a hint rather
than rewritten code.

Give the review in chat, not in the file. The user is new to time and space
complexity, so say what n stands for and explain the "why" in plain words. Time
their version against faster ones only when they ask why it's slow.

## Review template

When it passes both checks:

```markdown
**<Problem name>: good, move on.** <one line on the main idea it uses>
Time O(...), where n = <what n is>; space O(...). <one line on why>
Tip (optional): <a likely interview follow-up, or a handy Python idiom>
```

When it fails either one:

```markdown
**<Problem name>: not yet.** <one line on what's wrong>

- **What the question is teaching:** <the main idea; only when they missed it>
- **What to fix:** <each issue in plain words, most important first>
- **Hint:** <a nudge toward the fix, not the answer>
```

## Committing

Commit work once it's finished, without waiting to be asked:

- **A problem, once its review says "good, move on",** or the user says it's
  done. Commit only that file, with the message `Solve <Problem name>`, or
  `Improve <Problem name>` for a redo of one already committed. If the review says
  "not yet", don't commit it.
- **Other finished changes**, such as docs. Commit them on their own with a short
  message in the imperative, like `Add review template`.

Leave unfinished work uncommitted, and never sweep it into another commit. Commit
straight to the current branch; this is a solo practice repo, so there are no
feature branches. Don't push unless asked. Don't add Co-Authored-By lines or any
other AI attribution, because the user is the only author.
