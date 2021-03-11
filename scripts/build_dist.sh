rm -r ../build/
rm -r ../dist/
cd ..
pipenv run pyinstaller ./__main__.spec --onefile
cp -r ./resources/ ./dist/resources/
rm -r ./scripts/Output
mkdir ./scripts/Output
pipenv run python -m zipfile -c ./scripts/Output/ward.zip ./dist/panelcontrol