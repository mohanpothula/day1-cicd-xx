# Student Quickstart: 3 Connected Exercises

## Prerequisites
- GitHub account and your own *public* GitHub repository created from the trainer's template.
- Internet browser; no AWS credentials and no terminal required.
- In the student repository select **Settings > Pages > Source: GitHub Actions**.

## Exercise 1 - Automatic trigger (35-45 min)
1. Open `site/index.html` in your GitHub repository.
2. Click the pencil icon (Edit file).
3. Change `<strong id="release-version">v1.0</strong>` to `v1.1`.
4. Click **Commit changes...** and commit directly to `main`.
5. Open **Actions > Day 1 - Website CI/CD**. Select the latest commit.
6. Confirm **Test and build website** succeeds, then **Deploy website** succeeds.
7. Open **Settings > Pages > Visit site** (or the environment URL) and verify `v1.1`.
8. Record the run URL and screenshot the green workflow.

## Exercise 2 - CI quality gate (35-45 min)
1. In `site/index.html` change `Healthy` inside `<span id="service-status">` to `Unhealthy`.
2. Commit to `main` with message `Simulate failing quality gate`.
3. In **Actions**, open the red workflow and expand **Run automated tests**.
4. Observe `AssertionError: 'Unhealthy' != 'Healthy'`. **Deploy website** is skipped.
5. Refresh the live Pages website. It must still show `Healthy` (last good release).
6. Fix the status text to `Healthy`; change `v1.1` to `v1.2`; commit.
7. Confirm green tests and the live website displays `v1.2`.
8. Record both the failed and recovered run URLs.

## Exercise 3 - CD and recovery (35-50 min)
1. In `site/index.html` change only the version `v1.2` to `v2.0` and commit `Release version 2.0`.
2. Open **Actions**, confirm both jobs succeeded, and open your live site. It should show `v2.0`.
3. In the successful run, download **website-build** artifact and inspect its `index.html` and `build-info.json`.
4. Roll back manually: edit the same `site/index.html` version line from `v2.0` back to `v1.2`. Commit `Rollback to last known good v1.2`.
5. Confirm another successful workflow and that the live site again displays `v1.2`.
6. Note: this is a **manual redeploy of earlier website content**. It is not native AWS CodeDeploy automatic rollback.
7. Record the `v2.0` and rollback run URLs and screenshots.

## Evidence checklist
- Exercise 1: commit and successful triggered workflow, Pages URL showing v1.1.
- Exercise 2: failed test log + skipped deployment, followed by recovery.
- Exercise 3: website-build artifact, successful v2.0 deployment and v1.2 recovery.

## Troubleshooting
- No new workflow: edit files under `site/`, not README; check Actions enabled and branch is `main`.
- CI fails with test error: set status content back to exact `Healthy`.
- Pages deploy fails: verify **Settings > Pages > Source: GitHub Actions** and repository permissions.
- 404 or old version: look for Pages site URL in deployment job and allow propagation; hard refresh.
- Repo not public: on GitHub Free, GitHub Pages requires a public repository. Never upload private code or secrets.
