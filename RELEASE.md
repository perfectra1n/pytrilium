# Release Process

This document describes the automated release process for PyTrilium.

## Overview

PyTrilium uses GitHub Actions for automated releases that:
- ✅ Run comprehensive tests across Python 3.7-3.11
- ✅ Verify code formatting and import order
- ✅ Check version consistency across files
- ✅ Build and publish to PyPI
- ✅ Create GitHub releases with changelogs
- ✅ Upload wheel and source distributions

## Quick Release

1. **Update version** using the helper script:
   ```bash
   python scripts/bump_version.py 1.3.2 --create-tag --push-tag
   ```

2. **Push to trigger release**:
   ```bash
   git push origin main
   ```

3. **That's it!** The GitHub Action will automatically:
   - Test the code
   - Build packages
   - Publish to PyPI
   - Create GitHub release

## Manual Release Process

If you prefer manual control:

### 1. Update Version Numbers

Update the version in both places:
- `pyproject.toml`: `version = "1.3.2"`
- `pytrilium/PyTriliumClient.py`: `"pytrilium/1.3.2"`

Or use the script:
```bash
python scripts/bump_version.py 1.3.2  # Updates files only
```

### 2. Commit Changes

```bash
git add .
git commit -m "bump: version 1.3.2"
git push origin main
```

### 3. Create and Push Tag

```bash
git tag -a v1.3.2 -m "Release v1.3.2"
git push origin v1.3.2
```

### 4. GitHub Action Takes Over

The release workflow automatically triggers on tag push and handles:
- Testing across Python versions
- Package building
- PyPI publishing
- GitHub release creation

## Version Management Script

The `scripts/bump_version.py` script helps manage versions:

```bash
# Update version numbers only
python scripts/bump_version.py 1.3.2

# Update versions and create git tag
python scripts/bump_version.py 1.3.2 --create-tag

# Update versions, create and push git tag
python scripts/bump_version.py 1.3.2 --create-tag --push-tag

# Preview changes without making them
python scripts/bump_version.py 1.3.2 --dry-run
```

## GitHub Secrets Setup

For the release process to work, ensure these secrets are configured in your GitHub repository:

### Required Secrets

1. **`PYPI_API_TOKEN`** - PyPI API token for publishing
   - Go to https://pypi.org/manage/account/token/
   - Create a new token with scope for this project
   - Add as repository secret

2. **`GITHUB_TOKEN`** - Automatically provided by GitHub
   - Used for creating releases
   - No setup required

### Optional: Trusted Publishing (Recommended)

For better security, set up PyPI trusted publishing:

1. Go to your PyPI project settings
2. Add GitHub as a trusted publisher:
   - Repository: `perfectra1n/pytrilium`
   - Workflow: `release.yml`
   - Environment: (leave empty)

Then remove the `password` line from the PyPI publish step in `release.yml`.

## Workflow Files

- **`.github/workflows/release.yml`** - Main release workflow
- **`.github/workflows/test.yml`** - PR/push testing
- **`.github/workflows/main.yml`** - Deprecated (kept for reference)

## Release Checklist

Before releasing:

- [ ] All tests pass locally
- [ ] Version numbers are consistent
- [ ] README examples work with new version
- [ ] New features are documented
- [ ] Breaking changes are noted

The GitHub Actions will verify most of these automatically.

## Troubleshooting

### Version Mismatch Errors

If you see version mismatch errors, ensure both files have the same version:
- `pyproject.toml`
- `pytrilium/PyTriliumClient.py`

Use the version script to fix: `python scripts/bump_version.py X.Y.Z`

### PyPI Upload Failures

1. Check `PYPI_API_TOKEN` secret is set correctly
2. Ensure token has correct permissions
3. Consider setting up trusted publishing

### GitHub Release Fails

1. Ensure `GITHUB_TOKEN` permissions are correct
2. Check repository settings allow Actions to create releases

## Development Dependencies

Install development tools:

```bash
pip install -e ".[dev]"
```

This installs: black, isort, flake8, pytest, build, twine