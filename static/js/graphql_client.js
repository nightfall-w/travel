$(function () {
    getData()
});


function getData(limit = 18, offset = 0, sort_by = 0) {
    const query = 'query pageSchemes($limit:Int,$offset:Int,$sortBy:Int){pageSchemes(limit:$limit,offset:$offset,sortBy:$sortBy){total}}';

    const variables = {limit: limit, offset: offset, sortBy: sort_by};

    fetch('/public_graphql/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': $.cookie('csrftoken')
        },
        body: JSON.stringify({query: query, variables: variables}),
    }).then(function (response) {
        //打印返回的json数据
        if (response.status === 200){
        response.json().then(function (json) {
            console.log(json.data);
            return json.data
        })}
        else{
            response.json().then(function (json) {
            console.log(json.errors);
        })}
    }).catch(function (e) {
        console.log('error: ' + e.toString());
    })
}