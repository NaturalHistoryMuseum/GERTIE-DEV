#!/bin/bash
# GERTIE Enhancement Validation Script

echo "========================================="
echo "GERTIE ENHANCEMENT VALIDATION"
echo "========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check feature flags
echo "Checking Feature Flags..."
echo "--------------------------"
for flag in USE_NEW_GERTIE USE_UNIFIED_CONFIG USE_JSONRPC USE_ANSIBLE USE_WEBSOCKETS; do
    value=${!flag:-false}
    if [ "$value" = "false" ]; then
        echo -e "${GREEN}✓${NC} $flag = false (safe)"
    else
        echo -e "${YELLOW}!${NC} $flag = $value (active)"
    fi
done

echo ""
echo "Checking Enhancement Files..."
echo "-----------------------------"


# Check if enhancement directories exist
for dir in config gertie deployment .quality docs; do
    if [ -d "$dir" ]; then
        echo -e "${GREEN}✓${NC} Directory $dir exists"
    else
        echo -e "${RED}✗${NC} Directory $dir missing"
    fi
done

echo ""
echo "Checking Key Files..."
echo "--------------------"

# Check key files
files=(
    "config/unified_config.py"
    "gertie/feature_flags.py"
    "gertie/shared/protocol.py"
    "deployment/inventory.ini"
    ".quality/ruff.toml"
    "pyproject.toml"
    "docs/MIGRATION_GUIDE.md"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $file"
    else
        echo -e "${RED}✗${NC} $file missing"
    fi
done

echo ""
echo "Testing Python Imports..."
echo "------------------------"

# Test imports with all flags false
export USE_NEW_GERTIE=false
export USE_UNIFIED_CONFIG=false
export USE_JSONRPC=false

python3 -c "from gertie.feature_flags import FeatureFlags; print('✓ Feature flags import OK')" 2>/dev/null || echo "✗ Feature flags import failed"
python3 -c "from config.unified_config import UnifiedConfig; print('✓ Unified config import OK')" 2>/dev/null || echo "✗ Unified config import failed"
python3 -c "from gertie.shared.protocol import JSONRPCMessage; print('✓ Protocol import OK')" 2>/dev/null || echo "✗ Protocol import failed"

echo ""
echo "Git Status..."
echo "------------"
git log --oneline -6 | grep -E "Stage E[1-6]" || echo "No enhancement commits found"

echo ""
echo "========================================="
echo "Validation Complete"
echo ""
echo "Next Steps:"
echo "1. Test with current system (all flags false)"
echo "2. Enable individual flags for testing"
echo "3. Deploy using sync_to_slaves.sh"
echo "========================================="
