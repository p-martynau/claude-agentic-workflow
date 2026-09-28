---
name: event-plan-html-theme
description: Reusable rendering rules and a standalone, print-friendly HTML template for the final Event Planner guide. Use only from html-builder, only after explicit approval, to render artifacts/event-plan.md into output/event-plan.html.
---

# event-plan-html-theme

Renders an approved `event-plan.md` into one self-contained HTML file: inline CSS, no external
requests, works when opened directly from the filesystem, and prints cleanly.

## Input

The approved `event-plan.md` content, split into its logical sections (overview, requirements
summary, venue, schedule, activities, catering, services, budget, weather/contingency if present,
sources).

## Template contract

Produce a single HTML document with:

- `<!DOCTYPE html>`, a descriptive `<title>` (event occasion + date), and a `<meta name="viewport">`.
- Inline `<style>` only — no linked stylesheets, fonts, or scripts. System font stack
  (`-apple-system, "Segoe UI", Roboto, sans-serif`) so it renders correctly offline.
- A sticky or top `<nav>` with in-page anchor links to each section.
- One `<section id="...">` per plan section, in the order listed above, each starting with an
  `<h2>`.
- The schedule rendered as a `<table>` (time / item / notes columns).
- The budget rendered as a `<table>` (line item / estimated or firm / cost / notes), with the
  total and contingency visually distinct (e.g., bold row).
- Every source URL rendered as a real `<a href="...">` link, opening in a new tab
  (`target="_blank" rel="noopener"`), grouped under a "Sources" section at the end.
- A `@media print` block that removes the nav, expands all sections, and uses black-on-white,
  serif body text for print/PDF.
- No JavaScript.

## Usage points

Invoked exclusively by the `html-builder` agent (`.claude/agents/html-builder.md`) after the
`approval-gate-guard` hook has permitted the write. Do not use this skill to render a draft or
unapproved plan.
