#!pip install jsonlines
#!pip install pandas
#!pip install transformers
#!pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
import jsonlines 
import pandas as pd
from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
from tqdm.auto import tqdm
rutas = ["/home/santiago/LanAn/aguadiana4-3_tweetsResCont.txt", "/home/santiago/LanAn/aguadiana6-4_tweetsResCont.txt", "/home/santiago/LanAn/manolojim4-3_tweetsResCont.txt", 
        "/home/santiago/LanAn/manolojim6-4_tweetsResCont.txt", "/home/santiago/LanAn/manolojim6-5_tweetsResCont.txt", "/home/santiago/LanAn/RicardoMeb6-4_tweetsResCont.txt", "/home/santiago/LanAn/leninperezr4-3_tweetsResCont.txt",
         "/home/santiago/LanAn/leninperezr6-4_tweetsResCont.txt", "/home/santiago/LanAn/leninperezr6-5_tweetsResCont.txt", "/home/santiago/LanAn/AlejandraDMV4-3_tweetsResCont.txt", "/home/santiago/LanAn/AlejandraDMV6-4_tweetsResCont.txt", 
        "/home/santiago/LanAn/delfinagomeza4-3_tweetsResCont.txt", "/home/santiago/LanAn/delfinagomeza6-4_tweetsResCont.txt", "/home/santiago/LanAn/delfinagomeza6-5_tweetsResCont.txt"]
df = pd.DataFrame()
for ruta in rutas:
    df = pd.concat([df, pd.read_json(ruta, lines=True)], ignore_index=True)
#df
model_path = "daveni/twitter-xlm-roberta-emotion-es" #pensar otro modelo
emotion_analysis = pipeline("text-classification", framework="pt", model=model_path, tokenizer=model_path)

buffer = StringIO()
for i, row in df.iterrows():
    contenido = row
    result = emotion_analysis(row["rawContent"])
    print(result, file=buffer)

# Guardar el contenido del buffer en un archivo CSV
buffer.seek(0)  # Reiniciar el puntero del buffer al principio
resultados_csv = pd.read_csv(buffer, delimiter=",")

# Guardar el DataFrame en un archivo CSV
ruta_archivo = "/home/santiago/LanAn/resultados.csv"
resultados_csv.to_csv(ruta_archivo, index=False)
  
