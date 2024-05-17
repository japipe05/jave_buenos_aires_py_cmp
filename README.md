# Instalacion
docker-compose up -d

# Subir archivos pesados 
git lfs install
git lfs track "*.gl.html"
git lfs push --all origin main
git add .
git commit -m "carga pureba"
git push

# traer a local
git checkout main 
git fetch origin main 
git merge origin/main

# subir
git add . 
git commit -m "cargue1" 
git push