#!/bin/bash
#Insertar las respuestas en los archivos de texto de cada usuario
usuarios=('AlejandraDMV' 'delfinagomeza' 'RicardoMeb' 'leninperezr' 'aguadiana' 'manolojim')
dias=("4-3" "6-4" "6-5")
for dia in "${dias[@]}"; do
    for usuario in "${usuarios[@]}"; do
        while IFS= read -r id_tweet; do
            snscrape --jsonl twitter-search "conversation_id:$id_tweet lang:es" >> "${usuario}${dia}_tweetsResCont.txt"
        done < "${usuario}${dia}IDS.txt"
    done
done                                  
