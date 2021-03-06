# Release Process

- Get the Nox:
  - `pip install -U nox`
- Bump the version number to an even number in `b2sdk/version.py`.
- Update the release history in `README.md` by changing "not released yet" to the current date for this release.
- Run linters and tests:
  - `export B2_TEST_APPLICATION_KEY=your_app_key`
  - `export B2_TEST_APPLICATION_KEY_ID=your_app_key_id`
  - `nox -x`
- Build docs locally:
  - `nox --non-interactive -xs doc`
- Commit and push to GitHub, then wait for build to complete successfully.
  - No need to make a branch. Push straight to `master`.
- Tag in git and push tag to origin.  (Version tags look like "v0.4.6".)
    - `git tag vx.x.x`
    - `git push origin vx.x.x`
- Build the distribution and upload to PyPI.
  - `nox -xs build deploy`
- Install using pip and verify that it gets the correct version.
- Update for dev
  - Bump the version number to an odd number (for example: 1.0.2 -> 1.0.3)
  - Add a "not released yet" section in the release history, like: 0.8.5 (not released yet)
  - Commit the changes
- Push to GitHub again.
