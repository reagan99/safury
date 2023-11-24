import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
# 원본 음성 파일 읽기
fs, original_audio = wavfile.read('mono-piano.wav')

# 워터마크 데이터 생성 (예: "qwer" 문자열을 바이너리로 변환)
watermark_text = "qwer"
watermark_binary = ''.join(format(ord(char), '08b') for char in watermark_text)

# 데이터 길이를 원본 오디오 데이터와 정확하게 일치시키기
while len(watermark_binary) < len(original_audio):
    watermark_binary += watermark_binary

watermark_binary = watermark_binary[:len(original_audio)]
watermark_data = np.array([int(bit) for bit in watermark_binary])

# FFT를 사용하여 주파수 도메인으로 변환
original_fft = np.fft.fft(original_audio)
watermark_fft = np.fft.fft(watermark_data)

# 워터마크 삽입
watermarked_fft = original_fft + watermark_fft

# 역 FFT를 사용하여 시간 도메인으로 변환
watermarked_audio = np.fft.ifft(watermarked_fft).real




extracted_fft = watermarked_fft - original_fft
extracted_fft_audio = np.fft.ifft(extracted_fft).real

plt.plot(extracted_fft)
plt.title('Watermarked Audio')
plt.show()





# 삽입된 워터마크를 가진 음성 파일 저장 (샘플링 레이트와 비트 깊이를 원본과 동일하게 설정)
wavfile.write('watermarked_audio.wav', fs, watermarked_audio.astype(original_audio.dtype))
extracted_watermark_binary = ''.join([str(int(bit)) for bit in extracted_fft_audio])

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
