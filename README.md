# 🤟 ASL Learning Web Application

An interactive web application that combines **machine learning** with **web development** to create an engaging American Sign Language (ASL) learning platform. The app uses **YOLO11** computer vision model for real-time sign language detection and recognition.

![ASL Learning App](https://img.shields.io/badge/ASL-Learning-blue) ![React](https://img.shields.io/badge/React-19.0.0-blue) ![Flask](https://img.shields.io/badge/Flask-3.1.2-green) ![YOLO](https://img.shields.io/badge/YOLO-11-orange) ![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-red)

## 🌟 Features

- **📚 Educational Interface**: Learn basic ASL signs with visual references
- **🤖 Real-time AI Practice**: Webcam-based sign language practice with AI feedback
- **🎯 Live Detection**: YOLO model processes webcam feed in real-time
- **👥 Team Project**: Built by 5 computer science students
- **📱 Responsive Design**: Modern web interface with React Router navigation

## 🎯 Supported Sign Language Gestures

The application recognizes **6 basic ASL signs**:
- 👋 **Hello** - Wave gesture
- ❤️ **I Love You** - Specific hand shape
- ❌ **No** - Shaking motion
- 🙏 **Please** - Praying hands gesture
- 🙏 **Thanks** - Thumbs up or specific gesture
- ✅ **Yes** - Nodding motion

## 🏗️ Architecture

### Frontend (React.js)
- **React 19.0.0** with React Router for navigation
- Modern web interface with multiple pages:
  - **Home**: Landing page with team member information
  - **Learn**: Educational content showing ASL signs
  - **Practice AI**: Real-time webcam-based sign language practice
  - **Cause**: Information about the project's purpose

### Backend (Flask)
- **Flask** web server handling ML inference
- **OpenCV** for webcam capture and video processing
- **Ultralytics YOLO** for real-time sign language detection
- Live video streaming via Flask's `Response` with multipart encoding

### Machine Learning
- **YOLO11** model trained on custom ASL dataset
- **6 sign language classes** with real-time detection
- Model trained for 50 epochs with 640px image size
- Custom dataset with 120 training images and 30 test images

## 🚀 Quick Start

### Prerequisites

- **Node.js** (v14 or higher)
- **Python 3.8+**
- **Webcam** (for AI practice feature)
- **macOS/Linux/Windows**

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ASL/learn-asl
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Set up Python virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Python dependencies**
   ```bash
   pip install flask opencv-python ultralytics
   ```

### Running the Application

1. **Start both frontend and backend**
   ```bash
   npm start
   ```

2. **Or start them separately**
   ```bash
   # Terminal 1 - React Frontend
   npm run start:react
   
   # Terminal 2 - Flask Backend
   npm run start:flask
   ```

3. **Access the application**
   - **Frontend**: http://localhost:3000
   - **Backend API**: http://localhost:5000
   - **Webcam Feed**: http://localhost:5000/video_feed

## 📁 Project Structure

```
ASL/
├── learn-asl/                    # Main application directory
│   ├── src/
│   │   ├── Pages/               # React components
│   │   │   ├── home.js          # Home page
│   │   │   ├── learn.js         # Learning page
│   │   │   ├── PracticeAI.js    # AI practice page
│   │   │   └── cause.js         # About page
│   │   ├── App.js               # Main React app
│   │   └── App.css              # Global styles
│   ├── templates/               # Flask HTML templates
│   ├── static/                  # CSS and static assets
│   ├── models/                  # YOLO model files
│   │   └── best.pt             # Trained ASL detection model
│   ├── app.py                   # Flask backend server
│   ├── package.json             # Node.js dependencies
│   └── venv/                    # Python virtual environment
├── Sign_language_data/          # Training dataset
│   ├── train/                   # Training images and labels
│   ├── test/                    # Test images and labels
│   └── data.yaml               # Dataset configuration
├── runs/detect/                 # Model training results
└── README.md                    # This file
```

## 🎮 Usage

### Learning Mode
1. Navigate to the **Learn** page
2. Study the basic ASL signs with visual references
3. Practice the gestures shown

### AI Practice Mode
1. Click **"Practice with AI"** button
2. Allow webcam access when prompted
3. Make sign language gestures in front of the camera
4. Watch as the AI detects and labels your gestures in real-time

### Testing the YOLO Model
```bash
# Run YOLO model directly
cd learn-asl
source venv/bin/activate
python test_yolo.py
```

## 🔧 Configuration

### Model Configuration
The YOLO model is configured in `Sign_language_data/data.yaml`:
```yaml
train: /path/to/train/images
val: /path/to/test/images
nc: 6
names: ['Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes']
```

### Flask Configuration
- **Host**: 0.0.0.0 (all interfaces)
- **Port**: 5000
- **Debug Mode**: Enabled in development

## 🛠️ Development

### Adding New Sign Language Gestures
1. Collect training images for the new gesture
2. Label the images using YOLO annotation format
3. Update `data.yaml` with the new class
4. Retrain the model:
   ```bash
   yolo task=detect mode=train data=data.yaml model=yolov5s.pt epochs=50
   ```

### Customizing the UI
- Modify React components in `src/Pages/`
- Update styles in corresponding CSS files
- Add new routes in `App.js`

## 🐛 Troubleshooting

### Common Issues

1. **Port 5000 already in use**
   ```bash
   # Kill processes using port 5000
   lsof -ti:5000 | xargs kill
   ```

2. **Webcam not working**
   - Check camera permissions in system settings
   - Ensure no other applications are using the camera

3. **YOLO model not loading**
   - Verify `models/best.pt` exists
   - Check file permissions

4. **Flask server not starting**
   - Ensure virtual environment is activated
   - Check Python dependencies are installed

### Debug Mode
```bash
# Run Flask in debug mode
cd learn-asl
source venv/bin/activate
python app.py
```

## 📊 Performance

- **Detection Speed**: ~200-600ms per frame
- **Model Size**: ~5.5MB (best.pt)
- **Supported Resolutions**: 640x640 (input), 1920x1080 (webcam)
- **FPS**: ~2-5 FPS (depending on hardware)

## 👥 Team

This project was developed by a team of 5 computer science students:

- **Kevin Dinh** - Computer Science
- **Srinarayan Srikanth** - Computer Science
- **Kenny Brown** - Computing Security Technology  
- **Soham Deshmukh** - Computer Science
- **Dhruv Goli** - omputer Science


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📚 Resources

- [YOLO Documentation](https://docs.ultralytics.com/)
- [React Documentation](https://reactjs.org/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [American Sign Language Resources](https://www.nidcd.nih.gov/health/american-sign-language)

## 🙏 Acknowledgments

- **Ultralytics** for the YOLO framework
- **React Team** for the frontend framework
- **Flask Team** for the backend framework
- **OpenCV** for computer vision capabilities
- **ASL Community** for sign language resources

---

**Made with ❤️ for the Deaf and Hard of Hearing Community**

For questions or support, please open an issue in the repository.
# ASLearn
