# py5 + uv Setup (Processing-style, no Thonny)

This repo contains notes for the course
[Designing with Python: Programming for a Visual Context](https://www.domestika.org/en/courses/4307-designing-with-python-programming-for-a-visual-context)

## Goal

Run `py5` sketches with Processing-style syntax (`size()` instead of `py5.size()`) using a standard workflow (no Thonny).

---

## Key Insight

Processing-style code requires **runtime namespace injection**.

* `python main.py` → ❌ no injection → `NameError`
* `py5-run-sketch` → ✅ injects global names (`size`, `mouse_x`, etc.)

This is a runtime concern, not an IDE feature.

---

## Setup

### 1. Install Java

```bash
sudo pacman -S jdk-openjdk
```

(Required for the Processing backend)

---

### 2. Create project + install dependencies

```bash
uv init
uv add "py5[extras]"
```

The `extras` package provides the official runner.

---

### 3. Run sketches

```bash
uv run py5-run-sketch main.py
```

---

## Example

```python
def setup():
    size(400, 400)

def draw():
    background(240)
```

No imports required when using the runner.

---

## Optional: Shell alias

```bash
alias p5="uv run py5-run-sketch"
```

Then:

```bash
p5 main.py
```

---

## Notes

* Works in any editor (Zed, VS Code, Vim, etc.)
* Avoid `import py5` if you want Processing-style syntax
* Use standard Python execution only if you’re okay with `py5.` prefixes

---

## Common Failure Modes

* `NameError: size is not defined`
  → You ran with `python`, not `py5-run-sketch`

* Window doesn’t open
  → Java not installed or misconfigured

