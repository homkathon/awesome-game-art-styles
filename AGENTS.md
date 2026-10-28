# Maintaining this repository (for coding agents)

Instructions for any AI agent (Codex, ChatGPT, Claude Code …) that updates this list. Humans: see CONTRIBUTING.md.

## How the repo works

- `tools/styles.py` is the source of truth: `GAMES`, `LEARN`, `ASSETS`, `SECTIONS`, `STYLES`, `SECTIONS_ZH`, `SUMMARY_ZH`.
- `tools/resources.md` and `tools/resources.zh-CN.md` hold the tables at the end of the READMEs.
- `README.md`, `README.zh-CN.md` and `styles/*/README.md` are generated. Never edit them by hand.
- After any change run `python3 tools/build.py`. It validates references and regenerates everything. Commit the generated files.
- CI (`.github/workflows/check.yml`) fails if generated files are stale or a link is dead.

## Routine update (run weekly)

Do these in order. Stop after step 4 if there is nothing to do; an empty week is fine.

1. **Fix what CI found.** Read the latest `check` workflow run. For each dead link, find the new URL or remove the entry.
   For a dead Steam screenshot: delete that game's entry from `tools/screenshots.json`, run
   `python3 tools/fetch_screenshots.py`, then re-pick the `hero` / `gallery` indices for every style that uses the game.
2. **Re-check licences** in `tools/resources.md` (and the zh copy) for one or two libraries. If a licence changed, update the
   emoji and note, and update the "checked on" date.
3. **Add 1–3 styles**, preferring the **Wanted** table in `tools/resources.md`. Follow "Adding a style" below.
   Remove a style from Wanted once it is added.
4. **Add resources** only if they teach a technique (tutorials, talks, breakdowns, shader libraries) or are asset libraries
   with a clear licence. Add them to `LEARN` / `ASSETS` and reference them from the relevant styles.
   For the **Popular X posts** table, look for creator-authored technical threads; verify the canonical post via X's public embed metadata, and update both language files. Treat it as a hand-curated selection, not a live ranking.
   Never invent popularity metrics or add posts that only promote a game without explaining a technique.
5. Run `python3 tools/build.py`, then open a pull request titled `Weekly update: <date>` listing what changed and why.
   Do not push to `main` directly.

## Adding a style

A style earns an entry when it is a recognisable look that more than one team could adopt, not a single game's identity.

1. Find **at least two** reference games on Steam. Get each app id from
   `https://store.steampowered.com/api/storesearch/?cc=us&l=en&term=<name>` and confirm with
   `https://store.steampowered.com/api/appdetails?appids=<id>&filters=basic`. Skip games that are delisted or have no screenshots.
2. Add them to `GAMES`, then run `python3 tools/fetch_screenshots.py` (it fetches only games used by a style, so add the
   style dict first with a placeholder hero, or fetch after step 3).
3. Add a `dict(...)` to `STYLES` with every field: `id`, `section` (index into `SECTIONS`), `title`, `zh`, `summary`, `spot`,
   `techniques`, `games`, `hero`, `gallery`, `learn`, `assets`, `similar`, `agent`. Copy the shape of an existing entry.
4. **Look at the screenshots** before choosing `hero` and `gallery`. The hero must be an in-game shot that shows the style
   clearly: no logos, title cards, menus, award collages or close-ups of UI. Prefer gallery shots from more than one game.
5. Add a one-line Chinese summary to `SUMMARY_ZH` (same meaning as `summary`, natural Chinese, not word-for-word).
6. `agent` steps must be concrete enough to implement: name the technique, the setting and the engine feature.
7. Run the build. If the style count changed, also update the number in `assets/compose.html` and mention in the PR that
   `assets/social-card.png` needs re-rendering and re-uploading (a human does that).

## Rules

- Never commit screenshots or other images of commercial games. Link to Steam-hosted URLs only.
- Never invent app ids, URLs, licences or facts about a game. If you cannot verify something, leave it out.
- Never describe a custom or unclear licence as CC0.
- Keep descriptions short and neutral. No affiliate links, no marketing language.
- Don't rename or remove existing style ids; other sites may link to `styles/<id>/`.
- If a site blocks the link checker (403 or a bot challenge) but works in a browser, add it to the lychee `--exclude`
  list in `check.yml` with a comment, instead of removing the link.
- Don't change the demos, the skill or the build scripts in a routine update unless CI requires it.
