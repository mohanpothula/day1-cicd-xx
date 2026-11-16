# Day 1: GitHub Actions CI/CD - student starter repo

**Three connected exercises, one repository, no AWS account needed.**

1. Edit `site/index.html`, commit to `main`, and inspect the automatic workflow run.
2. Change `<span id="service-status" ...>Healthy</span>` to `Unhealthy`; the CI test must fail and block deployment. Change it back to `Healthy`.
3. Publish a new release through GitHub Pages, then restore the previous known-good version using a new commit.

## Files

- `site/`: sample website; change `site/index.html` in class.
- `tests/test_website.py`: four simple Python unit tests.
- `scripts/build_site.py`: produces `dist/` and `build-info.json`.
- `.github/workflows/ci-cd.yml`: runs tests, builds, uploads a release artifact and deploys GitHub Pages only after tests pass.
- `docs/STUDENT_QUICKSTART.md`: steps for the three exercises.
- `docs/TRAINER_CHECKLIST.md`: steps to create and distribute the template repo.

## Before the first run

Each student needs an individual GitHub repository. On GitHub Free, make it **Public** (GitHub Pages requires public repositories for free accounts). Navigate to **Settings > Pages > Build and deployment > Source: GitHub Actions**. Do not select 'Deploy from a branch'.

The pipeline starts on commits to `main` that modify `site/`, `tests/`, `scripts/` or the workflow. A README-only edit intentionally does not start the pipeline; use **Actions > Day 1 - Website CI/CD > Run workflow** to run it manually.

Expected website URL: `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`.

## Run locally (optional)

```bash
python -m unittest discover -s tests -v
python scripts/build_site.py
```

No additional Python packages are required. Do not commit `dist/` (it is generated automatically).

**Important:** This is a real GitHub Actions + GitHub Pages CI/CD exercise. It does not use CodePipeline, CodeBuild, CodeDeploy, or AWS. GitHub services illustrate the equivalent DevOps concepts.
