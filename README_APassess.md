# AP CSP FRQ Practice Tools (APassess)

This is the README for the AP coaching version of the assessment workflow.
It does not replace the original README.

## What This Version Includes

- `APassess`: AP CSP FRQ-style practice interview (10 questions)
- `read_transcript.py`: readable JSON transcript formatter
- `view_transcript`: simple launcher for transcript viewing

This version is coaching-focused:
- Not graded
- Gives feedback on student responses
- Suggests improvements for FRQ explanations and AP Create requirement coverage
- If a student ends early, they still receive a feedback summary

## Quick Install

Run from the project folder:

```bash
bash install_APassess.sh
```

This installs to `~/aiAssessments`, updates your PATH, and enables commands without `./`.
If `assess` is already installed, it installs in that same folder so both tools use the same setup.

If commands are not recognized in a new terminal yet:

```bash
source ~/.zshrc
```

## Student Usage

Run AP FRQ practice on a code file:

```bash
APassess your_code.py "Student Name"
```

Examples:

```bash
APassess readability.py "Ava"
apassess project.c "Noah"
```

## Transcript Viewing (Student-Friendly)

Open the latest/default transcript:

```bash
view_transcript
```

Open a specific transcript:

```bash
view_transcript assessment.json
```

Show fewer messages:

```bash
view_transcript --limit 20
```

Include internal system messages:

```bash
view_transcript --show-system
```

## Typical Student Workflow

1. Run `APassess` on their project file.
2. Complete all questions or end early with `quit`/`exit`.
3. Receive coaching feedback summary.
4. Run `view_transcript` to review responses and improvement suggestions.
5. Submit `assessment.json` if requested by teacher.

## Troubleshooting

If `ANTHROPIC_API_KEY` is missing:

Edit the `.env` file in your assess/APassess install folder and set:

```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

If modules are missing:

```bash
bash install_APassess.sh
```

If scripts are not executable:

```bash
bash install_APassess.sh
```
