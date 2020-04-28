files=$(ls *.py)

echo "Monitoring..."
echo "$files"

while true; do
  inotifywait -qq -e close_write $files
  clear
  pytest
done
