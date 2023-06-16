import whisper
import moviepy.editor as mp
import speech_recognition as sr
import argparse
import tempfile
import os

def escribir_archivo_texto(texto, nombre_archivo):
    archivo = open(nombre_archivo, 'a' if os.path.exists(nombre_archivo) else 'w')
    archivo.write(texto+'\n')
    archivo.close()

def obtener_archivos_de_directorio(directorio, extensiones):
    archivos_directorio = os.listdir(directorio)
    archivos_video = [os.path.join(directorio, archivo) for archivo in archivos_directorio if es_archivo_video(os.path.join(directorio, archivo), extensiones)]
    return archivos_video

def es_archivo_video(ruta_archivo, extensiones):
    _, extension = os.path.splitext(ruta_archivo)
    return extension.lower() in extensiones

def pasar_a_audio(video_path):
    print("Extrayendo audio del video: ", video_path)
    video = mp.VideoFileClip(video_path)
    audio = video.audio
    archivo_temporal = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    audio.write_audiofile(archivo_temporal.name)
    archivo_temporal.close()
    return archivo_temporal.name

def pasar_audio_a_texto(model, audio_path):
    model = whisper.load_model(model)
    print("Procesando texto del video ", audio_path )
    text = model.transcribe(audio_path)
    return text

#transcribe -i /path/to/input.wav -o /path/to/output.json -m base
def main():
    parser = argparse.ArgumentParser()
    #banderas sin parametros 
    parser.add_argument("-v", "--video", action="store_true", help="Archivo de entrada es video")
    parser.add_argument("-a", "--audio", action="store_true", help="Archivo de entrada es audio")
    parser.add_argument('-d', "--directory", action="store_true", help="Archivo de entrada es un directorio")
    
    #banderas con parametros
    parser.add_argument("-i", "--input", type=str, help="Especificar la ruta del archivo de audio")
    parser.add_argument("-m", "--model", type=str, help="Especificar el modelo a utilizar (Tiny, Base, Small, Medium, Large)")

    args = parser.parse_args()
    _input = args.input
    _model = args.model

    if _input is None:
        print("Debe especificar la ruta del archivo de entrada")
        return
    if _model is None:
        print("Debe especificar el modelo a utilizar")
        return

    #si es un directorio y contiene videos
    if args.directory and args.video:
        extensiones_video = ['.mp4', '.avi', '.mkv', '.mov']  # Extensiones de video admitidas
        archivos = obtener_archivos_de_directorio(_input, extensiones_video)
        os.makedirs('./output', exist_ok=True)
  
        for archivo in archivos:
            audio = pasar_a_audio(archivo)
            text = pasar_audio_a_texto(_model, audio)
            _output = './output/'+os.path.splitext(os.path.basename(archivo))[0]+'.txt'
            escribir_archivo_texto(text['text'], _output)

        print("Proceso finalizado. Archivo de salida: ", _output)
        return

    #si es un directorio y contiene audios
    if args.directory and args.audio:
        extensiones_audio = ['.mp3', '.wav']  # Extensiones de audio admitidas
        archivos = obtener_archivos_de_directorio(_input, extensiones_audio)
        #recorrer archivos
        os.makedirs('./output', exist_ok=True)
        for archivo in archivos:
            text = pasar_audio_a_texto(_model, archivo)
            _output = './output/'+os.path.splitext(os.path.basename(archivo))[0]+'.txt'
            escribir_archivo_texto(text['text'], _output)

        print("Proceso finalizado. Archivo de salida: ", _output)
        return

    if args.video:
        audio_path = pasar_a_audio(_input)
        text = pasar_audio_a_texto(_model, audio_path)
        _output = './'+os.path.splitext(os.path.basename(_input))[0]+'.txt'
        escribir_archivo_texto(text['text'], _output)
        print("Proceso finalizado. Archivo de salida: ", _output)
        return
    
    if args.audio:
        text = pasar_audio_a_texto(_model, _input)
        _output = './'+os.path.splitext(os.path.basename(_input))[0]+'.txt'
        escribir_archivo_texto(text['text'], _output)
        print("Proceso finalizado. Archivo de salida: ", _output)
        return


#llamar funcion main
if __name__ == "__main__":
    main()
