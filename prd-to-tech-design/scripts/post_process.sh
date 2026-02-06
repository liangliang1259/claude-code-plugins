#!/bin/bash

# post_process.sh - Post-process generated technical design document
# This hook is called after writing the technical design document

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get file path from arguments
FILE_PATH="$1"

echo -e "${BLUE}🔧 Post-processing technical design document...${NC}"

# Check if file exists
if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File not found: $FILE_PATH"
    exit 1
fi

# Get directory and filename
DIR=$(dirname "$FILE_PATH")
FILENAME=$(basename "$FILE_PATH")
BASENAME="${FILENAME%.*}"
EXTENSION="${FILENAME##*.}"

# Step 1: Create backup copy
BACKUP_PATH="${DIR}/${BASENAME}_backup_$(date +%Y%m%d_%H%M%S).${EXTENSION}"
cp "$FILE_PATH" "$BACKUP_PATH"
echo -e "${GREEN}✓${NC} Created backup: $BACKUP_PATH"

# Step 2: Add metadata header if not present
TEMP_FILE="${FILE_PATH}.tmp"

if ! grep -q "生成时间" "$FILE_PATH"; then
    {
        echo "<!-- 自动生成的技术设计文档 -->"
        echo "<!-- 生成时间: $(date '+%Y-%m-%d %H:%M:%S') -->"
        echo "<!-- 工具: PRD to Tech Design Plugin -->"
        echo ""
        cat "$FILE_PATH"
    } > "$TEMP_FILE"
    mv "$TEMP_FILE" "$FILE_PATH"
    echo -e "${GREEN}✓${NC} Added metadata header"
fi

# Step 3: Add table of contents if not present
if ! grep -q "## 目录" "$FILE_PATH" && ! grep -q "## Table of Contents" "$FILE_PATH"; then
    echo -e "${BLUE}📑 Generating table of contents...${NC}"

    # Extract headers (## level 2 headers)
    TOC="## 目录\n\n"

    while IFS= read -r line; do
        if [[ "$line" =~ ^##[[:space:]]([0-9]+\.)?[[:space:]](.+)$ ]]; then
            SECTION_NUM="${BASH_REMATCH[1]}"
            SECTION_NAME="${BASH_REMATCH[2]}"
            # Create anchor link (lowercase, replace spaces with hyphens)
            ANCHOR=$(echo "$SECTION_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd '[:alnum:]-')
            TOC="${TOC}- [${SECTION_NUM} ${SECTION_NAME}](#${ANCHOR})\n"
        fi
    done < "$FILE_PATH"

    # Insert TOC after the title
    awk -v toc="$TOC" '
        /^# / && !inserted {
            print
            print ""
            printf "%s", toc
            print ""
            inserted=1
            next
        }
        {print}
    ' "$FILE_PATH" > "$TEMP_FILE"

    mv "$TEMP_FILE" "$FILE_PATH"
    echo -e "${GREEN}✓${NC} Added table of contents"
fi

# Step 4: Format code blocks (ensure proper spacing)
sed -i.bak '/```/s/^[[:space:]]*//' "$FILE_PATH"
rm -f "${FILE_PATH}.bak"
echo -e "${GREEN}✓${NC} Formatted code blocks"

# Step 5: Validate Mermaid syntax (basic validation)
echo -e "${BLUE}🔍 Validating Mermaid diagrams...${NC}"

MERMAID_ERRORS=0
IN_MERMAID=0
LINE_NUM=0

while IFS= read -r line; do
    ((LINE_NUM++))

    if [[ "$line" =~ ^\`\`\`mermaid ]]; then
        IN_MERMAID=1
        continue
    fi

    if [[ "$line" =~ ^\`\`\`$ ]] && [ "$IN_MERMAID" -eq 1 ]; then
        IN_MERMAID=0
        continue
    fi

    if [ "$IN_MERMAID" -eq 1 ]; then
        # Check for common Mermaid syntax errors
        if [[ "$line" =~ ^[[:space:]]*$ ]]; then
            continue  # Skip empty lines
        fi

        # Check for valid diagram type on first line
        if [[ "$line" =~ ^[[:space:]]*(graph|flowchart|sequenceDiagram|classDiagram|erDiagram|gantt|pie|journey|gitGraph) ]]; then
            continue
        fi

        # Check for valid node/edge syntax
        if [[ "$line" =~ (-->|---|==|\.\.>|\-\.\->|\[|\]|\(|\)|\{|\}) ]]; then
            continue
        fi

        # If line doesn't match any valid pattern, it might be an error
        if [[ ! "$line" =~ ^[[:space:]]*(%%|title|section|dateFormat|axisFormat) ]]; then
            echo -e "${YELLOW}⚠${NC} Potential Mermaid syntax issue at line $LINE_NUM: $line"
            ((MERMAID_ERRORS++))
        fi
    fi
done < "$FILE_PATH"

if [ "$MERMAID_ERRORS" -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Mermaid diagrams validated"
else
    echo -e "${YELLOW}⚠${NC} Found $MERMAID_ERRORS potential Mermaid syntax issues"
fi

# Step 6: Add document statistics
echo -e "${BLUE}📊 Generating document statistics...${NC}"

WORD_COUNT=$(wc -w < "$FILE_PATH" | tr -d ' ')
LINE_COUNT=$(wc -l < "$FILE_PATH" | tr -d ' ')
SECTION_COUNT=$(grep -c "^## " "$FILE_PATH" || true)
MERMAID_COUNT=$(grep -c '```mermaid' "$FILE_PATH" || true)

STATS_COMMENT="<!-- 文档统计: 字数=$WORD_COUNT, 行数=$LINE_COUNT, 章节数=$SECTION_COUNT, 图表数=$MERMAID_COUNT -->"

# Add stats comment at the end if not present
if ! grep -q "文档统计" "$FILE_PATH"; then
    echo "" >> "$FILE_PATH"
    echo "$STATS_COMMENT" >> "$FILE_PATH"
    echo -e "${GREEN}✓${NC} Added document statistics"
fi

# Step 7: Create a summary file
SUMMARY_FILE="${DIR}/${BASENAME}_summary.txt"
{
    echo "Technical Design Document Summary"
    echo "=================================="
    echo ""
    echo "File: $FILENAME"
    echo "Generated: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    echo "Statistics:"
    echo "  - Word count: $WORD_COUNT"
    echo "  - Line count: $LINE_COUNT"
    echo "  - Sections: $SECTION_COUNT"
    echo "  - Mermaid diagrams: $MERMAID_COUNT"
    echo ""
    echo "Sections:"
    grep "^## " "$FILE_PATH" | sed 's/^##/  -/'
    echo ""
    echo "Backup: $BACKUP_PATH"
} > "$SUMMARY_FILE"

echo -e "${GREEN}✓${NC} Created summary file: $SUMMARY_FILE"

# Final summary
echo ""
echo "========================================="
echo "Post-processing Complete"
echo "========================================="
echo -e "Document: ${GREEN}$FILE_PATH${NC}"
echo -e "Backup:   ${BLUE}$BACKUP_PATH${NC}"
echo -e "Summary:  ${BLUE}$SUMMARY_FILE${NC}"
echo ""
echo -e "${GREEN}✅ Post-processing completed successfully!${NC}"

exit 0
