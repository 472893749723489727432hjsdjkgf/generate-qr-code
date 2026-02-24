import { useState, useEffect } from 'react';
import axios from 'axios';

const ImageDisplay = ({ filePath }) => {
    const [imgUrl, setImgUrl] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!filePath) return;

        const fetchImage = async () => {
            setLoading(true);
            try {
                const response = await axios.get(`http://localhost:8080/api/get_img`, {
                    params: { file_path: filePath },
                    responseType: 'blob'
                });
                const blobUrl = URL.createObjectURL(response.data);
                setImgUrl(blobUrl);
            } catch (error) {
                console.error("Ошибка загрузки изображения:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchImage();
        // Чистим память
        return () => { if (imgUrl) URL.revokeObjectURL(imgUrl); };
    }, [filePath]);

    if (loading) return <p>Загрузка QR...</p>;

    return (
        <div style={{ marginTop: '20px' }}>
            {imgUrl ? <img src={imgUrl} alt="QR Result" style={{ maxWidth: '300px' }} /> : <p>Ожидание ссылки...</p>}
        </div>
    );
};

export default ImageDisplay;
