import streamlit as st
import tensorflow_hub as hub
import librosa
import numpy as np

# Загрузка предобученной модели YAMNet
@st.cache(allow_output_mutation=True)
def load_model():
    return hub.load('https://tfhub.dev/google/yamnet/1')

model = load_model()

def classify_sound(file):
    try:
        # Загрузка аудиофайла
        audio, sr = librosa.load(file, sr=16000)  # Загружаем файл с частотой дискретизации 16 kHz
        audio = np.asarray(audio, dtype=np.float32).flatten()  # Убедимся, что формат float32

        # Проверка на пустой массив
        if len(audio) == 0:
            raise ValueError("Файл аудио пустой или не поддерживается.")

        # Передача данных в модель
        scores, embeddings, spectrogram = model(audio)

        # Загрузка классов из YAMNet
        class_map_path = model.class_map_path().numpy().decode('utf-8')
        class_names = np.genfromtxt(class_map_path, delimiter=',', dtype=str, usecols=0)

        # Если размер class_names больше выходов модели, обрезаем
        if len(class_names) > scores.shape[1]:
            class_names = class_names[:scores.shape[1]]

        # Определение топового класса
        top_class_index = np.argmax(scores[0])
        top_class_name = class_names[top_class_index] if top_class_index < len(class_names) else "Unknown sound"
        top_score = scores.numpy()[0, top_class_index]  # Уверенность
        
        return top_class_name, top_score
    
    except Exception as e:
        st.error(f"Произошла ошибка при обработке файла: {e}")
        return None, None


# Интерфейс приложения
st.title("WildSound: Анализ звуков природы")
st.write("Загрузите аудиофайл и узнайте, какие звуки природы обнаружены!")

# Загрузка аудиофайла через интерфейс
uploaded_file = st.file_uploader("Выберите аудиофайл (.wav)", type=["wav"])

if uploaded_file is not None:
    try:
        # Классификация звука
        class_name, confidence = classify_sound(uploaded_file)
        st.write(f"**Обнаруженный звук:** {class_name}")
        st.write(f"**Уверенность:** {confidence:.2f}")
    except Exception as e:
        st.error(f"Произошла ошибка при обработке файла: {e}")
