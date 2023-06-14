#!/bin/bash
#Insertar las respuestas en los archivos de texto de cada usuario
usuarios=('AlejandraDMV' 'delfinagomeza' 'RicardoMeb' 'leninperezr' 'aguadiana' 'manolojim')
dias=("4-3" "6-4" "6-5")

for dia in "${dias[@]}"; do
    for usuario in "${usuarios[@]}"; do
        while IFS= read -r id_tweet; do
            content=$(snscrape --jsonl twitter-search "conversation_id:$id_tweet lang:es" | jq -r '.content')
            if [[ ! -z "$content" ]]; then
                echo "$content" >> "${usuario}${dia}_tweetsResp.txt"
            fi
        done < "${usuario}${dia}IDS.txt"
    done
done
