function scroll_elements(translation) {
    const list = document.querySelectorAll('li');
    list.forEach(li => {
        li.style.transform = `translateY(${translation}%)`;
    });
}

function scroll_down() {
    scroll_elements(-100);
}

function scroll_up() {
    scroll_elements(0);
    location.reload(true);
}

function updateFileName() {
    var fileInput = document.getElementById('music_file');
    var fileLabel = document.getElementById('music_file_name');

    fileLabel.innerText = fileInput.files.length > 0
        ? fileInput.files[0].name
        : 'Click to upload file';
}

async function submit_clicked() {
    try {
        var fileInput = document.getElementById('music_file');
        var file = fileInput.files[0];
        if (!file) {
            alert('Please select a file.');
            return;
        }

        var formData = new FormData();
        formData.append('file', file);

        const response = await fetch('/upload/', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            alert('File submitted successfully!');
            document.getElementById('upload_files').innerText = 'Audio watermark inserted';
            document.getElementById('download_button').style.display = 'block';
            scroll_elements(-200);
        } else {
            alert('Failed to submit file. Please try again.');
        }

    } catch (error) {
        console.error('Error:', error);
    }
}

async function download_clicked() {
    try {
        const response = await fetch('/download/watermarked_audio.wav');  // 파일 이름을 제공하세요
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);

        const link = document.createElement('a');
        link.href = url;
        link.download = 'watermarked_audio.wav';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);

    } catch (error) {
        console.error('에러:', error);
    }
}

