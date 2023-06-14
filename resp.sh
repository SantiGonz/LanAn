#!/bin/bash 
#Insertar las respuestas en los archivos de texto de cada usuario
usuarios=('AlejandraDMV' 'delfinagomeza' 'RicardoMeb' 'leninperezr' 'aguadiana' 'manolojim')

for usuario in "${usuarios[@]}"; do
    while IFS= read -r id_tweet; do
        snscrape --jsonl twitter-search "conversation_id:$id_tweet lang:es" >> "${usuario}_tweetsResp.txt"
    done < "${usuario}IDS.txt"
done


