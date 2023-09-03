function sendRequest() {
    const xhr = new XMLHttpRequest();
    let counter = document.getElementById('requestCounter');
    xhr.open("GET", "http://127.0.0.1:5000/send_request");
    xhr.onload = () => {
        response = JSON.parse(xhr.responseText);
        if (response['status_code'] == 200) {
            counter.value++;
        }
    }
    xhr.send();
}