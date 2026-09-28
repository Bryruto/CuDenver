#!/bin/bash
n=$1
shift
files=("$@")
echo "Number of Files: ${#files[@]}"
echo "Processing: ${files[*]}"
for file in "${files[@]}"; do
    echo "===($(wc -l -w -m "$file" | awk '{print $1, $2, $3, $4}'))==="
    grep -oE '[a-zA-Z]+' "$file" |tr '[:upper:]' '[:lower:]'|sort |uniq -c|sort -nr |head -n "$n"
done
echo "===done==="
