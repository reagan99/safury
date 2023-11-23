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
        fileLabel.innerText = 'Click to upload file';
    }
}

