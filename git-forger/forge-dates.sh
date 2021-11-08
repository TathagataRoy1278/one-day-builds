python3 date-generator.py
rm dummy

while IFS= read -r line; do
    echo test >> dummy
    git add . 
    git commit -m "test_commit" --date="$line"
done < dates
