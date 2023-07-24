function sendRequest() {
    const xhr = new XMLHttpRequest();
    let counter = document.getElementById('requestCounter');
    xhr.open("GET", "http://0.0.0.0:5000/send_request");
    xhr.onload = () => {
        response = JSON.parse(xhr.responseText);
        if (response['status_code'] == 200) {
            counter.value++;
        }
    }
    xhr.send();
}