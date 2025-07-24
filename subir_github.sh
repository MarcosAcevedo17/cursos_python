#!/bin/bash


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

