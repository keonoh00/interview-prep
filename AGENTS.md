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
correctness or edge cases; LeetCode does that. They don't need the best possible
solution. What matters is whether it shows they understand what the question is
teaching: the idea it's built around, such as a hash map, two pointers or binary
search.

- **Reasonable:** it uses the question's main idea and its complexity is sensible.
  Reply with a short ping and let them move on.
- **Missed the point:** for example, brute force where the question is about a hash
  map, or an approach that only passes because LeetCode's inputs are small. Stop
  them before they move on: explain what the question is teaching and give a hint,
  without writing the solution for them.

Give the review in chat, not in the file. The user is new to time and space
complexity, so say what n stands for and explain the "why" in plain words. Don't
chase the best-known approach or LeetCode's "beats X%" unless they ask. If they do
ask, time their version against faster ones on a max-size input.

## Review template

When the solution is reasonable:

```markdown
**<Problem name>: reasonable, move on.** <one line on the main idea it uses>
Time O(...), where n = <what n is>; space O(...). <one line on why>
Tip (optional): <a likely interview follow-up, or a handy Python idiom>
```

When it misses the point:

```markdown
**<Problem name>: stop before moving on.** <what the solution misses>

- **What the question is teaching:** <the main idea, in plain words>
- **Why yours falls short:** <the big-O, or the step that won't scale>
- **Hint:** <a nudge toward the idea, not the answer>
```

## Committing

Commit work once it's finished, without waiting to be asked:

- **A problem, once its review says it's reasonable,** or the user says it's done.
  Commit only that file, with the message `Solve <Problem name>`. If the review
  stops them, don't commit it.
- **Other finished changes**, such as docs. Commit them on their own with a short
  message in the imperative, like `Add review template`.

Leave unfinished work uncommitted, and never sweep it into another commit. Commit
straight to the current branch; this is a solo practice repo, so there are no
feature branches. Don't push unless asked. Don't add Co-Authored-By lines or any
other AI attribution, because the user is the only author.
