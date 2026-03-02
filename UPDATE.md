## Updating the code assessment tool with cs50.dev

To update your assessment tool copy this line of code and paste into you terminal. You can click on the `copy` icon to copy the entire line.

```bash
cd ~/aiAssessment && [ -f assess ] && mv assess assess.old; wget -O assess "https://raw.githubusercontent.com/margarettanzosh/distro/refs/heads/main/assess" && chmod +x assess && echo "✓ Assess tool updated!" && cd -
```

You should now be ready to use the newest version of this tool.
