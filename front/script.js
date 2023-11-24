function scroll_down() {
    const list = document.querySelectorAll('li');
    list.forEach(li => {
        li.style.transform = 'translateY(-100%)';
    });
}
function scroll_up() {
    const list = document.querySelectorAll('li');
    list.forEach(li => {
        li.style.transform = 'translateY(0%)';
    });
}

function updateFileName() {
    // 파일 입력 요소 가져오기
    var fileInput = document.getElementById('music_file');
    
    // 라벨 요소 가져오기
    var fileLabel = document.getElementById('music_file_name');
    
    // 선택된 파일이 있는지 확인
    if (fileInput.files.length > 0) {
        // 파일 이름 가져오기
        var fileName = fileInput.files[0].name;
        
        // 라벨에 파일 이름 표시
        fileLabel.innerText = fileName;
    } else {
        // 파일이 선택되지 않았을 경우 기본 문구 표시
        'Click to upload file';
    }
}

// 서버로 입력받은 파일 보내기
function submit_clicked() {
    // 파일 선택 확인
    var fileInput = document.getElementById('music_file');
    var file = fileInput.files[0];
    if (!file) {
        alert('Please select a file.');
        return;
    }

    // 파일을 서버로 전송
    var formData = new FormData();
    formData.append('file', file);

    fetch('/bocho', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(result => {
        // 실행 결과를 화면에 표시
        alert(result);
    })
    .catch(error => {
        alert('An error occurred: ' + error.message);
    });
}