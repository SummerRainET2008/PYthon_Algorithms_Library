# Change version
# add __init__ in each folder
rm -r dist 
python3 -m build

python3 -m twine upload --repository pypi dist/*
