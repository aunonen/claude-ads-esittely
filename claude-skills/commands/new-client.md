# New Client

> Create a new client workspace from the agency template, ready for `/onboard`.

## Variables

name: $ARGUMENTS (the client's name, e.g. `Acme Oy`. If empty, ask for it.)

---

## Run

1. **Find the agency hub.** It's the folder that contains both `_template/` and `clients/`: the current directory, or a parent of it. If you can't find it, stop and ask the user where it is.
2. **Make a folder slug** from the name: lowercase, ASCII only (ä→a, ö→o, å→a), spaces and punctuation → `-`. E.g. `Acme Oy` → `acme-oy`. Show the slug to the user.
3. **Check it doesn't already exist** in `clients/`. If it does, stop and tell the user; never overwrite a client folder.
4. **Copy the template**, including hidden files:
   ```bash
   cp -r "<hub>/_template" "<hub>/clients/<slug>"
   ```
   Then confirm with `ls -la "<hub>/clients/<slug>"` that `CLAUDE.md`, `context/`, `reference/` and `.gitignore` are there.
5. **Don't onboard here.** The skills read paths like `context/` and `reference/` relative to the session's folder, so the client must be onboarded in a session opened **in the client folder**.

## Report

Tell the user:

- The new folder's path, as a clickable link
- Next step: open a new Claude Code session in that folder (in the desktop app: new session → choose the folder), then run `/onboard`
- Optional: add the client's own picks (competitor ads, past winners) to `reference/ad-inspiration/` next to the starter set
