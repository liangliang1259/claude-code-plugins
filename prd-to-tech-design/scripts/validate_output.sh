#!/bin/bash

# validate_output.sh - Validate technical design document before writing
# This hook is called before writing the generated technical design document

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get file path and content from arguments
FILE_PATH="$1"
CONTENT="$2"

echo "🔍 Validating technical design document..."

# Validation counters
ERRORS=0
WARNINGS=0

# Check 1: File has .md extension
if [[ ! "$FILE_PATH" =~ \.md$ ]]; then
    echo -e "${RED}❌ Error: File must have .md extension${NC}"
    ((ERRORS++))
fi

# Check 2: Content is not empty
if [ -z "$CONTENT" ]; then
    echo -e "${RED}❌ Error: Content is empty${NC}"
    ((ERRORS++))
    exit 1
fi

CONTENT_LENGTH=${#CONTENT}
if [ "$CONTENT_LENGTH" -lt 500 ]; then
    echo -e "${RED}❌ Error: Content is too short (${CONTENT_LENGTH} chars, minimum 500)${NC}"
    ((ERRORS++))
fi

# Check 3: Contains required sections (8 sections)
REQUIRED_SECTIONS=(
    "功能概述"
    "技术栈选型"
    "核心模块设计"
    "数据库设计"
    "API设计"
    "部署架构"
    "风险评估"
    "开发计划"
)

echo "Checking for required sections..."
for section in "${REQUIRED_SECTIONS[@]}"; do
    if echo "$CONTENT" | grep -q "$section"; then
        echo -e "${GREEN}✓${NC} Found section: $section"
    else
        echo -e "${RED}✗${NC} Missing section: $section"
        ((ERRORS++))
    fi
done

# Check 4: Contains at least 3 Mermaid diagrams
MERMAID_COUNT=$(echo "$CONTENT" | grep -c '```mermaid' || true)
if [ "$MERMAID_COUNT" -ge 3 ]; then
    echo -e "${GREEN}✓${NC} Found $MERMAID_COUNT Mermaid diagrams (minimum 3)"
else
    echo -e "${YELLOW}⚠${NC} Warning: Only found $MERMAID_COUNT Mermaid diagrams (recommended: at least 3)"
    ((WARNINGS++))
fi

# Check 5: All sections have content (not just headers)
echo "Checking section content..."
EMPTY_SECTIONS=0

# Extract sections and check if they have content
while IFS= read -r line; do
    if [[ "$line" =~ ^##[[:space:]] ]]; then
        SECTION_NAME=$(echo "$line" | sed 's/^##[[:space:]]*//')
        # Check if next non-empty line after this header is another header
        NEXT_CONTENT=$(echo "$CONTENT" | awk "/$SECTION_NAME/{flag=1; next} flag && /^##[[:space:]]/{exit} flag && NF{print; exit}")
        if [ -z "$NEXT_CONTENT" ]; then
            echo -e "${YELLOW}⚠${NC} Warning: Section '$SECTION_NAME' appears to be empty"
            ((EMPTY_SECTIONS++))
        fi
    fi
done <<< "$CONTENT"

if [ "$EMPTY_SECTIONS" -gt 0 ]; then
    echo -e "${YELLOW}⚠${NC} Warning: Found $EMPTY_SECTIONS empty sections"
    ((WARNINGS++))
fi

# Check 6: Document has a title
if echo "$CONTENT" | head -n 5 | grep -q "^# "; then
    echo -e "${GREEN}✓${NC} Document has a title"
else
    echo -e "${YELLOW}⚠${NC} Warning: Document may be missing a title"
    ((WARNINGS++))
fi

# Check 7: Validate Mermaid syntax (basic check)
if [ "$MERMAID_COUNT" -gt 0 ]; then
    echo "Validating Mermaid diagram syntax..."

    # Check for common diagram types in the content
    if echo "$CONTENT" | grep -qE '(graph|flowchart|sequenceDiagram|classDiagram|erDiagram|gantt)'; then
        echo -e "${GREEN}✓${NC} Mermaid diagrams have valid diagram types"
    else
        echo -e "${YELLOW}⚠${NC} Warning: Mermaid diagrams may have invalid syntax"
        ((WARNINGS++))
    fi
fi

# Summary
echo ""
echo "========================================="
echo "Validation Summary"
echo "========================================="
echo -e "Errors:   ${RED}$ERRORS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

if [ "$ERRORS" -gt 0 ]; then
    echo -e "${RED}❌ Validation failed with $ERRORS error(s)${NC}"
    echo "Please fix the errors before proceeding."
    exit 1
elif [ "$WARNINGS" -gt 0 ]; then
    echo -e "${YELLOW}⚠ Validation passed with $WARNINGS warning(s)${NC}"
    echo "Consider addressing the warnings for better quality."
    exit 0
else
    echo -e "${GREEN}✅ Validation passed successfully!${NC}"
    exit 0
fi
