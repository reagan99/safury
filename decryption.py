from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import numpy as np
import uvicorn
from scipy.io import wavfile
from io import BytesIO

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# 엔드포인트: 두 음성을 빼서 복원한 값 HTML에 표시
@app.post("/decryption/", response_class=HTMLResponse)
async def subtract_and_restore(file1: UploadFile = File(...), file2: UploadFile = File(...), request: Request = None):
    try:
        contents1 = await file1.read()
        contents2 = await file2.read()

        fs, contents1 = wavfile.read(BytesIO(contents1))
        fs, contents2 = wavfile.read(BytesIO(contents2))
        
        # 두 음성 파일을 빼서 복원
        extracted_fft = np.fft.fft(contents1) - np.fft.fft(contents2)
        extracted_watermark = np.fft.ifft(extracted_fft).real

        # 추출된 워터마크 데이터를 다시 문자열로 변환
        extracted_watermark_binary = ''.join([str(int(bit)) for bit in extracted_watermark])

        # 추출된 이진 문자열을 8비트씩 분할하여 10진수로 변환한 다음, 문자열로 복원
        extracted_watermark_text = ''
        for i in range(0, len(extracted_watermark_binary), 8):
            extracted_byte = extracted_watermark_binary[i:i + 8]
            try:
                extracted_char = chr(int(extracted_byte, 2))
                if extracted_char.isalpha():
                    extracted_watermark_text += extracted_char
            except ValueError:
                pass
        # HTML 템플릿을 사용하여 결과 반환
        return templates.TemplateResponse("result.html", {"request": request, "extracted_watermark_text": extracted_watermark_text})

    except Exception as e:
        return {"error": str(e)}

# Root endpoint
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("result.html", {"request": request, "extracted_watermark_text": ""})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
