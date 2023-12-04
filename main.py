from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import numpy as np
from scipy.io import wavfile
from io import BytesIO
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# 함수: 오디오에 워터마크 삽입
def insert_watermark(original_audio, watermark_text):
    fs, original_audio = wavfile.read(BytesIO(original_audio))
    watermark_binary = ''.join(format(ord(char), '08b') for char in watermark_text)

    while len(watermark_binary) < len(original_audio):
        watermark_binary += watermark_binary

    watermark_binary = watermark_binary[:len(original_audio)]
    watermark_data = np.array([int(bit) for bit in watermark_binary])

    original_fft = np.fft.fft(original_audio)
    watermark_fft = np.fft.fft(watermark_data)

    watermarked_fft = original_fft + watermark_fft
    watermarked_audio = np.fft.ifft(watermarked_fft).real

    return fs, watermarked_audio.astype(original_audio.dtype)

# 엔드포인트: 오디오 파일 업로드
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        watermark_text = "qwer"  # 삽입할 워터마크 텍스트
        fs, watermarked_audio = insert_watermark(contents, watermark_text)

        # 새로운 파일로 저장 (임시 파일 또는 고유한 파일 이름을 사용해야 함)
        output_filename = "watermarked_audio.wav"
        wavfile.write(output_filename, fs, watermarked_audio)

        return {"message": "워터마크가 성공적으로 삽입되었습니다.", "filename": output_filename}

    except Exception as e:
        return {"error": str(e)}

# 엔드포인트: 워터마크가 삽입된 오디오 파일 다운로드
@app.get("/download/")
async def download_file():
    try:
        filename = "watermarked_audio.wav"  # 이전 엔드포인트에서 생성한 파일 이름 사용
        return FileResponse(filename, media_type="audio/wav", filename="watermarked_audio.wav")

    except Exception as e:
        return {"error": str(e)}


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
