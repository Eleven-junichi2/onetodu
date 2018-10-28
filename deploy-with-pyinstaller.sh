rm -r "dist/"
LD_LIBRARY_PATH=~/.pyenv/versions/3.7.0/lib python -m PyInstaller --name onetodu -F onetodu/main.py
cp -v "onetodu/onetodu.kv" "dist/"
cp -v -r "onetodu/images/" "dist/images/"
cp -v -r "onetodu/fonts/" "dist/fonts/"
