$(function () {
    // 页面加载,以默认的排序方式请求数据
    getData();
});


function getDataBySort(obj){
    // 根据排序方式发送graphql请求，获取数据
    if(!$(obj).parent().attr('class')){
        $(obj).parent().siblings().removeClass('active up').find('i').remove();
        $(obj).parent().attr('class','active up');
        var i = '<i class="fa fa-long-arrow-down"></i>';
        $(obj).append(i);
        var sort = $(obj).attr('sort');
        $(obj).attr('sort',sort-(2*sort))
        getData(limit = 18, offset = 0, sort_by = sort-(2*sort));
    }else{
        var sort = $(obj).attr('sort');
        var sortUpDown = $(obj).children('i').attr('class');
        if (sortUpDown === 'fa fa-long-arrow-down'){
            $(obj).children('i').attr('class','fa fa-long-arrow-up');
            $(obj).attr('sort',Math.abs(sort));
        }else{
            $(obj).children('i').attr('class','fa fa-long-arrow-down');
            $(obj).attr('sort',sort-(2*sort))
        }
        var sort = $(obj).attr('sort');
        getData(limit = 18, offset = 0, sort_by = sort)
    }
}

function loadGrade() {
    // Smaller size star
    $('.star-rating-12px').raty({
        path: "/static/images/raty",
        starHalf: 'star-half-sm.png',
        starOff: 'star-off-sm.png',
        starOn: 'star-on-sm.png',
        readOnly: true,
        round: {down: .2, full: .6, up: .8},
        half: true,
        space: false,
        score: function () {
            return $(this).attr('data-rating-score');
        }
    });
}


function foldIntroduce() {
    // 只显示一部分介绍信息,多的部分截掉
    let len = 350;      //默认显示字数
    let ctns = $(".introduce");  //获取div对象
    let scheme_length = ctns.length;
    for (i = 0; i < scheme_length; i++) {
        let ctn = ctns[i];
        let content = ctn.innerHTML;//获取div里的内容
        let span = document.createElement("span");     //创建<span>元素
        span.innerHTML = content.substring(0, len) + '&nbsp;&nbsp...';     //span里的内容为content的前len个字符
        // 设置div内容为空，span元素 a元素加入到div中
        ctn.innerHTML = "";
        ctn.appendChild(span);
        ctn.style.display = "block";
    }
}

function applyTemplate(scheme) {
    let name = scheme.name;
    let introduce = scheme.introduce;
    let originating = scheme.originating;
    let day = scheme.day;
    let night = scheme.night;
    let endLocale = scheme.endLocale;
    let price = scheme.price;
    let reviewNum = scheme.reviewNum;
    let beLike = scheme.beLike;
    let grade = scheme.grade;
    let photoUrl = scheme.photoUrl;
    var scheme_content = '<div class="package-list-item clearfix">' +
        '<div class="image">' + '<img src="' + '../../' + photoUrl + '" alt="Tour Package"/>' +
        '<div class="absolute-in-image">' +
        '<div class="duration"><span>' + day + ' 天' + night + '夜</span></div>' +
        '</div>' +
        '</div>' +
        '<div class="content">' +
        '<h5>' + name +
        '<button class="btn"><i class="fa fa-heart-o" be_like="' + beLike + '"></i></button>' +
        '</h5>' +
        '<div class="row gap-10">' +
        '<div class="col-sm-12 col-md-9">' +
        '<div class="introduce" style="display: none">' +
        '<p class="line">' + introduce + '</p>' +
        '</div>' +
        '<br>' +
        '<ul class="list-info">' +
        '<li><span class="icon"><i class="fa fa-map-marker"></i></span> <span class="font600">终点:</span>' + endLocale + '</li>' +
        '<li><span class="icon"><i class="fa fa-flag"></i></span> <span class="font600">起点:</span>' + originating + '</li>' +
        '</ul>' +
        '</div>' +
        '<div class="col-sm-12 col-md-3 text-right text-left-sm">' +
        '<div class="rating-wrapper">' +
        '<div class="raty-wrapper">' +
        '<div class="star-rating-12px" data-rating-score="' + grade + '"></div>' +
        '<span>' + reviewNum + ' /评论</span>' +
        '</div>' +
        '</div>' +
        '<div class="price">￥' + price + '</div>' +
        '<a href="detail-page.html" class="btn btn-primary btn-sm">详情</a>' +
        '</div>' +
        '</div>' +
        '</div>' +
        '</div>';
    return scheme_content
}

function loadDate(pageSchemes) {
    // 遍历加载所有scheme数据
    let scheme_list_template = '';
    pageSchemes.forEach(function (scheme) {
        aSchemeData = applyTemplate(scheme);
        scheme_list_template += aSchemeData;
    });
    $('.package-list-item-wrapper').html(scheme_list_template);
    foldIntroduce();
    loadGrade();
}

function loadPagination(page_info) {
    // 渲染分页条
    const limit = page_info.limit;
    const offset = page_info.offset;
    const totalData = page_info.total;
    const pageSchemes = page_info.pageScheme;
    const pageCount = Math.ceil(totalData / limit);
    const current = Math.floor(offset / limit);
    $(".allPage").text(pageCount);
    $(".totalData").text(totalData);
    $("#Pagination").pagination(pageCount, {
        current_page: current,
    });
    loadDate(pageSchemes)
}

function getData(limit = 18, offset = 0, sort_by = 0) {
    // 定义graphql查询语句
    const query =
        'query pageSchemes($limit: Int, $offset: Int, $sortBy: Int) { ' +
        'pageSchemes(limit: $limit, offset: $offset, sortBy: $sortBy) {' +
        'limit,' +
        'offset,' +
        'total,' +
        'pageScheme{' +
        'id,' +
        'name,' +
        'introduce,' +
        'originating,' +
        'endLocale,' +
        'price,' +
        'reviewNum,' +
        'beLike,' +
        'grade,' +
        'day,' +
        'night,' +
        'photoUrl,' +
        '}' +
        '}' +
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
        if (response.status === 200) {
            response.json().then(function (json) {
                const page_info = json.data.pageSchemes;
                // 将返回数据通过loadData()到页面渲染
                loadPagination(page_info[0]);
            })
        }
        else {
            response.json().then(function (json) {
                console.log(json.errors);
            })
        }
    }).catch(function (e) {
        console.log('error: ' + e.toString());
    })
}