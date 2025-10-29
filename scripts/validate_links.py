#!/usr/bin/env python3
"""
Validator script for AEP markdown links.

This script validates that:
1. No markdown links point to .md files
2. All AEP references point to existing AEPs
3. Links follow the correct format
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Set


def find_aep_directories() -> Set[str]:
    """Find all AEP directories and return their numbers."""
    aep_dirs = set()
    aep_path = Path("aep/general")

    if not aep_path.exists():
        print(f"Error: {aep_path} directory not found")
        sys.exit(1)

    for item in aep_path.iterdir():
        if item.is_dir() and item.name.isdigit():
            aep_dirs.add(item.name)

    return aep_dirs


def find_markdown_links(content: str) -> List[Tuple[int, str, str]]:
    """Find all markdown links in content and return (line_number, link_text, url)."""
    links = []
    lines = content.split('\n')

    # Pattern to match markdown links: [text](url)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    for line_num, line in enumerate(lines, 1):
        matches = link_pattern.findall(line)
        for link_text, url in matches:
            links.append((line_num, link_text, url))

    return links


def is_aep_reference(url: str) -> bool:
    """Check if a URL is an AEP reference."""
    # Match patterns like /0001, ./0001, /0121, etc.
    aep_pattern = re.compile(r'^\.?/(\d+)$')
    return bool(aep_pattern.match(url))


def validate_file(file_path: Path, existing_aeps: Set[str]) -> List[str]:
    """Validate a single markdown file and return list of errors."""
    errors = []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Error reading {file_path}: {e}")
        return errors

    links = find_markdown_links(content)

    for line_num, link_text, url in links:
        # Check for .md suffix (but exclude external GitHub links)
        if url.endswith('.md') and not url.startswith('https://github.com/'):
            errors.append(f"{file_path}:{line_num}: Link '{link_text}' points to .md file: {url}")

        # Check AEP references
        if is_aep_reference(url):
            # Extract AEP number
            match = re.match(r'^\.?/(\d+)$', url)
            if match:
                aep_num = match.group(1)
                if aep_num not in existing_aeps:
                    errors.append(f"{file_path}:{line_num}: Link '{link_text}' references non-existent AEP: {url}")

    return errors


def main():
    """Main validation function."""
    print("Validating AEP markdown links...")

    # Find all existing AEPs
    existing_aeps = find_aep_directories()
    print(f"Found {len(existing_aeps)} existing AEPs: {sorted(existing_aeps)}")

    # Find all markdown files
    aep_path = Path("aep/general")
    markdown_files = list(aep_path.rglob("*.md.j2"))

    print(f"Found {len(markdown_files)} markdown files to validate")

    all_errors = []

    for file_path in markdown_files:
        errors = validate_file(file_path, existing_aeps)
        all_errors.extend(errors)

    # Report results
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} validation errors:")
        for error in all_errors:
            print(f"  {error}")
        sys.exit(1)
    else:
        print("\n✅ All links are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()