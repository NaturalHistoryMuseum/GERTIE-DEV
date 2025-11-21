#!/bin/bash
# GERTIE Code Quality Check Script (Non-enforcing)

echo "========================================="
echo "GERTIE CODE QUALITY CHECK"
echo "========================================="
echo ""
echo "This script checks code quality but does NOT"
echo "enforce changes. Use for assessment only."
echo ""

# Check if ruff is installed
if command -v ruff &> /dev/null; then
    echo "Running Ruff linter check..."
    ruff check . --config .quality/ruff.toml --statistics
    echo ""
    echo "Running Ruff format check..."
    ruff format --check . --config .quality/ruff.toml
else
    echo "Ruff not installed. Install with: pip install ruff"
fi

echo ""
echo "========================================="
echo "Quality check complete (informational only)"
echo "No files were modified."
echo "========================================="
