const video = document.getElementById('video');
const loadingOverlay = document.getElementById('loading-overlay');
const loadingStatus = document.getElementById('loading-status');
const fpsDisplay = document.getElementById('fps-counter');
const faceCountDisplay = document.getElementById('face-count');

// URL chứa các models (sử dụng models có sẵn trên github của vladmandic)
const MODEL_URL = 'https://vladmandic.github.io/face-api/model/';

async function startVideo() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { width: 1280, height: 720 } });
        video.srcObject = stream;
    } catch (err) {
        console.error('Không thể truy cập camera:', err);
        loadingStatus.innerText = 'Lỗi truy cập camera. Vui lòng cấp quyền!';
    }
}

async function loadModels() {
    loadingStatus.innerText = 'Đang tải TinyFaceDetector (MobileNetV2 based)...';
    // TinyFaceDetector được xây dựng dựa trên các nguyên lý của MobileNet (Depthwise Separable Convolutions)
    await faceapi.nets.tinyFaceDetector.loadFromUri(MODEL_URL);
    
    loadingStatus.innerText = 'Đang tải Landmark & Expression models...';
    await faceapi.nets.faceLandmark68Net.loadFromUri(MODEL_URL);
    await faceapi.nets.faceExpressionNet.loadFromUri(MODEL_URL);
    
    loadingStatus.innerText = 'Tải mô hình thành công!';
    setTimeout(() => {
        loadingOverlay.style.opacity = '0';
        setTimeout(() => loadingOverlay.style.display = 'none', 500);
    }, 1000);
}

let lastTime = 0;
let frameCount = 0;

async function onPlay() {
    if (video.paused || video.ended || !faceapi.nets.tinyFaceDetector.params) {
        return setTimeout(() => onPlay());
    }

    const canvas = faceapi.createCanvasFromMedia(video);
    document.getElementById('canvas-container').append(canvas);
    const displaySize = { width: video.clientWidth, height: video.clientHeight };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
        // Sử dụng TinyFaceDetector để tối ưu tốc độ (MobileNetV2 principles)
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
            .withFaceLandmarks()
            .withFaceExpressions();

        const resizedDetections = faceapi.resizeResults(detections, displaySize);
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        
        // Tùy chỉnh màu sắc cho phù hợp với thiết kế premium
        const drawOptions = {
            boxColor: '#6366f1',
            textColor: '#f8fafc',
            lineWidth: 2
        };
        
        faceapi.draw.drawDetections(canvas, resizedDetections, drawOptions);
        faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
        
        // Cập nhật số lượng khuôn mặt
        faceCountDisplay.innerText = detections.length;

        // Tính toán FPS
        const now = performance.now();
        if (lastTime > 0) {
            const dt = now - lastTime;
            const fps = Math.round(1000 / dt);
            fpsDisplay.innerText = fps;
        }
        lastTime = now;
        
    }, 100); // 10 FPS cho nhẹ nhưng mượt mà
}

async function fetchBackendInfo() {
    const backendInfoDiv = document.getElementById('backend-info');
    try {
        // Thử kết nối tới backend (mặc định port 8080 nếu chạy manual, hoặc qua proxy nếu chạy docker)
        const response = await fetch('http://localhost:8080/api/info');
        const data = await response.json();
        
        backendInfoDiv.innerHTML = `
            <p style="color: #4ade80; font-weight: 600;">● Online</p>
            <p>Engine: ${data.engine}</p>
            <p>Accuracy: ${data.stats.accuracy}</p>
            <p>Latency: ${data.stats.latency}</p>
        `;
    } catch (err) {
        backendInfoDiv.innerHTML = `
            <p style="color: #f87171; font-weight: 600;">● Offline</p>
            <p style="font-size: 0.8rem; opacity: 0.7;">Vui lòng chạy backend để xem dữ liệu AI.</p>
        `;
    }
}

async function init() {
    await fetchBackendInfo();
    await loadModels();
    await startVideo();
    video.addEventListener('play', onPlay);
}

init();
