rm -r ../build/
rm -r ../dist/
cd ..
pipenv run pyinstaller ./ward.spec --onefile
cp -r ../resources ./dist
mkdir ./scripts/Output
pipenv run python -m zipfile -c ./scripts/Output/ward.zip ./dist/ward.exe ./dist/resources