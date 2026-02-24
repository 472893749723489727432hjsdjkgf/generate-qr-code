import { useState } from 'react';
import axios from 'axios';
import ImageDisplay from './ImageDisplay';

function App() {
    const [urlValue, setUrlValue] = useState("");
    const [pathOnServer, setPathOnServer] = useState("");

    const handleSendUrl = async (e) => {
    e.preventDefault();
    try {
        const res = await axios.post("http://localhost:8080/api/send_url", {
            url: urlValue
        });
        setPathOnServer(res.data.file_path);

        console.log("Ответ от бэка (POST):", res.data);

        setPathOnServer(res.data.file_path);
    } catch (err) {
        console.error("Ошибка запроса:", err);
    }
};

    return (
        <div style={{ padding: '20px' }}>
            <h1>Генератор QR-кодов</h1>
            <form onSubmit={handleSendUrl}>
                <input
                    type="text"
                    value={urlValue}
                    onChange={(e) => setUrlValue(e.target.value)}
                    placeholder="Вставьте ссылку"
                />
                <button type="submit">Сгенерировать</button>
            </form>

            {/*  */}
            <ImageDisplay filePath={pathOnServer} />
        </div>
    );
}

export default App;
