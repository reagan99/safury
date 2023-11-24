import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt

# 워터마크가 삽입된 음성 파일 읽기
fs, watermarked_audio = wavfile.read('watermarked_audio.wav')

# FFT를 사용하여 주파수 도메인으로 변환
watermarked_fft = np.fft.fft(watermarked_audio)

# 원본 음성 파일 읽기
fs, original_audio = wavfile.read('mono-piano.wav')

# FFT를 사용하여 주파수 도메인으로 변환
original_fft = np.fft.fft(original_audio)

# 워터마크 추출
extracted_fft = watermarked_fft - original_fft
extracted_watermark = np.fft.ifft(extracted_fft).real

# 추출된 워터마크 데이터를 확인
print(extracted_watermark)

# 추출된 워터마크 데이터를 다시 문자열로 변환
extracted_watermark_binary = ''.join([str(int(bit)) for bit in extracted_watermark])

# 추출된 이진 문자열을 8비트씩 분할하여 출력
for i in range(0, len(extracted_watermark_binary), 8):
    extracted_byte = extracted_watermark_binary[i:i + 8]
    print(extracted_byte)

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

print("Extracted Watermark Text:", extracted_watermark_text)

# 시각화
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(watermarked_audio)
plt.title('Watermarked Audio')
plt.subplot(3, 1, 2)
plt.plot(original_audio)
plt.title('Original Audio')
plt.subplot(3, 1, 3)
plt.plot(extracted_fft)
plt.title('Extracted FFT')
plt.tight_layout()
plt.show()
