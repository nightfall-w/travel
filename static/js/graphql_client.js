$(function () {
    gloabel_destinations = $('select[name="destination"]').val();
    gloabel_months = $('select[name="month"]').val();
    gloabel_years = $('select[name="year"]').val();
    // 页面加载,以默认的排序方式请求数据
    if (window.location.pathname === '/info/result-list/') {
        limit = 12;
        getData(limit, 0, 0, gloabel_destinations, gloabel_months, gloabel_years);
    } else {
        limit = 18;
        getData(limit, 0, 0, gloabel_destinations, gloabel_months, gloabel_years)
    }
});

function skipPage() {
    // go标签里 输入页码进行跳转
    let page_id = $("input[name='pageId']").val();
    let maxPage = parseInt($('.next').prev().text());
    page_id = parseInt(page_id, 10);
    if (page_id == 'NaN' || page_id <= 0 || !Number.isInteger(page_id) || page_id > maxPage) {
        console.log('错误的页码：' + page_id)
    } else {
        let offset = (page_id - 1) * limit;
        if ($('.fa.fa-long-arrow-up').length === 1) {
            var sort_by = parseInt($('.fa.fa-long-arrow-up').parent().attr('sort'))
        } else {
            var sort_by = parseInt($('.fa.fa-long-arrow-down').parent().attr('sort'))
        }
        $('.content-wrapper').hide(1);
        $('.loadbox').show(1);
        getData(limit, offset, sort_by, gloabel_destinations, gloabel_months, gloabel_years)
    }
}

function getSpecifiedPage(page_id) {
    // 点击页码条获取指定页数据
    if ($('.current').text() === page_id + 1) {
        return false
    }
    let offset = page_id * limit;
    if ($('.fa.fa-long-arrow-up').length === 1) {
        var sort_by = parseInt($('.fa.fa-long-arrow-up').parent().attr('sort'))
    } else {
        var sort_by = parseInt($('.fa.fa-long-arrow-down').parent().attr('sort'))
    }
    $('.content-wrapper').hide(1);
    $('.loadbox').show(1);
    getData(limit, offset, sort_by, gloabel_destinations, gloabel_months, gloabel_years)
}

function getDataBySort(obj) {
    // 根据排序方式发送graphql请求，获取数据
    if (!$(obj).parent().attr('class')) {
        $(obj).parent().siblings().removeClass('active up').find('i').remove();
        $(obj).parent().attr('class', 'active up');
        let i = '<i class="fa fa-long-arrow-down"></i>';
        $(obj).append(i);
        let sort = $(obj).attr('sort');
        $(obj).attr('sort', Math.abs(sort) - (2 * Math.abs(sort)));
        $('.content-wrapper').hide(1);
        $('.loadbox').show(1);
        getData(limit, 0, Math.abs(sort) - (2 * Math.abs(sort)), gloabel_destinations, gloabel_months, gloabel_years);
    } else {
        let sort = parseInt($(obj).attr('sort'));
        let sortUpDown = $(obj).children('i').attr('class');
        if (sortUpDown === 'fa fa-long-arrow-down') {
            $(obj).children('i').attr('class', 'fa fa-long-arrow-up');
            $(obj).attr('sort', Math.abs(sort));
        } else {
            $(obj).children('i').attr('class', 'fa fa-long-arrow-down');
            $(obj).attr('sort', sort - (2 * sort))
        }
        sort = parseInt($(obj).attr('sort'));
        $('.content-wrapper').hide(1);
        $('.loadbox').show(1);
        getData(limit, 0, sort, gloabel_destinations, gloabel_months, gloabel_years)
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
    let id = scheme.Id;
    let title = scheme.title;
    let subhead = scheme.subhead;
    let departure = scheme.departure;
    let day = scheme.day;
    let night = scheme.night;
    let destination = scheme.destination;
    let price = scheme.price;
    price = '￥' + price;
    let reviewNum = scheme.review.length;
    let beLike = scheme.beLike;
    let grade = scheme.avgScore;
    let firstPhoto = scheme.scenicImages[1];
    let scheme_content = '<div class="package-list-item clearfix">' +
        '<div class="image">' + '<img src="' + '../../' + firstPhoto + '" alt="Tour Package"/>' +
        '<div class="absolute-in-image">' +
        '<div class="duration"><span>' + day + ' 天' + night + '夜</span></div>' +
        '</div>' +
        '</div>' +
        '<div class="content">' +
        '<h5>' + title +
        '<button class="btn"><i class="fa fa-heart-o" be_like="' + beLike + '"></i></button>' +
        '</h5>' +
        '<div class="row gap-10">' +
        '<div class="col-sm-12 col-md-9">' +
        '<div class="introduce" style="display: none">' +
        '<p class="line">' + subhead + '</p>' +
        '</div>' +
        '<br>' +
        '<ul class="list-info">' +
        '<li><span class="icon"><i class="fa fa-map-marker"></i></span> <span class="font600">终点:</span>' + destination + '</li>' +
        '<li><span class="icon"><i class="fa fa-flag"></i></span> <span class="font600">起点:</span>' + departure + '</li>' +
        '</ul>' +
        '</div>' +
        '<div class="col-sm-12 col-md-3 text-right text-left-sm">' +
        '<div class="rating-wrapper">' +
        '<div class="raty-wrapper">' +
        '<div class="star-rating-12px" data-rating-score="' + grade + '"></div>' +
        '<span>' + reviewNum + ' /评论</span>' +
        '</div>' +
        '</div>' +
        '<div class="price">' + price + '</div>' +
        '<a href="/info/detail/' + id + '" class="btn btn-primary btn-sm">详情</a>' +
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
    $('.content-wrapper').show(1);
    $('.loadbox').hide(1);
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
        callback: getSpecifiedPage
    });
    loadDate(pageSchemes)
}

function getData(limit, offset, sort_by, destinations, months, years) {
    // 定义graphql查询语句
    const query =
        'query pageSchemes($limit: Int, $offset: Int, $sortBy: Int, $destinations: String, $months: String, $years: String) { ' +
        'pageSchemes(limit: $limit, offset: $offset, sortBy: $sortBy, destinations: $destinations, months: $months, years: $years) {' +
        'limit,' +
        'offset,' +
        'total,' +
        'pageScheme{' +
        'Id,' +
        'title,' +
        'subhead,' +
        'departure,' +
        'destination,' +
        'price,' +
        'beLike,' +
        'avgScore,' +
        'day,' +
        'night,' +
        'scenicImages,' +
        'review{content}' +
        '}' +
        '}' +
        '}';

    // graphql语句传参
    const variables = {
        limit: limit,
        offset: offset,
        sortBy: sort_by,
        destinations: destinations,
        months: months,
        years: years
    };

    // 发送graphql请求
    fetch('/public_graphql/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-CSRFToken': $.cookie('csrftoken')    // 请求头必须携带csrf_token,不然会csrf验证失败 403
        },
        body: JSON.stringify({query: query, variables: variables})
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