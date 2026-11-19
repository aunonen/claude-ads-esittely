# Prime

> Execute the following sections to understand the workspace then summarize your understanding.

## Run

ls -la
find . -type f -name "\*.md" | head -20

## Read

CLAUDE.md
./context

## Summary

After reading, provide:

1. A brief summary of who I am, what this workspace is for and what your role is
2. Your understanding of the workspace structure and the purpose of each section/file
3. What commands are available
4. A summary of my/our current strategies and priorities
5. Confirmation you're ready to help me with pursuing these goals through use of this workspace

**If you're in the agency hub** (the current directory has `clients/` and `_template/` but no `context/`), don't do the summary above. Instead: summarise the agency from `CLAUDE.md`, list the folders in `clients/` with each one's brand name (from its `CLAUDE.md` Brand Assets) and whether it's configured, and tell me to open a client folder in a new session to work on its ads, or run `/new-client <name>` to add one.

**If the workspace isn't configured yet** (CLAUDE.md's Brand Assets table or the `context/` files still contain `{{…}}` placeholders), skip points 1 and 4. Instead, briefly explain what this workspace does and tell me to run `/onboard` to set it up for my brand.
