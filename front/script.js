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
    location.reload(true);
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

// submit button이 클릭되면, 파일 입력이 됐는지 확인하기
// 파일이 입력됐다면, 입력받은 파일을 서버로 보내기
// 서버에서 영상 처리 완료되면, 영상 서버로부터 받아서 저장하고 다음 페이지로 전환하기
function submit_clicked() {
    // // 파일 선택 확인
    // var fileInput = document.getElementById('music_file');
    // var file = fileInput.files[0];
    // if (!file) {
    //     alert('Please select a file.');
    //     return;
    // }

    // // 파일을 서버로 전송
    // var formData = new FormData();
    // formData.append('file', file);

    // fetch('/process_music', {
    //     method: 'POST',
    //     body: formData
    // })
    // .then(response => response.json())
    // .then(result => {
    //     alert(result);

    //     // 페이지 전환 애니메이션 적용
    //     const list = document.querySelectorAll('li');
    //     list.forEach(li => {
    //         li.style.transform = 'translateY(-200%)';
    //     });
    // })
    // .catch(error => {
    //     alert('An error occurred: ' + error.message);
    // });
    
    // 일단 백엔드 연동하기 뭐해서 내려가는 것만 해놓음 이거 지우고 구현하면 됨
    const list = document.querySelectorAll('li');
        list.forEach(li => {
            li.style.transform = 'translateY(-200%)';
        });
}

// download button이 클릭되면, 다운로드받기
function download_clicked() {
    window.location.href = '/download/watermark.wav';
}
