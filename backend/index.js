const express = require('express');
const cors = require('cors');
const app = express();
const port = 8080;

app.use(cors());

app.get('/api/info', (req, res) => {
  res.json({ 
    project: "MobileNetV2 Face Recognition",
    version: "1.0.0",
    engine: "PyTorch + MobileNetV2",
    status: "Active",
    stats: {
        parameters: "3.4M",
        accuracy: "92.5%",
        latency: "45ms"
    }
  });
});

app.listen(port, () => {
  console.log(`Backend listening at http://localhost:${port}`);
});
