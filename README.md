## Installing and using the code assessment tool with cs50.dev

### Installation

Step 1: Typing in the terminal, create a new directory:

```
cd
mkdir ~/aiAssessment
cd ~/aiAssessment
```

Step 2: Copy and paste the following two lines into your terminal:

```
wget https://raw.githubusercontent.com/margarettanzosh/distro/refs/heads/main/setup.sh
wget https://raw.githubusercontent.com/margarettanzosh/distro/refs/heads/main/assess
```

Step 3: Execute setup,sh and add the key when prompted:

in your terminal type:

```
source setup.sh
```

When prompted for your key copy and paste this line:

Sk-ant-api03... (and so on)

This is the ANTHROPIC_API_KEY I temporarily gave to students to paste into this prompt, and then deleted from google classroom after then completed the installation.

### Using the tool

Assess your understanding of your own program code!

in your terminal type:

```
cd
```

to return to your main directory.

You are now ready to self assess yourself for any of your program code!
To use this tool, just cd into a directory that holds a program you want to assess, for instance readability.py and type:

```
assess readability.py
```

Answer the questions and if you don't know any answers, you can ask the AI. 
If the AI asks you about distro code, you can tell it a particular function was starter code.

### Submitting the assessment

When done, submit the assessment file by typing in the terminal:

```
submit50 cs50nestm/checks/2026/assessment
```
