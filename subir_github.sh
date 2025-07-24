#!/bin/bash
# Mostrar los cambios que se van a subir
echo " Cambios detectados:"
git status

# Preguntar si quiere continuar
read -p "¿Querés subir estos cambios? (s/n): " confirmacion
if [[ "$confirmacion" != "s" && "$confirmacion" != "S" ]]; then
    echo " Subida cancelada."
    exit 0
fi

read -p "ingresa un mensaje para el Commit: " mensaje

# Si no se escribe nada, se cancela
if [ -z "$mensaje" ]; then
    echo " Commit cancelado: el mensaje esta vacío."
    exit 1
fi

# Ejecutar los comandos Git
git add .
git commit -m "$mensaje"
git push

