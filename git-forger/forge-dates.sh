python3 date-generator.py
rm dummy
git init

while IFS= read -r line; do
    echo test >> dummy
    git add . 
    git commit -m "test_commit" --date="$line"
done < dates
