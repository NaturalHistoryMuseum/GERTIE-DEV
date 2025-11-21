# GERTIE Enhancement Migration Guide

## Overview
This guide documents the code review enhancements implemented in Stages E1-E6.
All changes are **non-breaking** and **feature-flag protected**.

## Feature Flags (All Default to FALSE)
```bash
export USE_NEW_GERTIE=false      # New package structure
export USE_UNIFIED_CONFIG=false  # Centralized configuration
export USE_JSONRPC=false         # JSON-RPC protocol
export USE_ANSIBLE=false         # Ansible deployment supplement
export USE_WEBSOCKETS=false      # WebSocket communication (future)
```

## Enhancement Stages

### Stage E1: Parallel Configuration System
- **Location**: `config/unified_config.py`
- **Purpose**: Centralized configuration management
- **Activation**: Set `USE_UNIFIED_CONFIG=true`
- **Rollback**: `git revert f65fb62`

### Stage E2: Package Structure
- **Location**: `gertie/` directory
- **Purpose**: Modern Python package organization
- **Activation**: Set `USE_NEW_GERTIE=true`
- **Rollback**: `git revert d655a87`


### Stage E3: JSON-RPC Protocol Bridge
- **Location**: `gertie/shared/protocol.py`, `gertie/shared/protocol_bridge.py`
- **Purpose**: Modern message protocol with backward compatibility
- **Activation**: Set `USE_JSONRPC=true`
- **Rollback**: `git revert cc86604`

### Stage E4: Ansible Deployment Supplement
- **Location**: `deployment/` directory
- **Purpose**: Enhanced deployment capabilities (supplements sync_to_slaves.sh)
- **Activation**: Set `USE_ANSIBLE=true` and run `deployment/run_ansible_supplement.sh`
- **Rollback**: `git revert b97c141`
- **Note**: sync_to_slaves.sh remains the primary deployment method

### Stage E5: Code Quality Tools
- **Location**: `.quality/`, `pyproject.toml`, `.pre-commit-config.yaml`
- **Purpose**: Automated code quality checking
- **Activation**: Run `.quality/check_quality.sh` for assessment
- **Rollback**: `git revert 92f605e`

### Stage E6: Validation & Documentation
- **Location**: `docs/` directory
- **Purpose**: Consolidated documentation and validation
- **Status**: Current stage

## Testing Progression

1. **Baseline Test** (all flags FALSE)
   ```bash
   ./run_gui_with_logging.sh  # Should work exactly as before
   ```

2. **Individual Flag Testing**
   ```bash
   export USE_UNIFIED_CONFIG=true
   # Test configuration loading
   
   export USE_JSONRPC=true
   # Test protocol translation
   ```

3. **Combined Testing** (after individual validation)
   ```bash
   export USE_NEW_GERTIE=true
   export USE_UNIFIED_CONFIG=true
   export USE_JSONRPC=true
   ```

## Deployment Remains Unchanged
Primary deployment method: **sync_to_slaves.sh**
```bash
./sync_to_slaves.sh  # Always use this for deployment
```

## Rollback Procedures

### Full Rollback (all enhancements)
```bash
git revert HEAD~5  # Reverts E6, E5, E4, E3, E2, E1
```

### Selective Rollback
```bash
git revert <commit>  # See stage-specific commits above
```

## Support
- Session logs: `/Users/andrew1/Desktop/GERTIE_SESSION_LOG.md`
- Reference code: `/Users/andrew1/Desktop/GOLDEN_REFERENCE_DO_NOT_TOUCH/`
