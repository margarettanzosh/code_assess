# AP CSP FRQ Practice Tools (APassess)

This is the README for the AP coaching version of the assessment workflow.
It does not replace the original README.

## What This Version Includes

- `APassess`: AP CSP FRQ-style practice interview (10-12 questions)
- `read_transcript.py`: readable JSON transcript formatter
- `view_transcript`: simple launcher for transcript viewing with multiple attempt support

This version is coaching-focused:
- Not graded
- Gives feedback on student responses after initial questions
- Students can continue with more questions or stop after feedback
- Suggests improvements for FRQ explanations and AP Create requirement coverage
- Supports multiple practice attempts - each session is saved separately
- If a student ends early, they still receive a feedback summary

## Quick Install

Run from the project folder:

```bash
bash install_APassess.sh
```

This installs to `~/aiAssessment`, updates your PATH, and enables commands without `./`.
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

View your transcripts (will show a list to choose from if you have multiple practice attempts):

```bash
view_transcript
```

Open a specific transcript:

```bash
view_transcript assessment_John_Smith_20260423_143052.json
```

Show fewer messages:

```bash
view_transcript --limit 20
```

Include internal system messages:

```bash
view_transcript --show-system
```

**Note:** Each time you practice, a new transcript file is created with a unique timestamp. This allows you to:
- Practice multiple times with the same code
- Compare your responses across attempts
- See your improvement over time
- Choose which attempt to submit to your teacher

## Typical Student Workflow

1. Run `APassess` on their project file.
2. Answer 10-12 questions about their code.
3. Receive coaching feedback on their understanding.
4. Choose to continue with more questions or finish.
5. Review responses with `view_transcript` (select which attempt if multiple exist).
6. Practice again if desired - each session saves separately.
7. Submit their best transcript file (e.g., `assessment_StudentName_20260423_143052.json`) to teacher.

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
