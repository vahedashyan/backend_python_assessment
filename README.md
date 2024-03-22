# backend_python_assessment
# Take-Home Assessment for Intermediate to Senior Backend Python Engineers

## Part 1 - Code Review

### Instructions
- Review the provided Python code and documentation
- Identify at least 5 areas for improvement in design, implementation, readability, efficiency, or robustness
- Provide in-line comments in the code as if performing a code review, explaining each identified issue and suggesting potential improvements
- Time: Spend no more than 30 minutes on this review
- Submission: Email the annotated code file

### Code and Documentation
see code_review.py

## Part 2 - Software Design

### Instructions
- Design a Python application to score a game of bowling, allowing for custom rulesets
- The application should:
  - Allow the user to enter the scores for each ball throw for each player
  - Support an arbitrary number of players
  - Calculate the score for each player after each frame and the total score
  - Support both the standard bowling scoring rules and custom rules injected via a config file
- Example custom rules:
  - A strike earns 20 bonus points instead of 10
  - A spare earns 5 bonus points instead of the pins knocked down by the next ball
  - Fouls (throwing into the gutter) should award 5 points to the player instead of 0
- Document your design in a README file, including:
  - How to run the application
  - How to inject custom rule configurations
  - An overview of the code structure and key design decisions  
  - Any assumptions made
- Time: Aim to spend about 60 minutes on design, coding and documentation
- Submission: Email a zip file containing all code and documentation
