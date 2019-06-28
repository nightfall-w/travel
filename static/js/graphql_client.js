$(function () {
    const page_info = getData();
});


const schemeListTemplate = """

                        """

function loadDate(pageSchemes){;
    pageSchemes.forEach(function(scheme){
        let template = '<div class="package-list-item clearfix">'+
                            '<div class="image">'
                                <img src="{% static 'images/tour-package/01.jpg' %}" alt="Tour Package"/>

                                <div class="absolute-in-image">
                                    <div class="duration"><span>4 days 3 nights</span></div>
                                </div>
                            </div>

                            <div class="content">
                                <h5>Paris in Love
                                    <button class="btn"><i class="fa fa-heart-o"></i></button>
                                </h5>
                                <div class="row gap-10">
                                    <div class="col-sm-12 col-md-9">

                                        <p class="line18">Letter wooded direct two men indeed income sister. Impression
                                            up admiration partiality is...</p><br>
                                        <ul class="list-info">
                                            <li><span class="icon"><i class="fa fa-map-marker"></i></span> <span
                                                    class="font600">Ending Point:</span> France
                                            </li>
                                            <li><span class="icon"><i class="fa fa-flag"></i></span> <span
                                                    class="font600">Starting Point:</span> Paris
                                            </li>
                                        </ul>

                                    </div>
                                    <div class="col-sm-12 col-md-3 text-right text-left-sm">

                                        <div class="rating-wrapper">
                                            <div class="raty-wrapper">
                                                <div class="star-rating-12px" data-rating-score="4.0"></div>
                                                <span> / 7 review</span>
                                            </div>
                                        </div>

                                        <div class="price">$1422</div>

                                        <a href="detail-page.html" class="btn btn-primary btn-sm">view</a>

                                    </div>
                                </div>
                            </div>

                        </div>
    });
}

// 渲染分页条
function loadPagination(page_info){
    const limit = page_info.limit;
    const offset = page_info.offset;
    const totalData = page_info.total;
    const pageSchemes = page_info.pageScheme
    const pageCount = Math.ceil(totalData / limit);
    const current = Math.floor(offset / limit);
    $(".allPage").text(pageCount);
    $(".totalData").text(totalData);
    $("#Pagination").pagination(pageCount,{
        current_page:current,
    });
    loadDate(pageSchemes)
}

function getData(limit = 18, offset = 0, sort_by = 0) {
    // 定义graphql查询语句
    const query =
        'query pageSchemes($limit: Int, $offset: Int, $sortBy: Int) { '+
            'pageSchemes(limit: $limit, offset: $offset, sortBy: $sortBy) {'+
                'limit,'+
                'offset,'+
                'total,'+
                'pageScheme{'+
                    'id,'+
                    'name,'+
                    'introduce,'+
                    'originating,'+
                    'endLocale,'+
                    'price,'+
                    'reviewNum,'+
                    'beLike,'+
                    'grade,'+
                '}'+
            '}'+
        '}';

    // graphql语句传参
    const variables = {limit: limit, offset: offset, sortBy: sort_by};

    // 发送graphql请求
    fetch('/public_graphql/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': $.cookie('csrftoken')    // 请求头必须携带csrf_token,不然会csrf验证失败 403
        },
        body: JSON.stringify({query: query, variables: variables}),
    }).then(function (response) {
        //打印返回的json数据
        if (response.status === 200){
        response.json().then(function (json) {
            console.log(json.data)
            const page_info = json.data.pageSchemes
            // 将返回数据通过loadData()到页面渲染
            loadPagination(page_info[0]);
        })}
        else{
            response.json().then(function (json) {
            console.log(json.errors);
        })}
    }).catch(function (e) {
        console.log('error: ' + e.toString());
    })
}