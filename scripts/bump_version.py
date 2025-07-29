#!/usr/bin/env python3
"""
Version management script for PyTrilium.
Updates version numbers across all files and optionally creates a git tag.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path


def get_current_version():
    """Get the current version from pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found. Run this script from the project root.")
        sys.exit(1)

    content = pyproject_path.read_text()
    match = re.search(r'version = "([^"]+)"', content)
    if not match:
        print("❌ Could not find version in pyproject.toml")
        sys.exit(1)

    return match.group(1)


def update_version_in_file(file_path, old_version, new_version, pattern):
    """Update version in a specific file using the given pattern."""
    if not Path(file_path).exists():
        print(f"⚠️  {file_path} not found, skipping")
        return False

    content = Path(file_path).read_text()
    old_content = content

    # Replace using the pattern
    content = re.sub(
        pattern.format(old_version=re.escape(old_version)),
        pattern.format(old_version=new_version).replace("{old_version}", new_version),
        content,
    )

    if content != old_content:
        Path(file_path).write_text(content)
        print(f"✅ Updated {file_path}")
        return True
    else:
        print(f"⚠️  No changes needed in {file_path}")
        return False


def update_all_versions(old_version, new_version):
    """Update version in all relevant files."""
    files_updated = []

    # Update pyproject.toml
    if update_version_in_file("pyproject.toml", old_version, new_version, r'version = "{old_version}"'):
        files_updated.append("pyproject.toml")

    # Update User-Agent in PyTriliumClient.py
    if update_version_in_file("pytrilium/PyTriliumClient.py", old_version, new_version, r"pytrilium/{old_version}"):
        files_updated.append("pytrilium/PyTriliumClient.py")

    return files_updated


def create_git_tag(version, push=False):
    """Create a git tag for the version."""
    tag_name = f"v{version}"

    try:
        # Check if tag already exists
        result = subprocess.run(["git", "tag", "-l", tag_name], capture_output=True, text=True)
        if tag_name in result.stdout:
            print(f"⚠️  Tag {tag_name} already exists")
            return False

        # Create the tag
        subprocess.run(["git", "tag", "-a", tag_name, "-m", f"Release {tag_name}"], check=True)
        print(f"✅ Created git tag {tag_name}")

        if push:
            subprocess.run(["git", "push", "origin", tag_name], check=True)
            print(f"✅ Pushed tag {tag_name} to origin")

        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create/push git tag: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Bump version numbers across PyTrilium files")
    parser.add_argument("new_version", help="New version number (e.g., 1.3.2)")
    parser.add_argument("--create-tag", action="store_true", help="Create a git tag after updating versions")
    parser.add_argument("--push-tag", action="store_true", help="Push the git tag to origin (implies --create-tag)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be changed without making changes")

    args = parser.parse_args()

    if args.push_tag:
        args.create_tag = True

    # Validate version format
    if not re.match(r"^\d+\.\d+\.\d+$", args.new_version):
        print(f"❌ Invalid version format: {args.new_version}")
        print("   Version should be in format: X.Y.Z (e.g., 1.3.2)")
        sys.exit(1)

    current_version = get_current_version()
    print(f"Current version: {current_version}")
    print(f"New version: {args.new_version}")

    if current_version == args.new_version:
        print("⚠️  New version is the same as current version")
        sys.exit(1)

    if args.dry_run:
        print("\n🔍 DRY RUN - No changes will be made")
        print(f"Would update version from {current_version} to {args.new_version} in:")
        print("  - pyproject.toml")
        print("  - pytrilium/PyTriliumClient.py")
        if args.create_tag:
            print(f"Would create git tag: v{args.new_version}")
        if args.push_tag:
            print(f"Would push git tag to origin")
        return

    # Update versions
    print(f"\n🔄 Updating version from {current_version} to {args.new_version}...")
    files_updated = update_all_versions(current_version, args.new_version)

    if not files_updated:
        print("❌ No files were updated")
        sys.exit(1)

    print(f"\n✅ Successfully updated {len(files_updated)} file(s)")

    # Create git tag if requested
    if args.create_tag:
        print(f"\n🏷️  Creating git tag...")
        create_git_tag(args.new_version, push=args.push_tag)

    print(f"\n🎉 Version bump complete!")
    print(f"📝 Don't forget to:")
    print(f"   1. Review and commit the changes")
    print(f"   2. Update the changelog/release notes")
    if not args.create_tag:
        print(
            f"   3. Create and push a git tag: git tag -a v{args.new_version} -m 'Release v{args.new_version}' && git push origin v{args.new_version}"
        )


if __name__ == "__main__":
    main()
