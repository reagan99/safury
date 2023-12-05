function updateFileName() {
    // 파일 입력 요소 가져오기
    var fileInput1 = document.getElementById('file1');
   
    // 라벨 요소 가져오기
    var fileLabel1 = document.getElementById('file1_name');

    // 선택된 파일이 있는지 확인
    if (fileInput1.files.length > 0) {
        // 파일 이름 가져오기
        var fileName = fileInput1.files[0].name;

        // 라벨에 파일 이름 표시
        fileLabel1.innerText = fileName;
    } else {
        // 파일이 선택되지 않았을 경우 기본 문구 표시
        'Click to upload summary';
    }

    if (fileInput2.files.length > 0) {
        // 파일 이름 가져오기
        var fileName = fileInput2.files[0].name;

        // 라벨에 파일 이름 표시
        fileLabel2.innerText = fileName;
    } else {
        // 파일이 선택되지 않았을 경우 기본 문구 표시
        'Click to upload wrong answers';
    }
}
function updateFileName2() {
    var fileInput2 = document.getElementById('file2');
    var fileLabel2 = document.getElementById('file2_name');

    if (fileInput2.files.length > 0) {
        // 파일 이름 가져오기
        var fileName = fileInput2.files[0].name;

        // 라벨에 파일 이름 표시
        fileLabel2.innerText = fileName;
    } else {
        // 파일이 선택되지 않았을 경우 기본 문구 표시
        'Click to upload wrong answers';
    }
}