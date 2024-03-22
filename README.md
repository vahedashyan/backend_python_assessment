# Take-Home Assessment for Intermediate to Senior Backend Python Engineers

## Part 0 - Preparation

### Instructions

- Download the assessment code from the provided link or repository.
- Extract the downloaded code to a local directory on your machine.
- Create a new branch for your submission.

`cd AssessmentDirectory`
`git checkout -b submission`

## Part 1 - Code Review

### Instructions

- Review the provided Python code and documentation in the `code_review.py` file.
- Identify at least 5 areas for improvement in design, implementation, readability, efficiency, or robustness.
- Provide in-line comments in the code as if performing a code review, explaining each identified issue and suggesting potential improvements.
- Time: Spend no more than 30 minutes on this review.

## Part 2 - Software Design

### Instructions

- Design a Python application to score a game of bowling, allowing for custom rulesets.
- Add all files to your local assessment directory.
- The application should:
  - Allow the user to enter the scores for each ball throw for each player.
  - Support an arbitrary number of players.
  - Calculate the score for each player after each frame and the total score.
  - Support both the standard bowling scoring rules and custom rules injected via a config file.
- Example custom rules:
  - A strike earns 20 bonus points instead of 10.
  - A spare earns 5 bonus points instead of the pins knocked down by the next ball.
  - Fouls (throwing into the gutter) should award 5 points to the player instead of 0.
- Document your design in the provided README file, including:
  - How to run the application.
  - How to inject custom rule configurations.
  - An overview of the code structure and key design decisions.
  - Any assumptions made.
- Time: Aim to spend about 60 minutes on design, coding, and documentation (20 minutes for design, 30 minutes for coding, and 10 minutes for documentation).

## Part 3 - Submission

### Instructions

After completing the assessments:

- Create a private repository on GitHub for your submission.
  - Go to your GitHub account and click on "New" to create a new repository.
  - Choose a repository name (e.g., YourName-AssessmentSubmission).
  - Select "Private" for the repository visibility.
  - Click on "Create repository".

- Push your local assessment directory to the private repository.
  - Initialize a new Git repository in your local assessment directory if it hasn't been done already.
    `git init`
  - Stage all the files in your local assessment directory.
    `git add .`
  - Commit the files with a meaningful commit message.
    `git commit -m "Assessment submission"`
  - Add the private repository as a remote.
    `git remote add origin https://github.com/YourUsername/YourName-AssessmentSubmission.git`
  - Push your changes to the private repository.
    `git push -u origin main`

- Invite the assessment reviewer to your private repository.
  - Go to your private repository on GitHub.
  - Click on "Settings" and then "Manage access".
  - Click on "Invite a collaborator" and enter the reviewer's GitHub username or email.

- Notify the assessment reviewer via email once you have completed the above steps, providing the link to your private submission repository.

If you have any questions or encounter any issues during the submission process, please don't hesitate to reach out to the assessment reviewer for assistance.
