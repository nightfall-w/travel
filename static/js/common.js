function getHotScheme(){
    fetch('/info/schemes', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-CSRFToken': $.cookie('csrftoken')    // 请求头必须携带csrf_token,不然会csrf验证失败 403
    },
    }).then(function (response) {
        if (response.status === 200) {
            response.json().then(function (json) {
                console.log(json)
            })
        }
    })
}