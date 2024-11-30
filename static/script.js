fetch('/', {
    method: 'POST',
    body: new FormData(this)
})
.then(response => response.json())
.then(data => {
    if (data.status === 'success') {
        let audioURL = `/static/${data.file}`;
        document.querySelector('audio source').src = audioURL;
        document.querySelector('audio').load();
        new bootstrap.Modal(document.getElementById('successModal')).show();
    } else {
        alert('Error generating audio: ' + (data.message || 'Unknown error'));
    }
    document.getElementById('loadingSpinner').style.display = 'none';
})
.catch(error => {
    console.error('Error:', error);
    alert('An error occurred while connecting to the server.');
    document.getElementById('loadingSpinner').style.display = 'none';
});
