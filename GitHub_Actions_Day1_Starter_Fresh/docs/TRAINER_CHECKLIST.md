# Trainer checklist (prepare BEFORE class)

1. Create an empty public GitHub repository `day1-cicd-starter`; ensure the default branch is named `main`.
2. Extract this ZIP and push all files, including hidden `.github/workflows/ci-cd.yml`. For example:

```bash
cd day1_github_actions_lab
git init
git branch -M main
git add .
git commit -m "Prepare Day 1 CI/CD starter"
git remote add origin https://github.com/YOUR-ACCOUNT/day1-cicd-starter.git
git push -u origin main
```

3. In starter repository **Settings > General**, enable **Template repository**.
4. In starter repository **Settings > Pages**, set **Source = GitHub Actions**, and run the workflow once.
5. Verify baseline four tests pass and the site publishes (version v1.0).
6. Give students the template URL. Each student clicks **Use this template > Create a new repository**. Do not have an entire class edit the same repository.
7. Students enable Pages separately on their own copies. If Actions are disabled, enable them under repository Settings > Actions.
8. Rehearse the red run from `Healthy` → `Unhealthy` and ensure the *last good website* is still live.
9. Ensure students can create PUBLIC repositories, or provide organization GitHub accounts with Pages entitlement.
10. Use the same mapping in teaching: GitHub push ~ CodePipeline trigger; tests ~ CodeBuild quality gate; Pages ~ deployment target; previous-content redeploy ~ manual rollback concept.

This starter intentionally does not provision AWS. AWS Skill Builder labs for IAM and S3 remain separate Day 1 exercises.
