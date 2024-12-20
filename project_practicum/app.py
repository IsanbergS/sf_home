import streamlit as st
import tensorflow_hub as hub
import librosa
import numpy as np
import csv
import time
import sounddevice as sd
import queue
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg

_lock = threading.Lock()

# Загрузка предобученной модели YAMNet
@st.cache_resource
def load_model():
    return hub.load('https://tfhub.dev/google/yamnet/1')

model = load_model()

# Загрузка классов из yamnet_class_map.csv
def load_class_map(file_path="project_practicum/yamnet_class_map.csv"):
    class_map = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                class_map.append(row['display_name'])  # Извлекаем только display_name
    except FileNotFoundError:
        st.error(f"Файл {file_path} не найден.")
    except KeyError:
        st.error(f"Проблема с форматом файла {file_path}. Проверьте, что он содержит колонки 'index', 'mid', 'display_name'.")
    return class_map

# Укажите путь к файлу yamnet_class_map.csv
class_map_path = "project_practicum/yamnet_class_map.csv"
class_names = load_class_map(class_map_path)

# Проверка загрузки классов
if class_names:
    st.write(f"Успешно загружено {len(class_names)} классов.")
else:
    st.error("Не удалось загрузить список классов.")

# Очередь для хранения данных аудио
audio_queue = queue.Queue()

# Флаг для остановки записи
stop_listening = threading.Event()

# Хранилище для всех результатов анализа
analysis_results = []

# Функция для записи аудио с отображением уровня громкости
def record_audio_with_visualization(duration=15):
    """Функция для записи аудио с микрофона и отображением уровня громкости в реальном времени."""
    st.write("Запись аудио и визуализация уровня громкости...")
    audio_data = []

    fig, ax = plt.subplots()
    ax.set_ylim(-1, 1)
    line, = ax.plot([], [])
    placeholder = st.empty()
    countdown_placeholder = st.empty()

    start_time = time.time()

    def audio_callback(indata, frames, time, status):
        if status:
            print(status)
        audio_data.append(indata.copy())
        line.set_ydata(indata[:, 0])
        line.set_xdata(np.arange(len(indata[:, 0])))
        ax.relim()
        ax.autoscale_view()

        remaining_time = max(0, duration - int(time.time() - start_time))
        with _lock:
            placeholder.pyplot(fig)
            countdown_placeholder.write(f"Осталось секунд: {remaining_time}")

    with sd.InputStream(samplerate=16000, channels=1, callback=audio_callback):
        sd.sleep(duration * 1000)

    return np.concatenate(audio_data, axis=0)

# Функция для анализа звука
def classify_audio(audio):
    try:
        audio = np.asarray(audio, dtype=np.float32).flatten()

        if len(audio) == 0:
            raise ValueError("Файл аудио пустой или не поддерживается.")

        # Передача данных в модель
        scores, embeddings, spectrogram = model(audio)

        # Определение топового класса
        top_class_index = np.argmax(scores.numpy()[0])
        top_class_name = class_names[top_class_index]
        top_score = scores.numpy()[0, top_class_index]

        result = f"**Обнаруженный звук:** {top_class_name}, **Уверенность:** {top_score:.2f}"
        analysis_results.insert(0, result)
        st.success(result)

    except Exception as e:
        st.error(f"Произошла ошибка при обработке звука: {e}")

# Интерфейс приложения
st.title("WildSound: Анализ звуков природы")
st.write("Загрузите аудиофайл или включите микрофон для анализа звуков природы!")

# Загрузка аудиофайла через интерфейс
uploaded_file = st.file_uploader("Выберите аудиофайл (.wav)", type=["wav"])

if uploaded_file is not None:
    try:
        # Загрузка и анализ аудиофайла
        audio, sr = librosa.load(uploaded_file, sr=16000)
        classify_audio(audio)
    except Exception as e:
        st.error(f"Произошла ошибка при обработке файла: {e}")

# Флаг для управления состоянием кнопки
if 'is_recording' not in st.session_state:
    st.session_state['is_recording'] = False

# Одна кнопка для управления записью
if st.session_state['is_recording']:
    if st.button("Выключить микрофон"):
        st.session_state['is_recording'] = False
        st.write("Микрофон выключен.")
else:
    if st.button("Включить микрофон"):
        st.session_state['is_recording'] = True
        st.write("Микрофон включен. Запись звука...")
        audio = record_audio_with_visualization(duration=15)
        classify_audio(audio)

# Отображение всех результатов анализа
st.write("### История анализов")
for result in analysis_results:
    st.write(result)
